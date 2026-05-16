# Free Telegram Proxy & MTProto Proxy List by RUKA VPN

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python)
![Telegram](https://img.shields.io/badge/Telegram-MTProto-2496ed?style=for-the-badge&logo=telegram)
![Updates](https://img.shields.io/badge/Updates-Fresh_Lists-success?style=for-the-badge&logo=github)
![Brand](https://img.shields.io/badge/Brand-RUKA%20VPN-1f8bff?style=for-the-badge)

**RUKA MTProto Collector** is a branded repository with fresh **free Telegram proxy** and **MTProto proxy** lists for users who need quick Telegram access on **iPhone, Android, Windows and macOS**.

Если говорить просто: это публичная точка входа, где публикуются свежие **MTProto-прокси для Telegram**, готовые `.txt`-списки, мобильная страница для быстрого подключения и ссылки на полноценный **VPN** через `@RukaVPN_bot`.

## What You Get

- fresh **Telegram MTProto proxy list**
- free **Telegram proxy for iPhone**
- free **Telegram proxy for Android**
- public raw files for clients and websites
- GitHub-hosted branded entrypoint for search traffic
- mobile page that opens Telegram proxy links directly

## Актуальные MTProto списки

Используй готовые raw-файлы:

- `RU`: <https://raw.githubusercontent.com/blagobiz/ruka-mtproto-collector/main/proxy_ru.txt>
- `Global / EU`: <https://raw.githubusercontent.com/blagobiz/ruka-mtproto-collector/main/proxy_eu.txt>
- `All`: <https://raw.githubusercontent.com/blagobiz/ruka-mtproto-collector/main/proxy_all.txt>

Проверенные файлы:

- `verified/proxy_ru_verified.txt`
- `verified/proxy_eu_verified.txt`
- `verified/proxy_all_verified.txt`
- `verified/proxy_links_tme_clean.txt`
- `verified/proxy_all_verified.json`
- `verified/proxy_stats_verified.json`

## GitHub Pages

Публичные страницы репозитория:

- main landing: `index.html`
- mobile entrypoint: `mobile.html`

После включения GitHub Pages их можно использовать как:

- landing page под запросы `прокси для Telegram бесплатно`
- mobile page для прямого открытия `tg://proxy`
- branded GitHub-витрину под `RUKA VPN`

## Бесплатные прокси для Telegram

Этот репозиторий заточен под запросы:

- `прокси для telegram бесплатно`
- `бесплатные прокси telegram`
- `mtproto proxy telegram`
- `telegram proxy free`
- `telegram proxy iphone`
- `telegram proxy android`
- `mtproto для telegram`
- `free telegram proxy list`

Идея простая:

- нужен только Telegram -> человек использует **free MTProto**
- нужен YouTube, Instagram, ChatGPT и другие сервисы -> человек переходит в **VPN**

## Как использовать на телефоне

Самый простой путь:

1. Открыть `mobile.html`
2. Нажать кнопку подключения
3. Telegram сразу откроет экран импорта прокси

Если нужен ручной сценарий:

1. Открыть raw-файл из этого репозитория
2. Скопировать ссылку или подписку
3. Импортировать её в нужный клиент

## Для каких клиентов подходит

MTProto-ссылки из этого репозитория можно использовать в:

- Telegram iPhone
- Telegram Android
- Telegram Desktop
- сторонних клиентах, которые поддерживают proxy import

Для полноценных VPN-конфигов и обхода не только Telegram используй:

- `https://t.me/RukaVPN_bot`

## Что делает collector

Collector проходит несколько этапов:

1. **Сбор**
   - получает MTProto-прокси из публичных источников
   - умеет разбирать `tg://proxy`, `t.me/proxy`, `host:port:secret`, JSON

2. **Нормализация**
   - приводит найденные прокси к единому виду
   - удаляет дубли и мусор

3. **Фильтрация**
   - разделяет список на `RU`, `EU / Global` и `All`
   - поддерживает branded публикацию

4. **Проверка**
   - делает базовую проверку доступности
   - оставляет более чистый пул для публикации

5. **Публикация**
   - обновляет `verified/*`
   - копирует итоговые `.txt` в корень
   - поддерживает GitHub как публичную витрину проекта

## Почему это полезно для RUKA VPN

Репозиторий работает сразу в нескольких ролях:

- как **SEO-вход** под бесплатные MTProto-прокси
- как **GitHub brand page**
- как источник `.txt` и `.json` для сайта
- как переход из бесплатного Telegram proxy в платный VPN

Это хороший сценарий для маркетинга:

- бесплатный вход по Telegram-интенту
- доверие через GitHub и обновляемые списки
- апсейл в `@RukaVPN_bot`

## Auto Update

В репозитории подготовлен workflow для регулярного обновления списков.

Логика такая:

1. запускается по расписанию
2. ставит зависимости
3. запускает `python main.py --top 200`
4. обновляет `verified/*`
5. обновляет публичные `.txt`

## Local Run

```bash
git clone https://github.com/blagobiz/ruka-mtproto-collector.git
cd ruka-mtproto-collector
pip install -r requirements.txt
python main.py --top 200
```

Для более строгой проверки:

```bash
export MTPROXY_API_ID=123456
export MTPROXY_API_HASH=your_hash
python main.py --top 200
```

## FAQ

### Это VPN?

Нет. Это **MTProto proxy for Telegram**. Он нужен именно для Telegram.

### Работает ли это на iPhone?

Да, если Telegram на iPhone корректно открывает proxy-link и сам прокси в данный момент живой.

### Работает ли это на Android?

Да, Android тоже поддерживает Telegram proxy links.

### Почему список нужно обновлять часто?

Публичные прокси быстро умирают, поэтому свежесть списка очень важна.

### Когда нужен полноценный VPN?

Когда нужен не только Telegram, а ещё:

- YouTube
- Instagram
- ChatGPT
- браузер
- зарубежные сервисы

Для этого используй `https://t.me/RukaVPN_bot`.

## Brand Links

- VPN bot: <https://t.me/RukaVPN_bot>
- brand site: <https://rukavpn.site/>

## Marketing Notes

Чтобы репозиторий лучше находили:

- держи сильный keyword-rich `README`
- не убирай `index.html` и `mobile.html`
- используй raw-ссылки в Telegram, на сайте и в описаниях
- обновляй файлы регулярно
- связывай репозиторий с брендом `RUKA VPN`

## Attribution

Часть collector-логики основана на открытом upstream-проекте под MIT.  
Подробности: [THIRD_PARTY_NOTICES.md](./THIRD_PARTY_NOTICES.md)
