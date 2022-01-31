# Домашнее задание к занятию "3.7. Компьютерные сети, лекция 2"

## 1. Проверьте список доступных сетевых интерфейсов на вашем компьютере. Какие команды есть для этого в Linux и в Windows?

В Windows используется утилита `ipconfig`:
```
C:\Users\ruden> ipconfig /all

Настройка протокола IP для Windows

   Имя компьютера  . . . . . . . . . : pc-z
   Основной DNS-суффикс  . . . . . . :
   Тип узла. . . . . . . . . . . . . : Гибридный
   IP-маршрутизация включена . . . . : Нет
   WINS-прокси включен . . . . . . . : Нет

Адаптер Ethernet Ethernet 3:

   DNS-суффикс подключения . . . . . :
   Описание. . . . . . . . . . . . . : VirtualBox Host-Only Ethernet Adapter
   Физический адрес. . . . . . . . . : 0A-00-27-00-00-15
   DHCP включен. . . . . . . . . . . : Нет
   Автонастройка включена. . . . . . : Да
   Локальный IPv6-адрес канала . . . : fe80::1584:ad86:88d0:7e7a%21(Основной)
   IPv4-адрес. . . . . . . . . . . . : 192.168.56.1(Основной)
   Маска подсети . . . . . . . . . . : 255.255.255.0
   Основной шлюз. . . . . . . . . :
   IAID DHCPv6 . . . . . . . . . . . : 705298471
   DUID клиента DHCPv6 . . . . . . . : 00-01-00-01-28-68-97-03-2C-F0-5D-E0-A4-27
   NetBios через TCP/IP. . . . . . . . : Включен

Адаптер Ethernet vEthernet (External Switch):

   DNS-суффикс подключения . . . . . :
   Описание. . . . . . . . . . . . . : Hyper-V Virtual Ethernet Adapter #2
   Физический адрес. . . . . . . . . : 2C-F0-5D-E0-A4-27
   DHCP включен. . . . . . . . . . . : Да
   Автонастройка включена. . . . . . : Да
   Локальный IPv6-адрес канала . . . : fe80::bdf1:f0c1:9da3:7ca0%9(Основной)
   IPv4-адрес. . . . . . . . . . . . : 192.168.88.10(Основной)
   Маска подсети . . . . . . . . . . : 255.255.255.0
   Аренда получена. . . . . . . . . . : 29 января 2022 г. 2:31:44
   Срок аренды истекает. . . . . . . . . . : 31 января 2022 г. 23:16:49
   Основной шлюз. . . . . . . . . : 192.168.88.1
   DHCP-сервер. . . . . . . . . . . : 192.168.88.1
   IAID DHCPv6 . . . . . . . . . . . : 489484381
   DUID клиента DHCPv6 . . . . . . . : 00-01-00-01-28-68-97-03-2C-F0-5D-E0-A4-27
   DNS-серверы. . . . . . . . . . . : 192.168.88.1
                                       194.85.113.243
                                       212.122.1.2
   NetBios через TCP/IP. . . . . . . . : Включен

Адаптер Ethernet Сетевое подключение Bluetooth:

   Состояние среды. . . . . . . . : Среда передачи недоступна.
   DNS-суффикс подключения . . . . . :
   Описание. . . . . . . . . . . . . : Bluetooth Device (Personal Area Network)
   Физический адрес. . . . . . . . . : 00-E0-3C-A4-39-03
   DHCP включен. . . . . . . . . . . : Да
   Автонастройка включена. . . . . . : Да

Адаптер Ethernet vEthernet (Default Switch):

   DNS-суффикс подключения . . . . . :
   Описание. . . . . . . . . . . . . : Hyper-V Virtual Ethernet Adapter
   Физический адрес. . . . . . . . . : 00-15-5D-40-92-06
   DHCP включен. . . . . . . . . . . : Нет
   Автонастройка включена. . . . . . : Да
   Локальный IPv6-адрес канала . . . : fe80::b4cb:4da8:9bd1:b8b4%27(Основной)
   IPv4-адрес. . . . . . . . . . . . : 172.24.240.1(Основной)
   Маска подсети . . . . . . . . . . : 255.255.240.0
   Основной шлюз. . . . . . . . . :
   IAID DHCPv6 . . . . . . . . . . . : 452990301
   DUID клиента DHCPv6 . . . . . . . : 00-01-00-01-28-68-97-03-2C-F0-5D-E0-A4-27
   NetBios через TCP/IP. . . . . . . . : Включен
```

В Linux актуальной считается утилита `ip` входящая в состав `iproute2`:
```
# ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
    link/ether 00:15:5d:58:0a:06 brd ff:ff:ff:ff:ff:ff
    inet 192.168.88.100/24 brd 192.168.88.255 scope global dynamic noprefixroute eth0
       valid_lft 342sec preferred_lft 342sec
    inet6 fe80::d41d:96e2:8ff7:f33d/64 scope link noprefixroute 
       valid_lft forever preferred_lft forever
3: virbr0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default qlen 1000
    link/ether 52:54:00:42:7b:c6 brd ff:ff:ff:ff:ff:ff
    inet 192.168.122.1/24 brd 192.168.122.255 scope global virbr0
       valid_lft forever preferred_lft forever
4: virbr0-nic: <BROADCAST,MULTICAST> mtu 1500 qdisc fq_codel master virbr0 state DOWN group default qlen 1000
    link/ether 52:54:00:42:7b:c6 brd ff:ff:ff:ff:ff:ff
5: docker0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default 
    link/ether 02:42:7c:4e:7c:e8 brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.1/16 brd 172.17.255.255 scope global docker0
       valid_lft forever preferred_lft forever
```

## 2. Какой протокол используется для распознавания соседа по сетевому интерфейсу? Какой пакет и команды есть в Linux для этого?



## 3. Какая технология используется для разделения L2 коммутатора на несколько виртуальных сетей? Какой пакет и команды есть в Linux для этого? Приведите пример конфига.



## 4. Какие типы агрегации интерфейсов есть в Linux? Какие опции есть для балансировки нагрузки? Приведите пример конфига.



## 5. Сколько IP адресов в сети с маской /29 ? Сколько /29 подсетей можно получить из сети с маской /24. Приведите несколько примеров /29 подсетей внутри сети 10.10.10.0/24.



## 6. Задача: вас попросили организовать стык между 2-мя организациями. Диапазоны 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16 уже заняты. Из какой подсети допустимо взять частные IP адреса? Маску выберите из расчета максимум 40-50 хостов внутри подсети.



## 7. Как проверить ARP таблицу в Linux, Windows? Как очистить ARP кеш полностью? Как из ARP таблицы удалить только один нужный IP?


