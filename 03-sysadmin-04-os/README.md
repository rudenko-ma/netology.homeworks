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
ExecStart=/usr/local/bin/node_exporter

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
vagrant@ubuntu2004:~$ echo "ARGS=--my-extra-option=some-value" | sudo tee /etc/default/node_exporter
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
             └─1066 /usr/local/bin/node_exporter

Jan 19 07:10:19 ubuntu2004 node_exporter[1066]: ts=2022-01-19T07:10:19.658Z caller=node_exporter.go:115 level=info collector=thermal_zone
Jan 19 07:10:19 ubuntu2004 node_exporter[1066]: ts=2022-01-19T07:10:19.658Z caller=node_exporter.go:115 level=info collector=time
Jan 19 07:10:19 ubuntu2004 node_exporter[1066]: ts=2022-01-19T07:10:19.658Z caller=node_exporter.go:115 level=info collector=timex
Jan 19 07:10:19 ubuntu2004 node_exporter[1066]: ts=2022-01-19T07:10:19.659Z caller=node_exporter.go:115 level=info collectorudp_queues
Jan 19 07:10:19 ubuntu2004 node_exporter[1066]: ts=2022-01-19T07:10:19.659Z caller=node_exporter.go:115 level=info collector=uname
Jan 19 07:10:19 ubuntu2004 node_exporter[1066]: ts=2022-01-19T07:10:19.659Z caller=node_exporter.go:115 level=info collector=vmstat
Jan 19 07:10:19 ubuntu2004 node_exporter[1066]: ts=2022-01-19T07:10:19.659Z caller=node_exporter.go:115 level=info collector=xfs
Jan 19 07:10:19 ubuntu2004 node_exporter[1066]: ts=2022-01-19T07:10:19.659Z caller=node_exporter.go:115 level=info collector=zfs
Jan 19 07:10:19 ubuntu2004 node_exporter[1066]: ts=2022-01-19T07:10:19.659Z caller=node_exporter.go:199 level=info msg="Listening on" address=:9100
Jan 19 07:10:19 ubuntu2004 node_exporter[1066]: ts=2022-01-19T07:10:19.660Z caller=tls_config.go:195 level=info msg="TLS is disabled." http2=false
vagrant@ubuntu2004:~$ sudo cat /proc/1066/environ 
LANG=en_US.UTF-8LANGUAGE=en_US:PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/binINVOCATION_ID=c15345d821dd4d76a8e636f5f779f5d2JOURNAL_STREAM=9:26634ARGS=--my-extra-option=some-value
```

Как мы видим, аргумент передан в переменные окружения процесса.

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

## 3. Установите в свою виртуальную машину [Netdata](https://github.com/netdata/netdata). Воспользуйтесь [готовыми пакетами](https://packagecloud.io/netdata/netdata/install) для установки (`sudo apt install -y netdata`). После успешной установки:

![](https://github.com/rudenko-ma/netology.homeworks/blob/main/03-sysadmin-04-os/img/q3.png)

## 4. Можно ли по выводу `dmesg` понять, осознает ли ОС, что загружена не на настоящем оборудовании, а на системе виртуализации?



## 5. Как настроен sysctl `fs.nr_open` на системе по-умолчанию? Узнайте, что означает этот параметр. Какой другой существующий лимит не позволит достичь такого числа (`ulimit --help`)?



## 6. Запустите любой долгоживущий процесс (не `ls`, который отработает мгновенно, а, например, `sleep 1h`) в отдельном неймспейсе процессов; покажите, что ваш процесс работает под PID 1 через `nsenter`. Для простоты работайте в данном задании под root (`sudo -i`). Под обычным пользователем требуются дополнительные опции (`--map-root-user`) и т.д.



## 7. Найдите информацию о том, что такое `:(){ :|:& };:`. Запустите эту команду в своей виртуальной машине Vagrant с Ubuntu 20.04 (**это важно, поведение в других ОС не проверялось**). Некоторое время все будет "плохо", после чего (минуты) – ОС должна стабилизироваться. Вызов `dmesg` расскажет, какой механизм помог автоматической стабилизации. Как настроен этот механизм по-умолчанию, и как изменить число процессов, которое можно создать в сессии?
