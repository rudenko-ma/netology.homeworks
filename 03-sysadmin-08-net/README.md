# Домашнее задание к занятию "3.8. Компьютерные сети, лекция 3"

## 1. Подключитесь к публичному маршрутизатору в интернет. Найдите маршрут к вашему публичному IP

<details>
  <summary>Сеанс `telnet` с публичным маршрутизатором:</summary>

  ```
# telnet route-views.routeviews.org
Trying 128.223.51.103...
Connected to route-views.routeviews.org.
Escape character is '^]'.
C
**********************************************************************

                    RouteViews BGP Route Viewer
                    route-views.routeviews.org

 route views data is archived on http://archive.routeviews.org

 This hardware is part of a grant by the NSF.
 Please contact help@routeviews.org if you have questions, or
 if you wish to contribute your view.

 This router has views of full routing tables from several ASes.
 The list of peers is located at http://www.routeviews.org/peers
 in route-views.oregon-ix.net.txt

 NOTE: The hardware was upgraded in August 2014.  If you are seeing
 the error message, "no default Kerberos realm", you may want to
 in Mac OS X add "default unset autologin" to your ~/.telnetrc

 To login, use the username "rviews".

 **********************************************************************

User Access Verification

Username: rviews
route-views>show ip route 92.37.237.169   
Routing entry for 92.37.232.0/21
  Known via "bgp 6447", distance 20, metric 0
  Tag 3356, type external
  Last update from 4.68.4.46 1w3d ago
  Routing Descriptor Blocks:
  * 4.68.4.46, from 4.68.4.46, 1w3d ago
      Route metric is 0, traffic share count is 1
      AS Hops 2
      Route tag 3356
      MPLS label: none
route-views>show bgp 92.37.237.169
BGP routing table entry for 92.37.232.0/21, version 273876541
Paths: (23 available, best #15, table default)
  Not advertised to any peer
  Refresh Epoch 1
  20912 3257 3356 12389
    212.66.96.126 from 212.66.96.126 (212.66.96.126)
      Origin IGP, localpref 100, valid, external
      Community: 3257:8070 3257:30515 3257:50001 3257:53900 3257:53902 20912:65004
      path 7FE103EDEF08 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  3303 12389
    217.192.89.50 from 217.192.89.50 (138.187.128.158)
      Origin IGP, localpref 100, valid, external
      Community: 3303:1004 3303:1006 3303:1030 3303:3056 34584:27000
      path 7FE0E1B46F78 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  101 3491 12389
    209.124.176.223 from 209.124.176.223 (209.124.176.223)
      Origin IGP, localpref 100, valid, external
      Community: 101:20300 101:22100 3491:400 3491:415 3491:9001 3491:9080 3491:9081 3491:9087 3491:62210 3491:62220 34584:27000
      path 7FE133D49FC0 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  701 1273 12389
    137.39.3.55 from 137.39.3.55 (137.39.3.55)
      Origin IGP, localpref 100, valid, external
      path 7FE11C88BAF0 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  3333 1103 12389
    193.0.0.56 from 193.0.0.56 (193.0.0.56)
      Origin IGP, localpref 100, valid, external
      Community: 34584:27000
      path 7FE04307E9A0 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  7018 1299 12389
    12.0.1.63 from 12.0.1.63 (12.0.1.63)
      Origin IGP, localpref 100, valid, external
      Community: 7018:5000 7018:37232
      path 7FE14861B4D0 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  57866 3356 12389
    37.139.139.17 from 37.139.139.17 (37.139.139.17)
      Origin IGP, metric 0, localpref 100, valid, external
      Community: 3356:2 3356:22 3356:100 3356:123 3356:501 3356:901 3356:2065 34584:27000
      path 7FE0D5514230 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  3561 3910 3356 12389
    206.24.210.80 from 206.24.210.80 (206.24.210.80)
      Origin IGP, localpref 100, valid, external
      path 7FE12559EDD0 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  1351 6939 12389
    132.198.255.253 from 132.198.255.253 (132.198.255.253)
      Origin IGP, localpref 100, valid, external
      path 7FE15E1F7460 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 2
  8283 1299 12389
    94.142.247.3 from 94.142.247.3 (94.142.247.3)
      Origin IGP, metric 0, localpref 100, valid, external
      Community: 1299:30000 8283:1 8283:101 8283:103
      unknown transitive attribute: flag 0xE0 type 0x20 length 0x24
        value 0000 205B 0000 0000 0000 0001 0000 205B
              0000 0005 0000 0001 0000 205B 0000 0005
              0000 0003 
      path 7FE033507E30 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  852 3491 12389
    154.11.12.212 from 154.11.12.212 (96.1.209.43)
      Origin IGP, metric 0, localpref 100, valid, external
      path 7FE130962218 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  20130 6939 12389
    140.192.8.16 from 140.192.8.16 (140.192.8.16)
      Origin IGP, localpref 100, valid, external
      path 7FE0F4ED0130 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  4901 6079 3356 12389
    162.250.137.254 from 162.250.137.254 (162.250.137.254)
      Origin IGP, localpref 100, valid, external
      Community: 65000:10100 65000:10300 65000:10400
      path 7FE175769968 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  53767 14315 6453 6453 3356 12389
    162.251.163.2 from 162.251.163.2 (162.251.162.3)
      Origin IGP, localpref 100, valid, external
      Community: 14315:5000 53767:5000
      path 7FE0E71AB188 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  3356 12389
    4.68.4.46 from 4.68.4.46 (4.69.184.201)
      Origin IGP, metric 0, localpref 100, valid, external, best
      Community: 3356:2 3356:22 3356:100 3356:123 3356:501 3356:901 3356:2065 34584:27000
      path 7FE03111CAC8 RPKI State valid
      rx pathid: 0, tx pathid: 0x0
  Refresh Epoch 1
  3549 3356 12389
    208.51.134.254 from 208.51.134.254 (67.16.168.191)
      Origin IGP, metric 0, localpref 100, valid, external
      Community: 3356:2 3356:22 3356:100 3356:123 3356:501 3356:901 3356:2065 3549:2581 3549:30840 34584:27000
      path 7FE155CDF228 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 2
  2497 12389
    202.232.0.2 from 202.232.0.2 (58.138.96.254)
      Origin IGP, localpref 100, valid, external
      path 7FE11EB113B8 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  7660 2516 12389
    203.181.248.168 from 203.181.248.168 (203.181.248.168)
      Origin IGP, localpref 100, valid, external
      Community: 2516:1050 7660:9001
      path 7FE1403160B0 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  49788 12552 12389
    91.218.184.60 from 91.218.184.60 (91.218.184.60)
      Origin IGP, localpref 100, valid, external
      Community: 12552:12000 12552:12100 12552:12101 12552:22000
      Extended Community: 0x43:100:1
      path 7FE18C262D28 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  1221 4637 12389
    203.62.252.83 from 203.62.252.83 (203.62.252.83)
      Origin IGP, localpref 100, valid, external
      path 7FE147BA77D8 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  3257 3356 12389
    89.149.178.10 from 89.149.178.10 (213.200.83.26)
      Origin IGP, metric 10, localpref 100, valid, external
      Community: 3257:8794 3257:30043 3257:50001 3257:54900 3257:54901
      path 7FE03DC53D98 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  19214 3257 3356 12389
    208.74.64.40 from 208.74.64.40 (208.74.64.40)
      Origin IGP, localpref 100, valid, external
      Community: 3257:8108 3257:30048 3257:50002 3257:51200 3257:51203
      path 7FE16ABBBE58 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  6939 12389
    64.71.137.241 from 64.71.137.241 (216.218.252.164)
      Origin IGP, localpref 100, valid, external
      path 7FE15C2048A8 RPKI State valid
      rx pathid: 0, tx pathid: 0
route-views>
  ```
</details>

## 2. Создайте dummy0 интерфейс в Ubuntu. Добавьте несколько статических маршрутов. Проверьте таблицу маршрутизации.

Создаем интерфейс dummpy0:
```
vagrant@ubuntu2004:~$ sudo vim /etc/network/interfaces
# ifupdown has been replaced by netplan(5) on this system.  See
# /etc/netplan for current configuration.
# To re-enable ifupdown on this system, you can run:
#    sudo apt install ifupdown

# создаем интерфейс
auto dummy0
iface dummy0 inet static
        address 172.16.0.100/32
        pre-up ip link add dummy0 type dummy
        post-down ip link del dummy0

        # добавляем статические маршруты
        post-up ip route add 172.16.100.0/24 dev dummy0
        post-up ip route add 172.16.200.0/24 dev dummy0

allow-hotplug eth0
iface eth0 inet dhcp
```

Добавляем маршруты и проверяем таблицу маршрутизации:
```
vagrant@ubuntu2004:~$ ip r
default via 192.168.121.1 dev eth0 
default via 192.168.121.1 dev eth0 proto dhcp src 192.168.121.172 metric 100 
172.16.100.0/24 dev dummy0 scope link 
172.16.200.0/24 dev dummy0 scope link 
192.168.121.0/24 dev eth0 proto kernel scope link src 192.168.121.172 
192.168.121.1 dev eth0 proto dhcp scope link src 192.168.121.172 metric 100
```

## 3. Проверьте открытые TCP порты в Ubuntu, какие протоколы и приложения используют эти порты? Приведите несколько примеров.

На сервере открыты следующие TCP порты:
- 22 - сервер SSH (протокол `SSH`)
- 53 - DNS резолвер (протокол `DNS`)
- 8125 - порт сервера мониторинга `Netdata` (протокол `StatsD`)
- 19999 - интерфейс сервера мониторинга `Netdata` (протокол `HTTP`)
- 9101 - интрефейс агента `node_exporter` (протокол `HTTP`)

```
vagrant@ubuntu2004:~$ sudo ss -tnlp
State  Recv-Q Send-Q Local Address:Port  Peer Address:Port Process
LISTEN 0      4096   127.0.0.53%lo:53         0.0.0.0:*     users:(("systemd-resolve",pid=1073,fd=13))
LISTEN 0      128          0.0.0.0:22         0.0.0.0:*     users:(("sshd",pid=712,fd=3))
LISTEN 0      4096       127.0.0.1:8125       0.0.0.0:*     users:(("netdata",pid=674,fd=44))
LISTEN 0      4096         0.0.0.0:19999      0.0.0.0:*     users:(("netdata",pid=674,fd=4))
LISTEN 0      4096               *:9101             *:*     users:(("node_exporter",pid=675,fd=3))
LISTEN 0      128             [::]:22            [::]:*     users:(("sshd",pid=712,fd=4)) 
```

## 4. Проверьте используемые UDP сокеты в Ubuntu, какие протоколы и приложения используют эти порты?

На сервере открыты следующие UDP порты:
- 53 - DNS резолвер (протокол `DNS`)
- 68 - DHCP клиент (протокол `DHCP`)
- 8125 - порты сервера мониторинга `Netdata` (протокол `StatsD`)

```
vagrant@ubuntu2004:~$ sudo ss -unlp
State       Recv-Q      Send-Q                   Local Address:Port             Peer Address:Port      Process
UNCONN      0           0                            127.0.0.1:8125                  0.0.0.0:*          users:(("netdata",pid=674,fd=43))
UNCONN      0           0                        127.0.0.53%lo:53                    0.0.0.0:*          users:(("systemd-resolve",pid=1073,fd=12))
UNCONN      0           0                 192.168.121.172%eth0:68                    0.0.0.0:*          users:(("systemd-network",pid=363,fd=20))
UNCONN      0           0                              0.0.0.0:68                    0.0.0.0:*          users:(("dhclient",pid=530,fd=9))
```

## 5. Используя diagrams.net, создайте L3 диаграмму вашей домашней сети или любой другой сети, с которой вы работали.

Диаграмма моей [домашней сети](diagrams.net):

![](https://github.com/rudenko-ma/netology.homeworks/blob/main/03-sysadmin-08-net/img/q5.png)
