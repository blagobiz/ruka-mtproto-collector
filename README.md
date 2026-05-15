# RUKA MTProto Collector

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Auto_Update-Every_Hour-success?style=for-the-badge&logo=github-actions)
![Brand](https://img.shields.io/badge/Brand-RUKA%20VPN-1f8bff?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-orange?style=for-the-badge)

**Брендированный MTProto collector для Telegram под проект `RUKA VPN`.**

Этот репозиторий нужен для трёх задач:

1. собирать свежие MTProto-прокси из открытых источников;
2. фильтровать и публиковать списки `RU`, `Global` и `All`;
3. давать людям понятную публичную точку входа по запросам вроде:
   - `прокси для Telegram бесплатно`
   - `MTProto прокси Telegram`
   - `telegram proxy free`
   - `MTProto для Telegram`

---

## Актуальные списки

После каждого автообновления в репозитории публикуются:

| RU сегмент | Global / EU | Все прокси |
| :--- | :--- | :--- |
| `proxy_ru.txt` | `proxy_eu.txt` | `proxy_all.txt` |
| лучшие варианты для Telegram из РФ | общий международный пул | полный актуальный список |

Основные файлы:

- `proxy_ru.txt`
- `proxy_eu.txt`
- `proxy_all.txt`
- `verified/proxy_ru_verified.txt`
- `verified/proxy_eu_verified.txt`
- `verified/proxy_all_verified.txt`
- `verified/proxy_links_tme_clean.txt`
- `verified/proxy_all_verified.json`
- `verified/proxy_stats_verified.json`

---

## Мобильная страница

Если человек открывает репозиторий с телефона, ему не нужно копировать ссылки вручную.

Используй страницу:

- `mobile.html`

Она загружает `verified/proxy_links_tme_clean.txt` и показывает кнопки формата:

- `Подключить MTProto #1`
- `Подключить MTProto #2`
- `Подключить MTProto #3`

По нажатию Telegram сразу открывает окно подключения прокси.

---

## Как это работает

Collector проходит несколько этапов:

1. **Сбор**
   - тянет MTProto-прокси из открытых TXT / API / GitHub-источников;
   - умеет разбирать `tg://proxy`, `t.me/proxy`, `host:port:secret`, JSON.

2. **Декодирование**
   - пытается извлечь домен маскировки из секрета;
   - на этом шаге можно разделять прокси по сценарию использования.

3. **Фильтрация**
   - режет слабые, лишние или нежелательные варианты;
   - выделяет RU-friendly слой и глобальный слой.

4. **Проверка**
   - делает TCP-check;
   - при наличии `API_ID / API_HASH` может работать и через более строгую Telegram-проверку.

5. **Публикация**
   - обновляет `verified/*`;
   - копирует итоговые `.txt` в корень;
   - поддерживает GitHub Pages как публичную витрину проекта.

---

## Что это даёт проекту RUKA VPN

Этот репозиторий можно использовать как:

- публичный SEO-вход для бесплатных MTProto;
- GitHub-страницу для мобильного трафика;
- источник `.txt` и `.json` для сайта `RUKA VPN`;
- branded entrypoint, который переводит человека из бесплатного MTProto в платный VPN.

То есть логика простая:

- **нужен только Telegram** → человек использует бесплатный MTProto;
- **нужен YouTube, Instagram, ChatGPT и другие сервисы** → человек переходит в `RukaVPN_bot`.

---

## Автообновление

В `.github/workflows/update.yml` уже подготовлен GitHub Actions workflow.

Он:

1. запускается каждый час;
2. ставит зависимости;
3. запускает `python main.py --top 200`;
4. обновляет `verified/*`;
5. обновляет файлы в корне;
6. коммитит изменения только если список реально поменялся.

---

## Локальный запуск

```bash
git clone https://github.com/blagobiz/ruka-mtproto-collector.git
cd ruka-mtproto-collector
pip install -r requirements.txt
python main.py --top 200
```

Если хочешь включить более строгую проверку через Telethon:

```bash
export MTPROXY_API_ID=123456
export MTPROXY_API_HASH=your_hash
python main.py --top 200
```

---

## Публикация в GitHub

Оптимальный сценарий:

1. создать новый репозиторий `ruka-mtproto-collector`;
2. загрузить эту папку;
3. включить GitHub Actions;
4. включить GitHub Pages от `main` branch;
5. при желании доработать `index.html` и `mobile.html` под свои CTA и ссылки.

---

## SEO-заметки

Если хочешь, чтобы репозиторий находили по ключам, а не только как код:

- держи подробный `README`;
- не убирай `index.html` и `mobile.html`;
- регулярно обновляй файлы;
- связывай репозиторий с сайтом и Telegram-ботом;
- не плодить дубли на зеркалах без ясного canonical.

---

## Брендовые ссылки

- VPN bot: `https://t.me/RukaVPN_bot`
- основной бренд: `RUKA VPN`

---

## Attribution

Часть collector-логики основана на MIT-лицензированном upstream-проекте.  
Подробности смотри в [THIRD_PARTY_NOTICES.md](./THIRD_PARTY_NOTICES.md).
