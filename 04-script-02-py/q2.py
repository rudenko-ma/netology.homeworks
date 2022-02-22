#!/usr/bin/env python3

import os

repo_path= os.path.dirname(os.path.abspath(__file__))
bash_command = [f"cd {repo_path}", "git status"]
result_os = os.popen(' && '.join(bash_command)).read()
#is_change = False  -- не используется
for result in result_os.split('\n'):
    if result.find('modified:') != -1 or result.find('изменено:'):
        prepare_result = result.split(':')[1].strip()
        print(os.path.join(repo_path, prepare_result))
