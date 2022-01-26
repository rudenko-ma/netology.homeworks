# Домашнее задание к занятию "3.6. Компьютерные сети, лекция 1"

## 1. Работа c HTTP через телнет.
- Подключитесь утилитой телнет к сайту stackoverflow.com
`telnet stackoverflow.com 80`
- отправьте HTTP запрос
```bash
GET /questions HTTP/1.0
HOST: stackoverflow.com
[press enter]
[press enter]
```
- В ответе укажите полученный HTTP код, что он означает?

**Ответ:**

Первая строка ответа `HTTP/1.1 301 Moved Permanently` содержит код 301 сообщающий браузеру что сайт окончательно переехал. Получив этот код браузер автоматически перейдет по адресу указанному в заголовке `location`.

В данном случае, web-сервер настроен так, чтобы используя данный код перенаправлять посетителей сайта на защищенный протокол `HTTPS`.

![](https://github.com/rudenko-ma/netology.homeworks/blob/main/03-sysadmin-06-net/img/q1.png)

## 2. Повторите задание 1 в браузере, используя консоль разработчика F12.
- откройте вкладку `Network`
- отправьте запрос http://stackoverflow.com
- найдите первый ответ HTTP сервера, откройте вкладку `Headers`
- укажите в ответе полученный HTTP код.
- проверьте время загрузки страницы, какой запрос обрабатывался дольше всего?
- приложите скриншот консоли браузера в ответ.

**Ответ:**

Первый полученный ответ содержит код: `Status Code: 307 Internal Redirect`.

![](https://github.com/rudenko-ma/netology.homeworks/blob/main/03-sysadmin-06-net/img/q2_1.png)

Дольше всего обрабатывался второй запрос (произошедший в следствие редиректа), в ответ на который сервер сформировал исходный код страницы.

![](https://github.com/rudenko-ma/netology.homeworks/blob/main/03-sysadmin-06-net/img/q2_2.png)

## 3. Какой IP адрес у вас в интернете?

Мой IP: `92.37.216.164`

![](https://github.com/rudenko-ma/netology.homeworks/blob/main/03-sysadmin-06-net/img/q3.png)

## 4. Какому провайдеру принадлежит ваш IP адрес? Какой автономной системе AS? Воспользуйтесь утилитой `whois`

Мой IP адрес принадлежит провайдеру `Rostelecom`, автономной системе `AS12389`.

```
# whois 92.37.216.164
% This is the RIPE Database query service.
% The objects are in RPSL format.
%
% The RIPE Database is subject to Terms and Conditions.
% See http://www.ripe.net/db/support/db-terms-conditions.pdf

% Note: this output has been filtered.
%       To receive output for a database update, use the "-B" flag.

% Information related to '92.37.216.0 - 92.37.217.255'

% Abuse contact for '92.37.216.0 - 92.37.217.255' is 'abuse@rt.ru'

inetnum:        92.37.216.0 - 92.37.217.255
netname:        KHT-XDSL
descr:          PPPoE xDSL links in Komsomolsk-at-Amur town, ATS-530 node
country:        ru
admin-c:        kv422-ripe
admin-c:        MMS422-ripe
tech-c:         kv422-ripe
tech-c:         MMS422-ripe
status:         ASSIGNED PA
mnt-by:         MNT-KHTDSV-NOC
mnt-lower:      MNT-KHTDSV-NOC
created:        2008-11-18T09:02:12Z
last-modified:  2008-11-18T09:02:12Z
source:         RIPE # Filtered

person:         Konstantyn Vasenyn
address:        The Khabarovsk Telephone - Telegraph station
address:        58, Karl Marks st.
address:        RU-680000 Khabarovsk
address:        Russia
mnt-by:         MNT-KV422-RIPE
phone:          +7 421 2323794
fax-no:         +7 421 2325206
nic-hdl:        KV422-RIPE
created:        1970-01-01T00:00:00Z
last-modified:  2006-11-06T02:28:34Z
source:         RIPE # Filtered

person:         Maxim Medvedev
address:        The Khabarovsk Telephone - Telegraph station
address:        58, Karl Marks st.
address:        RU-680000 Khabarovsk
address:        Russia
mnt-by:         MNT-MMS422-RIPE
phone:          +7 421 2322391
nic-hdl:        MMS422-RIPE
created:        2005-12-27T01:50:53Z
last-modified:  2006-07-21T00:29:44Z
source:         RIPE # Filtered

% Information related to '92.37.216.0/21AS12389'

route:          92.37.216.0/21
descr:          Rostelecom networks
origin:         AS12389
mnt-by:         ROSTELECOM-MNT
created:        2018-10-18T15:22:49Z
last-modified:  2018-10-18T15:22:49Z
source:         RIPE # Filtered

% This query was served by the RIPE Database Query Service version 1.102.2 (ANGUS)
```

## 5. Через какие сети проходит пакет, отправленный с вашего компьютера на адрес 8.8.8.8? Через какие AS? Воспользуйтесь утилитой `traceroute`

```
# traceroute -An 8.8.8.8
traceroute to 8.8.8.8 (8.8.8.8), 30 hops max, 60 byte packets
 1  192.168.88.1 [*]  0.433 ms  0.474 ms  0.528 ms
 2  10.251.14.151 [*]  4.759 ms 10.251.14.149 [*]  4.956 ms 10.251.14.151 [*]  5.029 ms
 3  10.251.14.150 [*]  1.476 ms 10.251.14.148 [*]  1.897 ms  2.064 ms
 4  87.226.181.89 [AS12389]  101.187 ms  96.865 ms  97.688 ms
 5  5.143.253.105 [AS12389]  101.461 ms 74.125.51.172 [AS15169]  101.528 ms 5.143.253.245 [AS12389]  104.786 ms
 6  108.170.250.66 [AS15169]  102.000 ms * *
 7  142.251.49.24 [AS15169]  112.630 ms 142.251.49.78 [AS15169]  116.913 ms *
 8  172.253.65.159 [AS15169]  130.199 ms 172.253.66.108 [AS15169]  112.629 ms  112.180 ms
 9  142.250.238.181 [AS15169]  113.565 ms 74.125.253.147 [AS15169]  110.709 ms 209.85.254.179 [AS15169]  112.392 ms
10  * * *
11  * * *
12  * * *
13  * * *
14  * * *
15  * * *
16  * * *
17  * * *
18  * * 8.8.8.8 [AS15169]  107.994 ms
```

## 6. Повторите задание 5 в утилите `mtr`. На каком участке наибольшая задержка - delay?

Наибольшая задержка наблюдается на участке **№9** `AS15169  216.239.46.139`. За 10 циклов проверки она составила в среднем `124.6`мс.

```
# mtr -znr -c 10 8.8.8.8 | grep AS | sort -gr -k 7
  9. AS15169  216.239.46.139       0.0%    10  113.2 124.6 112.7 171.1  24.0
  7. AS15169  142.251.49.158      40.0%    10  116.3 116.6 116.2 118.1   0.7
  8. AS15169  74.125.253.94        0.0%    10  112.3 112.3 112.0 112.9   0.3
 19. AS15169  8.8.8.8             30.0%    10  111.4 111.4 111.2 111.8   0.2
  6. AS15169  108.170.250.113     60.0%    10  104.3 104.3 104.3 104.3   0.0
  4. AS12389  87.226.181.89        0.0%    10  100.8 101.5 100.7 106.6   1.8
  5. AS15169  74.125.51.172        0.0%    10   99.9 100.0  99.9 100.4   0.2
  2. AS???    10.251.14.151        0.0%    10    9.0  12.6   1.6  26.2   6.8
  3. AS???    10.251.14.150        0.0%    10    2.9   2.5   0.9   9.9   2.8
  1. AS???    192.168.88.1         0.0%    10    0.5   0.4   0.3   0.5   0.0
 18. AS???    ???                 100.0    10    0.0   0.0   0.0   0.0   0.0
 17. AS???    ???                 100.0    10    0.0   0.0   0.0   0.0   0.0
 16. AS???    ???                 100.0    10    0.0   0.0   0.0   0.0   0.0
 15. AS???    ???                 100.0    10    0.0   0.0   0.0   0.0   0.0
 14. AS???    ???                 100.0    10    0.0   0.0   0.0   0.0   0.0
 13. AS???    ???                 100.0    10    0.0   0.0   0.0   0.0   0.0
 12. AS???    ???                 100.0    10    0.0   0.0   0.0   0.0   0.0
 11. AS???    ???                 100.0    10    0.0   0.0   0.0   0.0   0.0
 10. AS???    ???                 100.0    10    0.0   0.0   0.0   0.0   0.0
     AS???    10.251.14.149
```

## 7. Какие DNS сервера отвечают за доменное имя dns.google? Какие A записи? воспользуйтесь утилитой `dig`

За доменное имя `dns.google` отвечают четыре DNS сервера:

```
# dig NS dns.google

; <<>> DiG 9.16.1-Ubuntu <<>> NS dns.google
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 34069
;; flags: qr rd ra; QUERY: 1, ANSWER: 4, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 65494
;; QUESTION SECTION:
;dns.google.                    IN      NS

;; ANSWER SECTION:
dns.google.             17214   IN      NS      ns2.zdns.google.
dns.google.             17214   IN      NS      ns3.zdns.google.
dns.google.             17214   IN      NS      ns1.zdns.google.
dns.google.             17214   IN      NS      ns4.zdns.google.

;; Query time: 111 msec
;; SERVER: 127.0.0.53#53(127.0.0.53)
;; WHEN: Ср янв 26 17:41:08 +10 2022
;; MSG SIZE  rcvd: 116
```

У данного доменного имени есть две A записи:

```
# dig dns.google

; <<>> DiG 9.16.1-Ubuntu <<>> dns.google
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 13000
;; flags: qr rd ra; QUERY: 1, ANSWER: 2, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 65494
;; QUESTION SECTION:
;dns.google.                    IN      A

;; ANSWER SECTION:
dns.google.             542     IN      A       8.8.4.4
dns.google.             542     IN      A       8.8.8.8

;; Query time: 115 msec
;; SERVER: 127.0.0.53#53(127.0.0.53)
;; WHEN: Ср янв 26 17:40:59 +10 2022
;; MSG SIZE  rcvd: 71
```

## 8. Проверьте PTR записи для IP адресов из задания 7. Какое доменное имя привязано к IP? воспользуйтесь утилитой `dig`


