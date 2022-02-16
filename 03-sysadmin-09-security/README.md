# Домашнее задание к занятию "3.9. Элементы безопасности информационных систем"

## 1. Установите Bitwarden плагин для браузера. Зарегестрируйтесь и сохраните несколько паролей.

Плагин `Bitwarden` установлен. Пароли сохранены.
![](https://github.com/rudenko-ma/netology.homeworks/blob/main/03-sysadmin-09-security/img/q1.png)

## 2. Установите Google authenticator на мобильный телефон. Настройте вход в Bitwarden акаунт через Google authenticator OTP.

Приложение `Google Authenticator` установлено. Двухфакторная аутентификация настроена. Плагин `Bitwarden` запрашивает 6 знаячный пин.
![](https://github.com/rudenko-ma/netology.homeworks/blob/main/03-sysadmin-09-security/img/q2.png)

## 3. Установите apache2, сгенерируйте самоподписанный сертификат, настройте тестовый сайт для работы по HTTPS.

<details>
  <summary>Устанавливаем веб сервер `apache2`</summary>

  ```
vagrant@u20web:~$ sudo apt install apache2 -y     
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following additional packages will be installed:
  apache2-bin apache2-data apache2-utils libapr1 libaprutil1 libaprutil1-dbd-sqlite3 libaprutil1-ldap libjansson4 ssl-cert
Suggested packages:
  apache2-doc apache2-suexec-pristine | apache2-suexec-custom www-browser openssl-blacklist
The following NEW packages will be installed:
  apache2 apache2-bin apache2-data apache2-utils libapr1 libaprutil1 libaprutil1-dbd-sqlite3 libaprutil1-ldap libjansson4 ssl-cert
0 upgraded, 10 newly installed, 0 to remove and 62 not upgraded.
Need to get 1518 kB/1760 kB of archives.
After this operation, 7649 kB of additional disk space will be used.
Get:1 http://us.archive.ubuntu.com/ubuntu focal-updates/main amd64 apache2-bin amd64 2.4.41-4ubuntu3.9 [1180 kB]
Get:2 http://us.archive.ubuntu.com/ubuntu focal-updates/main amd64 apache2-data all 2.4.41-4ubuntu3.9 [159 kB]
Get:3 http://us.archive.ubuntu.com/ubuntu focal-updates/main amd64 apache2-utils amd64 2.4.41-4ubuntu3.9 [84.3 kB]
Get:4 http://us.archive.ubuntu.com/ubuntu focal-updates/main amd64 apache2 amd64 2.4.41-4ubuntu3.9 [95.5 kB]
Fetched 1518 kB in 3s (595 kB/s)
Preconfiguring packages ...
Selecting previously unselected package libapr1:amd64.
(Reading database ... 111201 files and directories currently installed.)
Preparing to unpack .../0-libapr1_1.6.5-1ubuntu1_amd64.deb ...
Unpacking libapr1:amd64 (1.6.5-1ubuntu1) ...
Selecting previously unselected package libaprutil1:amd64.
Preparing to unpack .../1-libaprutil1_1.6.1-4ubuntu2_amd64.deb ...
Unpacking libaprutil1:amd64 (1.6.1-4ubuntu2) ...
Selecting previously unselected package libaprutil1-dbd-sqlite3:amd64.
Preparing to unpack .../2-libaprutil1-dbd-sqlite3_1.6.1-4ubuntu2_amd64.deb ...
Unpacking libaprutil1-dbd-sqlite3:amd64 (1.6.1-4ubuntu2) ...
Selecting previously unselected package libaprutil1-ldap:amd64.
Preparing to unpack .../3-libaprutil1-ldap_1.6.1-4ubuntu2_amd64.deb ...
Unpacking libaprutil1-ldap:amd64 (1.6.1-4ubuntu2) ...
Selecting previously unselected package libjansson4:amd64.
Preparing to unpack .../4-libjansson4_2.12-1build1_amd64.deb ...
Unpacking libjansson4:amd64 (2.12-1build1) ...
Selecting previously unselected package apache2-bin.
Preparing to unpack .../5-apache2-bin_2.4.41-4ubuntu3.9_amd64.deb ...
Unpacking apache2-bin (2.4.41-4ubuntu3.9) ...
Selecting previously unselected package apache2-data.
Preparing to unpack .../6-apache2-data_2.4.41-4ubuntu3.9_all.deb ...
Unpacking apache2-data (2.4.41-4ubuntu3.9) ...
Selecting previously unselected package apache2-utils.
Preparing to unpack .../7-apache2-utils_2.4.41-4ubuntu3.9_amd64.deb ...
Unpacking apache2-utils (2.4.41-4ubuntu3.9) ...
Selecting previously unselected package apache2.
Preparing to unpack .../8-apache2_2.4.41-4ubuntu3.9_amd64.deb ...
Unpacking apache2 (2.4.41-4ubuntu3.9) ...
Selecting previously unselected package ssl-cert.
Preparing to unpack .../9-ssl-cert_1.0.39_all.deb ...
Unpacking ssl-cert (1.0.39) ...
Setting up libapr1:amd64 (1.6.5-1ubuntu1) ...
Setting up libjansson4:amd64 (2.12-1build1) ...
Setting up ssl-cert (1.0.39) ...
Setting up apache2-data (2.4.41-4ubuntu3.9) ...
Setting up libaprutil1:amd64 (1.6.1-4ubuntu2) ...
Setting up libaprutil1-ldap:amd64 (1.6.1-4ubuntu2) ...
Setting up libaprutil1-dbd-sqlite3:amd64 (1.6.1-4ubuntu2) ...
Setting up apache2-utils (2.4.41-4ubuntu3.9) ...
Setting up apache2-bin (2.4.41-4ubuntu3.9) ...
Setting up apache2 (2.4.41-4ubuntu3.9) ...
Enabling module mpm_event.
Enabling module authz_core.
Enabling module authz_host.
Enabling module authn_core.
Enabling module auth_basic.
Enabling module access_compat.
Enabling module authn_file.
Enabling module authz_user.
Enabling module alias.
Enabling module dir.
Enabling module autoindex.
Enabling module env.
Enabling module mime.
Enabling module negotiation.
Enabling module setenvif.
Enabling module filter.
Enabling module deflate.
Enabling module status.
Enabling module reqtimeout.
Enabling conf charset.
Enabling conf localized-error-pages.
Enabling conf other-vhosts-access-log.
Enabling conf security.
Enabling conf serve-cgi-bin.
Enabling site 000-default.
Created symlink /etc/systemd/system/multi-user.target.wants/apache2.service → /lib/systemd/system/apache2.service.
Created symlink /etc/systemd/system/multi-user.target.wants/apache-htcacheclean.service → /lib/systemd/system/apache-htcacheclean.service.
Processing triggers for ufw (0.36-6ubuntu1) ...
Processing triggers for systemd (245.4-4ubuntu3.13) ...
Processing triggers for man-db (2.9.1-1) ...
Processing triggers for libc-bin (2.31-0ubuntu9.2) ...
  ```
</details>

<details>
  <summary>Включаем модуль `ssl` и перезагружаем демон `apache2`</summary>

  ```
vagrant@u20web:~$ sudo a2enmod ssl
Considering dependency setenvif for ssl:
Module setenvif already enabled
Considering dependency mime for ssl:
Module mime already enabled
Considering dependency socache_shmcb for ssl:
Enabling module socache_shmcb.
Enabling module ssl.
See /usr/share/doc/apache2/README.Debian.gz on how to configure SSL and create self-signed certificates.
To activate the new configuration, you need to run:
  systemctl restart apache2
vagrant@u20web:~$ sudo systemctl restart apache2
  ```
</details>

<details>
  <summary>Генерируем самоподписанный сертификат</summary>

  ```
vagrant@u20web:~$ sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 \-keyout /etc/ssl/private/apache-selfsigned.key \-out /etc/ssl/certs/apache-selfsigned.crt \-subj "/C=RU/ST=FE/L=Khabarovsk/O=RudenkoMA/OU=Org/CN=u20web.home"
Generating a RSA private key
................+++++
.......+++++
writing new private key to '/etc/ssl/private/apache-selfsigned.key'
-----
  ```
</details>

<details>
  <summary>Создаем файл конфигруации сайта</summary>

  ```
vagrant@u20web:~$ sudo vim /etc/apache2/sites-available/u20web.conf
vagrant@u20web:~$ cat /etc/apache2/sites-available/u20web.conf
<VirtualHost *:443>
        ServerName u20web.home
        DocumentRoot /var/www/u20web
        SSLEngine on
        SSLCertificateFile /etc/ssl/certs/apache-selfsigned.crt
        SSLCertificateKeyFile /etc/ssl/private/apache-selfsigned.key
</VirtualHost>
  ```
</details>

<details>
  <summary>Создаем директорию сайта и индексный файл</summary>

  ```
vagrant@u20web:~$ sudo mkdir /var/www/u20web
vagrant@u20web:~$ sudo vim /var/www/u20web/index.html
vagrant@u20web:~$ cat /var/www/u20web/index.html     
<!DOCTYPE html>
<html>
<head>
  <title>Homework 3.9</title>
</head>
<body>
  <h1>It works!</h1>
  <p>This page was served with Apache2 server over SSL.</p>
</body>
</html>
  ```
</details>

<details>
  <summary>Меняем права, включаем конфигурацию сайта, проверяем и перезагружаем конфигурацию `apache2`</summary>
  
  ```
vagrant@u20web:~$ sudo chown -R www-data:www-data /var/www/u20web/
vagrant@u20web:~$ sudo a2ensite u20web
Enabling site u20web.
To activate the new configuration, you need to run:
  systemctl reload apache2
vagrant@u20web:~$ sudo apache2ctl configtest 
Syntax OK
vagrant@u20web:~$ sudo systemctl reload apache2
  ```
</details>

Проверяем доступность сайта (предварительно, необходимо прописать наш сайт в файле `hosts` или создать `A` запись в `DNS` сервере).
![](https://github.com/rudenko-ma/netology.homeworks/blob/main/03-sysadmin-09-security/img/q3.png)

## 4. Проверьте на TLS уязвимости произвольный сайт в интернете (кроме сайтов МВД, ФСБ, МинОбр, НацБанк, РосКосмос, РосАтом, РосНАНО и любых госкомпаний, объектов КИИ, ВПК ... и тому подобное).

Проверка обнаружила потенциальные уязвимости.
![](https://github.com/rudenko-ma/netology.homeworks/blob/main/03-sysadmin-09-security/img/q4.png)

## 5. Установите на Ubuntu ssh сервер, сгенерируйте новый приватный ключ. Скопируйте свой публичный ключ на другой сервер. Подключитесь к серверу по SSH-ключу.
 
Доступ по ключу получен.
![](https://github.com/rudenko-ma/netology.homeworks/blob/main/03-sysadmin-09-security/img/q5.png)

## 6. Переименуйте файлы ключей из задания 5. Настройте файл конфигурации SSH клиента, так чтобы вход на удаленный сервер осуществлялся по имени сервера.

Вход по имени настроен.
![](https://github.com/rudenko-ma/netology.homeworks/blob/main/03-sysadmin-09-security/img/q6.png)

## 7. Соберите дамп трафика утилитой tcpdump в формате pcap, 100 пакетов. Откройте файл pcap в Wireshark.

Собрали трафик на удаленном веб сервере, скачали `pcap` файл, открыли в `Wireshark`.
![](https://github.com/rudenko-ma/netology.homeworks/blob/main/03-sysadmin-09-security/img/q7.png)

## 8*. Просканируйте хост scanme.nmap.org. Какие сервисы запущены?

На сервере `scanme.nmap.org` запущены следующие сервисы:
- 22/tcp - OpenSSH 6.6.1p1
- 80/tcp - Apache httpd 2.4.7
- 5555/tcp - freeciv (игра по мотивам серии Сида Мейера Civilization)
- 9929/tcp - Nping echo
- 31337/tcp - tcpwrapped (какой-то веб сервис, к которому нет доступа с нашего хоста)

```
nmap -T4 -A scanme.nmap.org
Starting Nmap 7.80 ( https://nmap.org ) at 2022-02-16 15:19 +10
Nmap scan report for scanme.nmap.org (45.33.32.156)
Host is up (0.28s latency).
Other addresses for scanme.nmap.org (not scanned): 2600:3c01::f03c:91ff:fe18:bb2f
Not shown: 995 closed ports
PORT      STATE    SERVICE    VERSION
22/tcp    open     ssh        OpenSSH 6.6.1p1 Ubuntu 2ubuntu2.13 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   1024 ac:00:a0:1a:82:ff:cc:55:99:dc:67:2b:34:97:6b:75 (DSA)
|   2048 20:3d:2d:44:62:2a:b0:5a:9d:b5:b3:05:14:c2:a6:b2 (RSA)
|   256 96:02:bb:5e:57:54:1c:4e:45:2f:56:4c:4a:24:b2:57 (ECDSA)
|_  256 33:fa:91:0f:e0:e1:7b:1f:6d:05:a2:b0:f1:54:41:56 (ED25519)
80/tcp    open     http       Apache httpd 2.4.7 ((Ubuntu))
|_http-server-header: Apache/2.4.7 (Ubuntu)
|_http-title: Go ahead and ScanMe!
5555/tcp  filtered freeciv
9929/tcp  open     nping-echo Nping echo
31337/tcp open     tcpwrapped
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 26.66 seconds
```

## 9*. Установите и настройте фаервол ufw на web-сервер из задания 3. Откройте доступ снаружи только к портам 22,80,443

Установили `ufw`, добавили правила доступа к указанным портам, включили файерволл.

```
vagrant@u20web:~$ sudo apt install ufw
Reading package lists... Done
Building dependency tree       
Reading state information... Done
ufw is already the newest version (0.36-6ubuntu1).
0 upgraded, 0 newly installed, 0 to remove and 62 not upgraded.
vagrant@u20web:~$ sudo ufw allow 22/tcp
Rules updated
Rules updated (v6)
vagrant@u20web:~$ sudo ufw allow 80/tcp
Rules updated
Rules updated (v6)
vagrant@u20web:~$ sudo ufw allow 443/tcp
Rules updated
Rules updated (v6)
vagrant@u20web:~$ sudo ufw enable
Command may disrupt existing ssh connections. Proceed with operation (y|n)? y
Firewall is active and enabled on system startup
vagrant@u20web:~$ sudo ufw status verbose
Status: active
Logging: on (low)
Default: deny (incoming), allow (outgoing), disabled (routed)
New profiles: skip

To                         Action      From
--                         ------      ----
22/tcp                     ALLOW IN    Anywhere                  
80/tcp                     ALLOW IN    Anywhere                  
443/tcp                    ALLOW IN    Anywhere                  
22/tcp (v6)                ALLOW IN    Anywhere (v6)             
80/tcp (v6)                ALLOW IN    Anywhere (v6)             
443/tcp (v6)               ALLOW IN    Anywhere (v6) 
```

