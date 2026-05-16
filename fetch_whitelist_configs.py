#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations

import json
import time
import urllib.request
from collections import OrderedDict
from pathlib import Path
from urllib.parse import parse_qsl, urlsplit


ROOT = Path(__file__).resolve().parent

SOURCES = OrderedDict(
    {
        "igareck_rus_mobile": "https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/Vless-Reality-White-Lists-Rus-Mobile.txt",
        "igareck_rus_mobile_2": "https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/Vless-Reality-White-Lists-Rus-Mobile-2.txt",
        "zieng2_lite": "https://raw.githubusercontent.com/zieng2/wl/main/vless_lite.txt",
    }
)


OUTPUTS = {
    "primary": ROOT / "whitelist_primary.txt",
    "extended": ROOT / "whitelist_extended.txt",
    "all": ROOT / "whitelist_all.txt",
    "ios": ROOT / "whitelist_ios.txt",
    "android": ROOT / "whitelist_android.txt",
    "stats": ROOT / "whitelist_stats.json",
}


SUPPORTED_ANDROID_FINGERPRINTS = {"", "chrome", "firefox", "safari", "randomized"}


def fetch_text(url: str) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": "RUKA-Whitelist-Collector/1.0"})
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8", errors="ignore")


def extract_vless_links(text: str) -> list[str]:
    links: list[str] = []
    seen: set[str] = set()
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or not line.startswith("vless://"):
            continue
        if line in seen:
            continue
        seen.add(line)
        links.append(line)
    return links


def dedupe(items: list[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for item in items:
        if item in seen:
            continue
        seen.add(item)
        result.append(item)
    return result


def extract_query_params(link: str) -> dict[str, str]:
    try:
        query = urlsplit(link).query
    except ValueError:
        return {}
    return {key.lower(): value for key, value in parse_qsl(query, keep_blank_values=True)}


def has_android_query_garbage(link: str) -> bool:
    normalized = link.lower()
    garbage_markers = (
        "%5c%22",
        "%22%2c",
        "headertype=none%22",
        "none\\\\",
        "headertype=none\\\",",
        "\\#",
    )
    return any(marker in normalized for marker in garbage_markers)


def is_android_friendly(link: str) -> bool:
    if has_android_query_garbage(link):
        return False

    params = extract_query_params(link)
    security = params.get("security", "").lower()
    transport = params.get("type", "").lower()
    fingerprint = params.get("fp", "").lower()

    if security not in {"reality", "tls"}:
        return False
    if fingerprint not in SUPPORTED_ANDROID_FINGERPRINTS:
        return False
    if security == "reality" and (not params.get("pbk") or not params.get("sni")):
        return False
    if security == "tls" and not (params.get("sni") or params.get("host")):
        return False
    if transport == "ws" and not params.get("path"):
        return False

    return True


def split_by_fp(links: list[str]) -> tuple[list[str], list[str]]:
    ios: list[str] = []
    android: list[str] = []
    for link in links:
        normalized = link.lower()
        if "fp=ios" in normalized:
            ios.append(link)
        elif is_android_friendly(link):
            android.append(link)
    return ios, android


def write_lines(path: Path, lines: list[str]) -> None:
    payload = "\n".join(lines).strip()
    if payload:
        payload += "\n"
    path.write_text(payload, encoding="utf-8")


def main() -> None:
    collected: dict[str, list[str]] = {}
    source_stats: dict[str, dict] = {}

    for name, url in SOURCES.items():
        text = fetch_text(url)
        links = extract_vless_links(text)
        collected[name] = links
        source_stats[name] = {
            "url": url,
            "links": len(links),
        }

    igareck_links = dedupe(collected["igareck_rus_mobile"] + collected["igareck_rus_mobile_2"])
    zieng2_links = dedupe(collected["zieng2_lite"])
    all_links = dedupe(igareck_links + zieng2_links)
    ios_links, android_links = split_by_fp(all_links)

    write_lines(OUTPUTS["primary"], igareck_links)
    write_lines(OUTPUTS["extended"], zieng2_links)
    write_lines(OUTPUTS["all"], all_links)
    write_lines(OUTPUTS["ios"], ios_links)
    write_lines(OUTPUTS["android"], android_links)

    stats = {
        "updated_at": int(time.time()),
        "updated_at_iso": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "totals": {
            "primary": len(igareck_links),
            "extended": len(zieng2_links),
            "all": len(all_links),
            "ios": len(ios_links),
            "android": len(android_links),
        },
    }
    OUTPUTS["stats"].write_text(json.dumps(stats, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print("Whitelist files updated:")
    for key in ("primary", "extended", "all", "ios", "android"):
        print(f"  {OUTPUTS[key].name}: {stats['totals'][key]}")


if __name__ == "__main__":
    main()
