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

<details>
  <summary>Установим vault согласно инструкции</summary>

  ```shell
vagrant@diplom:~$ curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo apt-key add -
OK
vagrant@diplom:~$ sudo apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main"
Get:1 https://apt.releases.hashicorp.com focal InRelease [14.6 kB]                                                                  
Get:2 http://security.ubuntu.com/ubuntu focal-security InRelease [114 kB]                                      
Get:3 https://apt.releases.hashicorp.com focal/main amd64 Packages [50.1 kB]
Hit:4 http://us.archive.ubuntu.com/ubuntu focal InRelease                                                    
Get:5 http://us.archive.ubuntu.com/ubuntu focal-updates InRelease [114 kB]
Get:6 http://security.ubuntu.com/ubuntu focal-security/main i386 Packages [395 kB]
Get:7 http://security.ubuntu.com/ubuntu focal-security/main amd64 Packages [1310 kB]                                                                                                                             
Get:8 http://security.ubuntu.com/ubuntu focal-security/main Translation-en [228 kB]                                                                                                                              
Get:9 http://security.ubuntu.com/ubuntu focal-security/main amd64 c-n-f Metadata [9732 B]                                                                                                                        
Get:10 http://security.ubuntu.com/ubuntu focal-security/restricted amd64 Packages [799 kB]                                                                                                                       
Get:11 http://security.ubuntu.com/ubuntu focal-security/restricted Translation-en [114 kB]                                                                                                                       
Get:12 http://us.archive.ubuntu.com/ubuntu focal-backports InRelease [108 kB]                                                                                                                                    
Get:13 http://us.archive.ubuntu.com/ubuntu focal-updates/main amd64 Packages [1640 kB]                                                                                                                           
Get:14 http://us.archive.ubuntu.com/ubuntu focal-updates/main i386 Packages [615 kB]                                                                                                                             
Get:15 http://us.archive.ubuntu.com/ubuntu focal-updates/main Translation-en [312 kB]                                                                                                                            
Get:16 http://us.archive.ubuntu.com/ubuntu focal-updates/main amd64 c-n-f Metadata [14.8 kB]                                                                                                                     
Get:17 http://us.archive.ubuntu.com/ubuntu focal-updates/restricted amd64 Packages [853 kB]                                                                                                                      
Get:18 http://us.archive.ubuntu.com/ubuntu focal-updates/restricted Translation-en [122 kB]                                                                                                                      
Get:19 http://us.archive.ubuntu.com/ubuntu focal-updates/universe amd64 Packages [909 kB]                                                                                                                        
Get:20 http://us.archive.ubuntu.com/ubuntu focal-updates/universe i386 Packages [672 kB]                                                                                                                         
Get:21 http://us.archive.ubuntu.com/ubuntu focal-updates/multiverse amd64 Packages [23.8 kB]                                                                                                                     
Get:22 http://us.archive.ubuntu.com/ubuntu focal-updates/multiverse i386 Packages [8464 B]                                                                                                                       
Fetched 8425 kB in 11s (761 kB/s)                                                                                                                                                                                
Reading package lists... Done
vagrant@diplom:~$ sudo apt-get update && sudo apt-get install vault
Hit:1 http://security.ubuntu.com/ubuntu focal-security InRelease                         
Hit:2 http://us.archive.ubuntu.com/ubuntu focal InRelease                                
Hit:3 http://us.archive.ubuntu.com/ubuntu focal-updates InRelease  
Hit:4 http://us.archive.ubuntu.com/ubuntu focal-backports InRelease
Hit:5 https://apt.releases.hashicorp.com focal InRelease           
Reading package lists... Done
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following NEW packages will be installed:
  vault
0 upgraded, 1 newly installed, 0 to remove and 77 not upgraded.
Need to get 69.6 MB of archives.
After this operation, 188 MB of additional disk space will be used.
Get:1 https://apt.releases.hashicorp.com focal/main amd64 vault amd64 1.9.4 [69.6 MB]
Fetched 69.6 MB in 24s (2902 kB/s)                                                                                                                                                                               
Selecting previously unselected package vault.
(Reading database ... 111201 files and directories currently installed.)
Preparing to unpack .../archives/vault_1.9.4_amd64.deb ...
Unpacking vault (1.9.4) ...
Setting up vault (1.9.4) ...
Generating Vault TLS key and self-signed certificate...
Generating a RSA private key
............................................................................................................................................................................................................................................................................................................................................................++++
..............................................................................................................................................++++
writing new private key to 'tls.key'
-----
Vault TLS key and self-signed certificate have been generated in '/opt/vault/tls'.
  ```
</details>

## Процесс установки и настройки сервера nginx
## Страница сервера nginx в браузере хоста не содержит предупреждений
## Скрипт генерации нового сертификата работает (сертификат сервера ngnix должен быть "зеленым")
## Crontab работает (выберите число и время так, чтобы показать что crontab запускается и делает что надо)
