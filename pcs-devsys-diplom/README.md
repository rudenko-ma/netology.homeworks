# Курсовая работа по итогам модуля "DevOps и системное администрирование"

## Процесс установки и настройки ufw

```bash
vagrant@diplom:~$ sudo apt install ufw
Reading package lists... Done
Building dependency tree       
Reading state information... Done
ufw is already the newest version (0.36-6ubuntu1).
0 upgraded, 0 newly installed, 0 to remove and 76 not upgraded.
vagrant@diplom:~$ sudo ufw allow 22/tcp
Rules updated
Rules updated (v6)
vagrant@diplom:~$ sudo ufw allow 443/tcp
Rules updated
Rules updated (v6)
vagrant@diplom:~$ sudo ufw enable
Command may disrupt existing ssh connections. Proceed with operation (y|n)? y
Firewall is active and enabled on system startup
vagrant@diplom:~$ sudo ufw status verbose
Status: active
Logging: on (low)
Default: deny (incoming), allow (outgoing), disabled (routed)
New profiles: skip

To                         Action      From
--                         ------      ----
22/tcp                     ALLOW IN    Anywhere                  
443/tcp                    ALLOW IN    Anywhere                  
22/tcp (v6)                ALLOW IN    Anywhere (v6)             
443/tcp (v6)               ALLOW IN    Anywhere (v6)
```

## Процесс установки и выпуска сертификата с помощью hashicorp vault
## Процесс установки и настройки сервера nginx
## Страница сервера nginx в браузере хоста не содержит предупреждений
## Скрипт генерации нового сертификата работает (сертификат сервера ngnix должен быть "зеленым")
## Crontab работает (выберите число и время так, чтобы показать что crontab запускается и делает что надо)
