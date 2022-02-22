#!/usr/bin/env python3

import os
import socket
import yaml

# путь к файлу в котором хранится последнее состояние
state_file = 'state.yaml'

# если файл существует...
state_file = os.path.abspath(state_file)
if os.path.isfile(state_file):
    # проверяем права
    if os.access(state_file, os.R_OK) and os.access(state_file, os.W_OK):
        # читаем последнее состояние
        with open(state_file) as f:
            urls = yaml.safe_load(f)
    else: 
        # для работы не хватает прав
        print(f"[ERROR] Файл '{state_file}' должен быть доступен на чтение и запись!')
        sys.exit(1)
else:
    # иначе - инициализируем словарь имен без адресов
    urls = {'drive.google.com':'0.0.0.0', 'mail.google.com':'0.0.0.0', 'google.com':'0.0.0.0'}

# для каждого имени
for url, ip in urls.items():
    # получаем адрес
    new_ip = socket.gethostbyname(url)
    # если адрес изменился...
    if new_ip != ip:
        # оповещаем пользоваиеля
        print(f"[ERROR] {url} IP mismatch: {ip} {new_ip}")
        urls[url] = new_ip
    else:
        # выводим соответствие 
        print(f"{url} - {ip}")

# сохраняем новое состояние
with open(state_file, 'w') as f:
    document = yaml.dump(urls, f) 
