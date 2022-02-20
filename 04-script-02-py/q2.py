#!/usr/bin/env python3

import os

modified = 'modified:'
repo_path= os.path.dirname(os.path.abspath(__file__))
bash_command = [f"cd {repo_path}", "git status"]
result_os = os.popen(' && '.join(bash_command)).read()
#is_change = False  -- не используется
for result in result_os.split('\n'):
    if result.find(modified) != -1:
        prepare_result = result.split(':')[1].strip()
        print(os.path.join(repo_path, prepare_result))
