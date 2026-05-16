# Бесплатные прокси для Telegram и белые списки обхода | RUKA VPN

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python)
![Telegram](https://img.shields.io/badge/Telegram-MTProto-2496ed?style=for-the-badge&logo=telegram)
![Обновления](https://img.shields.io/badge/Обновления-Свежие_списки-success?style=for-the-badge&logo=github)
![Бренд](https://img.shields.io/badge/Бренд-RUKA%20VPN-1f8bff?style=for-the-badge)

**RUKA MTProto Collector** — это брендированный репозиторий под `RUKA VPN`, где публикуются:

- **бесплатные MTProto-прокси для Telegram**
- **VLESS-конфиги по обходу и белым спискам**
- готовые `.txt`-файлы для iPhone, Android и ПК
- GitHub Pages-витрина под поисковые запросы

Если говорить просто: это публичная точка входа, где человек может взять либо **прокси для Telegram бесплатно**, либо **конфиги белых списков / обхода**, а потом перейти в полноценный VPN через `@RukaVPN_bot`.

## Что есть в этом репозитории

### MTProto для Telegram

Готовые raw-файлы:

- `RU`: <https://raw.githubusercontent.com/blagobiz/ruka-mtproto-collector/main/proxy_ru.txt>
- `Global / EU`: <https://raw.githubusercontent.com/blagobiz/ruka-mtproto-collector/main/proxy_eu.txt>
- `All`: <https://raw.githubusercontent.com/blagobiz/ruka-mtproto-collector/main/proxy_all.txt>

Проверенные MTProto-файлы:

- `verified/proxy_ru_verified.txt`
- `verified/proxy_eu_verified.txt`
- `verified/proxy_all_verified.txt`
- `verified/proxy_links_tme_clean.txt`
- `verified/proxy_all_verified.json`
- `verified/proxy_stats_verified.json`

### Белые списки и обход

Готовые raw-файлы:

- `Основной слой`: <https://raw.githubusercontent.com/blagobiz/ruka-mtproto-collector/main/whitelist_primary.txt>
- `Расширенный слой`: <https://raw.githubusercontent.com/blagobiz/ruka-mtproto-collector/main/whitelist_extended.txt>
- `All`: <https://raw.githubusercontent.com/blagobiz/ruka-mtproto-collector/main/whitelist_all.txt>
- `iPhone`: <https://raw.githubusercontent.com/blagobiz/ruka-mtproto-collector/main/whitelist_ios.txt>
- `Android / универсальные`: <https://raw.githubusercontent.com/blagobiz/ruka-mtproto-collector/main/whitelist_android.txt>

Служебный файл:

- `whitelist_stats.json`

## Публичные страницы GitHub Pages

После включения GitHub Pages в репозитории доступны:

- `index.html` — витрина для бесплатных MTProto-прокси
- `mobile.html` — мобильный вход для Telegram proxy
- `whitelist.html` — витрина под белые списки и VLESS-конфиги обхода

## Для каких запросов подходит

Этот репозиторий заточен под русские и международные интенты:

- `прокси для telegram бесплатно`
- `бесплатные прокси telegram`
- `mtproto proxy telegram`
- `telegram proxy free`
- `telegram proxy iphone`
- `telegram proxy android`
- `белые списки vpn`
- `конфиги обхода блокировок`
- `vless белые списки`
- `конфиги для сложного мобильного интернета`

## Что даёт MTProto, а что дают белые списки

### MTProto

Используется, если нужен доступ только в Telegram.

Подходит для:

- Telegram iPhone
- Telegram Android
- Telegram Desktop

### Белые списки / обход

Используются, если нужен более широкий обход через VLESS-конфиги, особенно на сложных мобильных сетях и нестабильных провайдерах.

Подходят для:

- клиентов V2Ray / sing-box / Hiddify / Happ / других совместимых клиентов
- сценариев с мобильным интернетом
- белых списков и обхода блокировок

## Как обновляются белые списки

Для этого добавлен отдельный скрипт:

- `fetch_whitelist_configs.py`

Он:

1. скачивает свежие VLESS-конфиги из нескольких публичных whitelist feeds
2. извлекает только валидные `vless://` ссылки
3. удаляет дубли
4. собирает:
   - `whitelist_primary.txt`
   - `whitelist_extended.txt`
   - `whitelist_all.txt`
   - `whitelist_ios.txt`
   - `whitelist_android.txt`
5. пишет `whitelist_stats.json`

## Как использовать

### Если нужен только Telegram

1. Открой `mobile.html`
2. Нажми кнопку подключения
3. Telegram сразу откроет экран импорта прокси

### Если нужны белые списки / обход

1. Открой `whitelist.html`
2. Выбери нужный `.txt`
3. Импортируй конфиг в свой клиент

### Если нужен полноценный VPN

Переходи в:

- <https://t.me/RukaVPN_bot>

## Запуск локально

### MTProto collector

```bash
git clone https://github.com/blagobiz/ruka-mtproto-collector.git
cd ruka-mtproto-collector
pip install -r requirements.txt
python main.py --top 200
```

### Белые списки / обход

```bash
python fetch_whitelist_configs.py
```

## Зачем это полезно для RUKA VPN

Репозиторий работает сразу в нескольких ролях:

- как **SEO-вход** под бесплатные MTProto-прокси
- как **SEO-вход** под белые списки и обход
- как **GitHub brand page**
- как источник `.txt` и `.json` для сайта и бота
- как переход из бесплатного входа в полноценный VPN

Логика простая:

- нужен только Telegram -> бесплатный MTProto
- нужен обход и мобильный интернет -> белые списки / VLESS
- нужен готовый полноценный продукт -> `RukaVPN_bot`

## Брендовые ссылки

- VPN bot: <https://t.me/RukaVPN_bot>
- основной сайт: <https://rukavpn.site/>

## Attribution

Часть collector-логики основана на открытом upstream-проекте под MIT.  
Подробности: [THIRD_PARTY_NOTICES.md](./THIRD_PARTY_NOTICES.md)
