# Домашнее задание к занятию "3.3. Операционные системы, лекция 1"

## 1. Какой системный вызов делает команда `cd`? В прошлом ДЗ мы выяснили, что `cd` не является самостоятельной  программой, это `shell builtin`, поэтому запустить `strace` непосредственно на `cd` не получится. Тем не менее, вы можете запустить `strace` на `/bin/bash -c 'cd /tmp'`. В этом случае вы увидите полный список системных вызовов, которые делает сам `bash` при старте. Вам нужно найти тот единственный, который относится именно к `cd`. Обратите внимание, что `strace` выдаёт результат своей работы в поток stderr, а не в stdout.

Системным вызовом команды `cd` приводящим к смене рабочей директории является системный вызов `chdir`.

```
# strace bash -c 'cd ~/Projects' 2>&1 | grep Projects              
execve("/bin/bash", ["bash", "-c", "cd ~/Projects"], 0x7ffe2e684060 /* 67 vars */) = 0
stat("/home/boroda/Projects/netology/netology.homeworks/03-sysadmin-03-os", {st_mode=S_IFDIR|0775, st_size=4096, ...}) = 0
stat("/home/boroda/Projects", {st_mode=S_IFDIR|0775, st_size=4096, ...}) = 0
stat("/home/boroda/Projects/netology", {st_mode=S_IFDIR|0775, st_size=4096, ...}) = 0
stat("/home/boroda/Projects/netology/netology.homeworks", {st_mode=S_IFDIR|0775, st_size=4096, ...}) = 0
stat("/home/boroda/Projects/netology/netology.homeworks/03-sysadmin-03-os", {st_mode=S_IFDIR|0775, st_size=4096, ...}) = 0
stat("/home/boroda/Projects", {st_mode=S_IFDIR|0775, st_size=4096, ...}) = 0
chdir("/home/boroda/Projects")          = 0

```

## 2. Попробуйте использовать команду `file` на объекты разных типов на файловой системе. Используя `strace` выясните, где находится база данных `file` на основании которой она делает свои догадки.

Пользуюсь регулярно.
```
vagrant@ubuntu2004:~$ file /sbin/init
/sbin/init: symbolic link to /lib/systemd/systemd

vagrant@ubuntu2004:~$ file /lib/systemd/systemd
/lib/systemd/systemd: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=2ede8a7dfd7aec024d95621e47c7f6fc5ab14b44, for GNU/Linux 3.2.0, stripped

vagrant@ubuntu2004:~$ file /run/dbus/system_bus_socket 
/run/dbus/system_bus_socket: socket

vagrant@ubuntu2004:~$ file /dev/vda
/dev/vda: block special (252/0)

vagrant@ubuntu2004:~$ file /dev/tty
/dev/tty: character special (5/0)
```

Чтобы выяснить где находится база данных:

1. Отфильтруем вывод `strace file` в поисках системного вызова `openat` отвечающего за открытие файла фильтруя строки с ошибкой `ENOENT`:

```
# strace file /dev/vda 2>&1 | grep openat | grep -v ENOENT
openat(AT_FDCWD, "/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libmagic.so.1", O_RDONLY|O_CLOEXEC) = 3
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libc.so.6", O_RDONLY|O_CLOEXEC) = 3
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/liblzma.so.5", O_RDONLY|O_CLOEXEC) = 3
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libbz2.so.1.0", O_RDONLY|O_CLOEXEC) = 3
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libz.so.1", O_RDONLY|O_CLOEXEC) = 3
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libpthread.so.0", O_RDONLY|O_CLOEXEC) = 3
openat(AT_FDCWD, "/usr/lib/locale/locale-archive", O_RDONLY|O_CLOEXEC) = 3
openat(AT_FDCWD, "/etc/magic", O_RDONLY) = 3
openat(AT_FDCWD, "/usr/share/misc/magic.mgc", O_RDONLY) = 3
openat(AT_FDCWD, "/usr/lib/x86_64-linux-gnu/gconv/gconv-modules.cache", O_RDONLY) = 3

```

2. Проверяем файлы начиная с конца списка:
```
# file /usr/lib/x86_64-linux-gnu/gconv/gconv-modules.cache                       
/usr/lib/x86_64-linux-gnu/gconv/gconv-modules.cache: gconv module configuration cache data

# file /usr/share/misc/magic.mgc                     
/usr/share/misc/magic.mgc: symbolic link to ../../lib/file/magic.mgc

# file /usr/share/misc/../../lib/file/magic.mgc           
/usr/share/misc/../../lib/file/magic.mgc: magic binary file for file(1) cmd (version 14) (little endian)

```

3. Файл `magic.mgc` является бинарным файлом для команды `file`.

4. Ищем в `man file` имя этого файла и убеждаемся в том, что информация необходимая для идентификации файлов действительно хранится в нём (и не только).

## 3. Предположим, приложение пишет лог в текстовый файл. Этот файл оказался удален (deleted в lsof), однако возможности сигналом сказать приложению переоткрыть файлы или просто перезапустить приложение – нет. Так как приложение продолжает писать в удаленный файл, место на диске постепенно заканчивается. Основываясь на знаниях о перенаправлении потоков предложите способ обнуления открытого удаленного файла (чтобы освободить место на файловой системе).

Сначала напишем однострочник имитирующий работу приложения (он будет записывать в файл 1 Гигабайт случайных данных раз в 10 секунд):

```
# (while true; do dd if=/dev/urandom bs=16M count=64; sleep 10; done;) >> big.log
64+0 records in
64+0 records out
1073741824 bytes (1,1 GB, 1,0 GiB) copied, 5,1745 s, 208 MB/s

```

Теперь узнаем сколько свободного места осталось на диске:

```
# df -h | grep root                                   
/dev/mapper/vgkubuntu-root  124G   23G   95G  20% /

```

Далее удалим файл, узнаем PID процесса удерживающего файловый дескриптор, и убедимся что свободное место на диске продолжает уменьшаться:

```
# rm big.log       

# sudo lsof 2> /dev/null | grep deleted | grep big.log
zsh       69960                           boroda    1w      REG              253,0 2147483648    4849708 /home/boroda/big.log (deleted)
sleep     69970                           boroda    1w      REG              253,0 2147483648    4849708 /home/boroda/big.log (deleted)

# df -h | grep root
/dev/mapper/vgkubuntu-root  124G   26G   92G  22% /

```

Теперь мы можем очистить содержимое удаленного файла и убедиться в том что место освободилось:

```
# sudo cat /dev/null > /proc/69960/fd/1                                          

# df -h | grep root                                   
/dev/mapper/vgkubuntu-root  124G   23G   95G  20% /
```

![](https://github.com/rudenko-ma/netology.homeworks/blob/main/03-sysadmin-03-os/img/q333ng)

## 4. Занимают ли зомби-процессы какие-то ресурсы в ОС (CPU, RAM, IO)?



## 5. В iovisor BCC есть утилита `opensnoop`:
    ```bash
    root@vagrant:~# dpkg -L bpfcc-tools | grep sbin/opensnoop
    /usr/sbin/opensnoop-bpfcc
    ```
    На какие файлы вы увидели вызовы группы `open` за первую секунду работы утилиты? Воспользуйтесь пакетом `bpfcc-tools` для Ubuntu 20.04. Дополнительные [сведения по установке](https://github.com/iovisor/bcc/blob/master/INSTALL.md).


## 6. Какой системный вызов использует `uname -a`? Приведите цитату из man по этому системному вызову, где описывается альтернативное местоположение в `/proc`, где можно узнать версию ядра и релиз ОС.



## 7. Чем отличается последовательность команд через `;` и через `&&` в bash? Например:
    ```bash
    root@netology1:~# test -d /tmp/some_dir; echo Hi
    Hi
    root@netology1:~# test -d /tmp/some_dir && echo Hi
    root@netology1:~#
    ```
    Есть ли смысл использовать в bash `&&`, если применить `set -e`?


## 8. Из каких опций состоит режим bash `set -euxo pipefail` и почему его хорошо было бы использовать в сценариях?



## 9. Используя `-o stat` для `ps`, определите, какой наиболее часто встречающийся статус у процессов в системе. В `man ps` ознакомьтесь (`/PROCESS STATE CODES`) что значат дополнительные к основной заглавной буквы статуса процессов. Его можно не учитывать при расчете (считать S, Ss или Ssl равнозначными).



