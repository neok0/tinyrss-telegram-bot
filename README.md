# TinyRSS Telegram Bot

This little utility can be used to send news notification to your phone.
It checks your existing TinyRSS instance for unread news and sends them
on your device via Telegram message.

## Prerequisites
1. Working Instance of TinyRSS. If not already running,
[here][tinyrss] is one of many good tutorials how to set one up.
2. Telegram App installed on your phone.
3. Enabled Telegram Bot. Have a look at [this][telegram] tutorial for setting up a new one.
4. Copy settings_template.py file to settings.py.
5. Edit settings.py file with your data (see settings_template.py file
for examples):
    - TINYRSS: url, user, password, feeds
    - TELEGRAM: token, chat_id
    - CHAT: users (optional), buttons (optional)

## Installation
1. Create virtual environment e.g.:
 `python3 -m venv .venv`
2. Work on virtual env. e.g.: `source .venv/bin/activate`
3. Install required packages
`pip3 install -r requirements.txt`
4. Run `python3 tinyrss-telegram-bot.py`
5. For persistence e.g. create cronjob


[tinyrss]:https://www.digitalocean.com/community/tutorials/how-to-install-ttrss-with-nginx-for-debian-7-on-a-vps
[telegram]:https://core.telegram.org/bots#6-botfather