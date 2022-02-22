#!/usr/bin/env python3

import os
import sys

# получаем путь к репозиторию
if len(sys.argv) > 1:
    repo_path = os.path.abspath(sys.argv[1])
else:
    repo_path= os.path.dirname(os.path.abspath(__file__))

# выполняем команды и получаем результат 
bash_command = [f"cd {repo_path}", "git status 2>&1"]
result_os = os.popen(' && '.join(bash_command)).read()

# построчно перебираем результат
for result in result_os.split('\n'):
    # фатальная ошибка - ругаемся и выходим
    if result.find('fatal') != -1:
        print(f"Директория '{repo_path}' не является GIT репозиторием!")
        sys.exit(1)

    # есть изменения - сообщаем полный путь к файлу
    if result.find('modified:') != -1 or result.find('изменено:') != -1:
        prepare_result = result.split(':')[1].strip()
        print(os.path.join(repo_path, prepare_result))
