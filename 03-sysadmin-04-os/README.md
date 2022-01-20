# Домашнее задание к занятию "3.4. Операционные системы, лекция 2"

## 1. На лекции мы познакомились с [node_exporter](https://github.com/prometheus/node_exporter/releases). В демонстрации его исполняемый файл запускался в background. Этого достаточно для демо, но не для настоящей production-системы, где процессы должны находиться под внешним управлением. Используя знания из лекции по systemd, создайте самостоятельно простой [unit-файл](https://www.freedesktop.org/software/systemd/man/systemd.service.html) для node_exporter:

Установим `node_exporter` в систему:
```
vagrant@ubuntu2004:~$ wget https://github.com/prometheus/node_exporter/releases/download/v1.3.1/node_exporter-1.3.1.linux-amd64.tar.gz
...
vagrant@ubuntu2004:~$ tar xvfz node_exporter-1.3.1.linux-amd64.tar.gz 
...
vagrant@ubuntu2004:~$ sudo cp -r node_exporter-1.3.1.linux-amd64 /usr/local/lib/node_exporter-1.3.1
...
vagrant@ubuntu2004:~$ sudo ln -s /usr/local/lib/node_exporter-1.3.1/node_exporter /usr/local/bin/node_exporter
```

Теперь созданим `unit-файл`:
```
vagrant@ubuntu2004:~$ sudo systemctl edit --force --full node_exporter.service
vagrant@ubuntu2004:~$ sudo systemctl cat node_exporter.service
# /etc/systemd/system/node_exporter.service
[Unit]
Description=Node Exporter
After=network-online.target

[Service]
Type=simple
EnvironmentFile=-/etc/default/node_exporter
ExecStart=/usr/local/bin/node_exporter $EXTRA_ARGS

[Install]
WantedBy=default.target
vagrant@ubuntu2004:~$ sudo systemctl status node_exporter.service
● node_exporter.service - Node Exporter
     Loaded: loaded (/etc/systemd/system/node_exporter.service; disabled; vendor preset: enabled)
     Active: inactive (dead)
```

Помещаем демон в автозагрузку:

```
vagrant@ubuntu2004:~$ sudo systemctl enable node_exporter.service 
Created symlink /etc/systemd/system/default.target.wants/node_exporter.service → /etc/systemd/system/node_exporter.service.
```

Проверим возможность добавления опций к запускаемому процессу через предусмотренный внешний файл(`EnvironmentFile`):
```
vagrant@ubuntu2004:~$ echo EXTRA_ARGS=--web.listen-address=:9101 | sudo tee /etc/default/node_exporter
ARGS=--my-extra-option=some-value
vagrant@ubuntu2004:~$ sudo systemctl restart node_exporter.service 
vagrant@ubuntu2004:~$ systemctl status node_exporter.service 
● node_exporter.service - Node Exporter
     Loaded: loaded (/etc/systemd/system/node_exporter.service; enabled; vendor preset: enabled)
     Active: active (running) since Wed 2022-01-19 07:10:19 UTC; 10s ago
   Main PID: 1066 (node_exporter)
      Tasks: 3 (limit: 1071)
     Memory: 2.2M
     CGroup: /system.slice/node_exporter.service
             └─1066 /usr/local/bin/node_exporter --web.listen-address=:9101

Jan 19 07:10:19 ubuntu2004 node_exporter[1066]: ts=2022-01-19T07:10:19.658Z caller=node_exporter.go:115 level=info collector=thermal_zone
Jan 19 07:10:19 ubuntu2004 node_exporter[1066]: ts=2022-01-19T07:10:19.658Z caller=node_exporter.go:115 level=info collector=time
Jan 19 07:10:19 ubuntu2004 node_exporter[1066]: ts=2022-01-19T07:10:19.658Z caller=node_exporter.go:115 level=info collector=timex
Jan 19 07:10:19 ubuntu2004 node_exporter[1066]: ts=2022-01-19T07:10:19.659Z caller=node_exporter.go:115 level=info collectorudp_queues
Jan 19 07:10:19 ubuntu2004 node_exporter[1066]: ts=2022-01-19T07:10:19.659Z caller=node_exporter.go:115 level=info collector=uname
Jan 19 07:10:19 ubuntu2004 node_exporter[1066]: ts=2022-01-19T07:10:19.659Z caller=node_exporter.go:115 level=info collector=vmstat
Jan 19 07:10:19 ubuntu2004 node_exporter[1066]: ts=2022-01-19T07:10:19.659Z caller=node_exporter.go:115 level=info collector=xfs
Jan 19 07:10:19 ubuntu2004 node_exporter[1066]: ts=2022-01-19T07:10:19.659Z caller=node_exporter.go:115 level=info collector=zfs
Jan 19 07:10:19 ubuntu2004 node_exporter[1066]: ts=2022-01-19T07:10:19.659Z caller=node_exporter.go:199 level=info msg="Listening on" address=:9101
Jan 19 07:10:19 ubuntu2004 node_exporter[1066]: ts=2022-01-19T07:10:19.660Z caller=tls_config.go:195 level=info msg="TLS is disabled." http2=false
vagrant@ubuntu2004:~$ sudo cat /proc/1066/environ 
LANG=en_US.UTF-8LANGUAGE=en_US:PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/binINVOCATION_ID=c15345d821dd4d76a8e636f5f779f5d2JOURNAL_STREAM=9:26634EXTRA_ARGS=--web.listen-address=:9101
```

Как мы видим, аргумент передан в переменные окружения процесса и интерфейс доступен по указанному порту `9101`.

## 2. Ознакомьтесь с опциями node_exporter и выводом `/metrics` по-умолчанию. Приведите несколько опций, которые вы бы выбрали для базового мониторинга хоста по CPU, памяти, диску и сети.

1. Процессор:

```
process_cpu_seconds_total
node_cpu_seconds_total{cpu="0",mode="idle"}
node_cpu_seconds_total{cpu="0",mode="iowait"}
node_cpu_seconds_total{cpu="0",mode="system"}
node_cpu_seconds_total{cpu="0",mode="user"}
```

1. Оперативная память:
```
node_memory_MemAvailable_bytes
node_memory_MemFree_bytes
node_memory_MemTotal_bytes
node_memory_SwapFree_bytes
node_memory_SwapTotal_bytes
```

1. Блочные устройства:
```
node_disk_io_time_seconds_total{device="vda"} 
node_disk_read_time_seconds_total{device="vda"}
node_disk_write_time_seconds_total{device="vda"}
node_disk_read_bytes_total{device="vda"} 
node_disk_written_bytes_total{device="vda"}
```

1. Сеть:
```
node_network_receive_bytes_total{device="eth0"}
node_network_receive_errs_total{device="eth0"}
node_network_transmit_bytes_total{device="eth0"}
node_network_transmit_errs_total{device="eth0"}
```

## 3. Установите в свою виртуальную машину [Netdata](https://github.com/netdata/netdata). Воспользуйтесь [готовыми пакетами](https://packagecloud.io/netdata/netdata/install) для установки (`sudo apt install -y netdata`). После успешной установки: пробросте порт `Netdata` на свой локальный компьютер, осуществите вход в интерфейс `Netdata` по `localhost:19999` и ознакомьтесь с метриками, которые по умолчанию собираются `Netdata` и с комментариями, которые даны к этим метрикам.

Установил, пробросил, ознакомился:
![](https://github.com/rudenko-ma/netology.homeworks/blob/main/03-sysadmin-04-os/img/q3.png)

## 4. Можно ли по выводу `dmesg` понять, осознает ли ОС, что загружена не на настоящем оборудовании, а на системе виртуализации?

Да, можно:
```
vagrant@ubuntu2004:~$ dmesg | grep virtualiz
[    0.013770] Booting paravirtualized kernel on KVM
[    1.727519] systemd[1]: Detected virtualization kvm.
```
В данном случае, мы видим что используется гипервизор`KVM`.

А вот вывод с виртуальной машины запущенной под управлением `Hyper-V`:
```
# dmesg | grep virtualiz 
[    0.017028] Booting paravirtualized kernel on Hyper-V
[    2.838227] systemd[1]: Detected virtualization microsoft.
```

## 5. Как настроен sysctl `fs.nr_open` на системе по-умолчанию? Узнайте, что означает этот параметр. Какой другой существующий лимит не позволит достичь такого числа (`ulimit --help`)?

По умолчанию параметр `fs.nr_open` имеет значение `1048576`.
```
vagrant@ubuntu2004:~$ sysctl fs.nr_open
fs.nr_open = 1048576

```

Данный параметр определяет максимально допустимое кол-во файловых дескрипторов открытых в системе.

Другой существующий лимит - это "мягкий" лимит пользователя, который по умолчанию равен `1024`:
```
vagrant@ubuntu2004:~$ ulimit -Sn
1024
```

## 6. Запустите любой долгоживущий процесс (не `ls`, который отработает мгновенно, а, например, `sleep 1h`) в отдельном неймспейсе процессов; покажите, что ваш процесс работает под PID 1 через `nsenter`. Для простоты работайте в данном задании под root (`sudo -i`). Под обычным пользователем требуются дополнительные опции (`--map-root-user`) и т.д.

Запускаем длительный процесс в отдельном пространстве имен:
```
root@ubuntu2004:~# unshare -f -p --mount-proc sleep 1h
```

Находим PID `unshare`, находим его потомка `sleep`, переходим в пространство имен данного процесса и смотрим его `PID`:
```
root@ubuntu2004:~# ps aux | grep unshare
root       26215  0.0  0.0   9832   532 pts/0    S+   15:21   0:00 unshare -f -p --mount-proc sleep 1h
root       26218  0.0  0.0  10760   736 pts/1    S+   15:21   0:00 grep --color=auto unshare
root@ubuntu2004:~# pstree -p 26215
unshare(26215)───sleep(26216)
root@ubuntu2004:~# nsenter -t 26216 -p -m
root@ubuntu2004:/# ps aux
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.0  0.0   9828   584 pts/0    S+   15:21   0:00 sleep 1h
root           2  0.2  0.5  12600  5048 pts/1    S    15:22   0:00 -bash
root          11  0.0  0.3  13216  3276 pts/1    R+   15:22   0:00 ps aux
```

## 7. Найдите информацию о том, что такое `:(){ :|:& };:`. Запустите эту команду в своей виртуальной машине Vagrant с Ubuntu 20.04 (**это важно, поведение в других ОС не проверялось**). Некоторое время все будет "плохо", после чего (минуты) – ОС должна стабилизироваться. Вызов `dmesg` расскажет, какой механизм помог автоматической стабилизации. Как настроен этот механизм по-умолчанию, и как изменить число процессов, которое можно создать в сессии?

Конструкция `:(){ :|:& };:` определяет и вызывает функцию с именем `:`.
```
vagrant@ubuntu2004:~$ :(){ :|:& };:
[1] 80677
vagrant@ubuntu2004:~$ -bash: fork: retry: Resource temporarily unavailable
-bash: fork: retry: Resource temporarily unavailable
-bash: fork: retry: Resource temporarily unavailable
...
```

Данная функция рекурсивно дважды вызывает сама себя в фоне порождая большое кол-во процессов `bash`. 
```
vagrant@ubuntu2004:~$ type -a :
: is a function
: () 
{ 
    : | : &
}
: is a shell builtin

```

Так как внутри функции нет ограничений на глубину рекурсии кол-во процессов достигает установленного лимита.
```
vagrant@ubuntu2004:~$ ulimit -u
3571
```
За спасение системы отвечает механизм `cgroup` предназначенный для ограничения ресурсов. Он блокирует порождение новых процессов сверх лимита, а так как функция больше ничего не делает, уже запущенные процессы завершаются.

```
vagrant@ubuntu2004:~$ dmesg -T
...
[Thu Jan 20 16:22:14 2022] cgroup: fork rejected by pids controller in /user.slice/user-1000.slice/session-5.scope
```

Изменить лимит на число запущенных пользовательских процессов(например, уменьшить до 100) можно коммандой:
```
vagrant@ubuntu2004:~$ ulimit -u 100
vagrant@ubuntu2004:~$ ulimit -u
100

```

Чтобы новые лимиты сохранились после перезагрузки нужно добавить их в файл `/etc/security/limits.conf`.

Кстати, состояние системы в этот момент можно пронаблюдать в установленной ранее `netdata` (правда в процессе система перестает отвечать на запросы метрик и часть данных отсутствует):
![](https://github.com/rudenko-ma/netology.homeworks/blob/main/03-sysadmin-04-os/img/q7.png)

