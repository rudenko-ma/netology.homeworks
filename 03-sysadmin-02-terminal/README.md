# Домашнее задание к занятию "3.2. Работа в терминале, лекция 2"

## 1. Какого типа команда `cd`? Попробуйте объяснить, почему она именно такого типа; опишите ход своих мыслей, если считаете что она могла бы быть другого типа.

Команда `cd` является встроенной командой оболочки, поскольку перемещение по директориям виртуальной файловой системы является одной из важнейших функций оболчки.

```
# type -a cd
cd is a shell builtin
```
Однако, мы можем переопределить данную команду(как и любую другую) посредством механизма псевдонимов(алиасов) или объявив функцию с таким же именем.

![](https://github.com/rudenko-ma/netology.homeworks/blob/main/03-sysadmin-02-terminal/img/q1.png)

## 2. Какая альтернатива без pipe команде `grep <some_string> <some_file> | wc -l`? `man grep` поможет в ответе на этот вопрос. Ознакомьтесь с [документом](http://www.smallo.ruhr.de/award.html) о других подобных некорректных вариантах использования pipe.

Вызов программы `wc` в однострочнике `grep <some_string> <some_file> | wc -l` является некорректным поскольку программа `grep` имеет встроенную возможность подсчета совпадений.

```
# grep 'dhcp' /var/log/syslog | wc -l
6525

# grep 'dhcp' /var/log/syslog -c     
6525
```

## 3. Какой процесс с PID `1` является родителем для всех процессов в вашей виртуальной машине Ubuntu 20.04?

Родителем для всех процессов в Ubuntu 20.04 является `systemd` запущенный посредством символической ссылки `/sbin/init`.

```
# ps 1
    PID TTY      STAT   TIME COMMAND
      1 ?        Ss     0:15 /sbin/init splash

# file /sbin/init
/sbin/init: symbolic link to /lib/systemd/systemd
```

## 4. Как будет выглядеть команда, которая перенаправит вывод stderr `ls` на другую сессию терминала?

Для перенаправления `stderr` на другой терминал необходимо сначала узнать его имя в виртуальной файловой системе при помощи команды `tty`. 

```
# tty
/dev/pts/15

```

После этого можно перенаправить поток `stderr` стандартным способом.

```
# ls --bad-param 2> /dev/pts/15

```

![](https://github.com/rudenko-ma/netology.homeworks/blob/main/03-sysadmin-02-terminal/img/q4.png)

## 5. Получится ли одновременно передать команде файл на stdin и вывести ее stdout в другой файл? Приведите работающий пример.

В примере ниже конструкция `(read input && echo "Input: "$input")` имитирует произвольную комманду ожидающую ввод пользователя и выводящую информацию в `stdout`.

```
# echo "Произольные данные\n" > ./somedata.txt
# (read input && echo "Input: $input") < ./somedata.txt 1> ./someoutput.txt

```

![](https://github.com/rudenko-ma/netology.homeworks/blob/main/03-sysadmin-02-terminal/img/q5.png)

## 6. Получится ли находясь в графическом режиме, вывести данные из PTY в какой-либо из эмуляторов TTY? Сможете ли вы наблюдать выводимые данные?

Да, получится. Для вывода данных в TTY (например №7) используем команду: `echo "<somedata>" | sudo tee /dev/tty7`

Для того, чтобы переключиться на `tty7` используем команду: `sudo chvt 7`.

Чтобы пронаблюдать вывод даты в `tty7` можно воспользоваться следующим однострочником:

```
sudo chvt 7 && echo "$(date +'%Y%m%d-%H%M%S')" | sudo tee /dev/tty7 && sleep 5 && sudo chvt 1
```

Данный однострочник переключит нас на teletype #7, затем отправит текущие дату-время в утилиту `tee`, утилита `tee` (с правами суперпользователя) выведет полученные данные на `tty7`, далее произойдет пауза в 5 секунд (чтобы мы могли увидеть выведенные данные), и далее система снова переключится на `tty1` в котором в Ubuntu 20.04 запущено графическое окружение.

## 7. Выполните команду `bash 5>&1`. К чему она приведет? Что будет, если вы выполните `echo netology > /proc/$$/fd/5`? Почему так происходит?

Команда `bash 5>$1` приведет к запуску нового дочернего процесса `bash` для которого будет создан дополнительный файловый дескриптор `5`, связанный с `stdout`.

Если после этого выполнить в данном экземпляре `bash` команду `echo netology > /proc/$$/fd/5`, то строка `netology` будет отправлена в этот файловый дескриптор и ,следовательно, выведена в `stdout`.

## 8. Получится ли в качестве входного потока для pipe использовать только stderr команды, не потеряв при этом отображение stdout на pty? Напоминаем: по умолчанию через pipe передается только stdout команды слева от `|` на stdin команды справа. Это можно сделать, поменяв стандартные потоки местами через промежуточный новый дескриптор, который вы научились создавать в предыдущем вопросе.

Конструкция `(pwd && cd /dir_is_not_exist)` выводит текущую рабочую директорию в `stdout` и ошибку об отсутствии директории `/dir_is_not_exist` в `stderr`.

При помощи конструкции `3>&1 1>&2 2>&3` мы создаем новый промежуточный файловый дескриптор `3` и перенаправляем выводы так, что вывод в `stdout` уйдет в `stderr`, вывод в `stderr` уйдет в `fd/3` а вывод в `fd/3` уйдет в `stdout`.

Таким образом, в качестве входного потока для `pipe` используется только `stderr` конструкции `(pwd && cd /dir_is_not_exist)`, но при этом её `stdout` будет выведен в терминал через `stderr`.

```
# (pwd && cd /dir_is_not_exist) 3>&1 1>&2 2>&3 | cat > file_out.text
/home/boroda

# cat file_out.text
cd: no such file or directory: /dir_is_not_exist
```

## 9. Что выведет команда `cat /proc/$$/environ`? Как еще можно получить аналогичный по содержанию вывод?

Команда `cat /proc/$$/environ` выведет переменные окружения текущей сессии `bash`.

Аналогичный (и даже более читабельный вывод) можно получить командой `env` или `printenv`.

## 10. Используя `man`, опишите что доступно по адресам `/proc/<PID>/cmdline`, `/proc/<PID>/exe`.

`/proc/[pid]/exe`

В Linux 2.2 и новее этот файл является символьной ссылкой, содержащей актуальный путь выполняемой команды. Данная символьная ссылка может обрабатываться обычным образом; попытка её открытия приведёт к открытию исполняемого файла.
(`man proc, строка 301`)

`/proc/[pid]/cmdline`

Данный  файл,  доступный  только для чтения, содержит полную командную строку процесса, если процесс не является зомби. В последнем случае этот файл пуст, поэтому чтение из него вернёт 0 символов.
(`man proc, строка 243`)

![](https://github.com/rudenko-ma/netology.homeworks/blob/main/03-sysadmin-02-terminal/img/q10.png)

## 11. Узнайте, какую наиболее старшую версию набора инструкций SSE поддерживает ваш процессор с помощью `/proc/cpuinfo`.

Мой процессор поддерживает SSE 4.2

```
# grep sse /proc/cpuinfo
flags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ss ht syscall nx pdpe1gb rdtscp lm constant_tsc rep_good nopl xtopology cpuid aperfmperf pni pclmulqdq ssse3 fma cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt aes xsave avx f16c rdrand hypervisor lahf_lm abm 3dnowprefetch invpcid_single ssbd ibrs ibpb stibp ibrs_enhanced fsgsbase bmi1 avx2 smep bmi2 erms invpcid rdseed adx smap clflushopt xsaveopt xsavec xgetbv1 xsaves flush_l1d arch_capabilities
flags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ss ht syscall nx pdpe1gb rdtscp lm constant_tsc rep_good nopl xtopology cpuid aperfmperf pni pclmulqdq ssse3 fma cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt aes xsave avx f16c rdrand hypervisor lahf_lm abm 3dnowprefetch invpcid_single ssbd ibrs ibpb stibp ibrs_enhanced fsgsbase bmi1 avx2 smep bmi2 erms invpcid rdseed adx smap clflushopt xsaveopt xsavec xgetbv1 xsaves flush_l1d arch_capabilities
flags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ss ht syscall nx pdpe1gb rdtscp lm constant_tsc rep_good nopl xtopology cpuid aperfmperf pni pclmulqdq ssse3 fma cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt aes xsave avx f16c rdrand hypervisor lahf_lm abm 3dnowprefetch invpcid_single ssbd ibrs ibpb stibp ibrs_enhanced fsgsbase bmi1 avx2 smep bmi2 erms invpcid rdseed adx smap clflushopt xsaveopt xsavec xgetbv1 xsaves flush_l1d arch_capabilities
flags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ss ht syscall nx pdpe1gb rdtscp lm constant_tsc rep_good nopl xtopology cpuid aperfmperf pni pclmulqdq ssse3 fma cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt aes xsave avx f16c rdrand hypervisor lahf_lm abm 3dnowprefetch invpcid_single ssbd ibrs ibpb stibp ibrs_enhanced fsgsbase bmi1 avx2 smep bmi2 erms invpcid rdseed adx smap clflushopt xsaveopt xsavec xgetbv1 xsaves flush_l1d arch_capabilities
```

## 12. При открытии нового окна терминала и `vagrant ssh` создается новая сессия и выделяется pty. Это можно подтвердить командой `tty`, которая упоминалась в лекции 3.2. Однако: `vagrant@netology1:~$ ssh localhost 'tty'` возвращает `not a tty`. Почитайте, почему так происходит, и как изменить поведение.

Это происходит потому, что при обычном подключении по `ssh` создается `tty` и запускается `shell` (так как предполагается, что мы хотим работать с терминалом). В случае запуска команды на удаленном сервере, `tty` не создается (для обеспечения прозрачной передачи бинарных данных).

Если нам необходмимо запустить команду из под `shell` то мы можем указать ключ `-t`.

```
# vagrant ssh
Last login: Wed Jan 12 16:43:17 2022 from 192.168.121.1
vagrant@ubuntu2004:~$ ssh localhost -t tty
vagrant@localhost's password: 
/dev/pts/1
Connection to localhost closed.

```

## 13. Бывает, что есть необходимость переместить запущенный процесс из одной сессии в другую. Попробуйте сделать это, воспользовавшись `reptyr`. Например, так можно перенести в `screen` процесс, который вы запустили по ошибке в обычной SSH-сессии.

1. Сначала запустим длительный процесс и отправим его в фоновые задания посредством `Ctrl+z`

```
# watch ls -la 

[1]  + 5635 suspended  watch ls -la

```

2. В нашем случае мы сразу узнали PID процесса `5635`, но можно убедиться что процесс присутствует в фоновых заданиях:

```
# jobs -l
[1]  + 5635 suspended  watch ls -la

```

3. Для чистоты переноса можно убрать процесс из списка заданий (опционально):
```
# disown watch
disown: warning: job is suspended, use `kill -CONT -5635' to resume

```

4. В Ubuntu 20.04 для преодоления ограничений безопасности необходимо включить `ptrace`:

```
# echo 0 | sudo tee /proc/sys/kernel/yama/ptrace_scope
0

```

5. Запускаем `screen` и выполняем `reptyr` для нашего процесса:

```
# screen

# reptyr 5635

```

6. Приостановленный процесс будет возобновлен в сессии `screen`

7. Отключаемся от сессии посредством `Ctrl+a+d`

8. Отключаем `ptrace`:
```
# echo 1 | sudo tee /proc/sys/kernel/yama/ptrace_scope
1

```

9. Теперь наш процесс полностью перенесен в сессию `screen` в которую мы можем вернуться при помощи команды `screen -dR`

## 14. `sudo echo string > /root/new_file` не даст выполнить перенаправление под обычным пользователем, так как перенаправлением занимается процесс shell'а, который запущен без `sudo` под вашим пользователем. Для решения данной проблемы можно использовать конструкцию `echo string | sudo tee /root/new_file`. Узнайте что делает команда `tee` и почему в отличие от `sudo echo` команда с `sudo tee` будет работать.

Команда `tee` считывает стандартный ввод и записывает его одновременно в стандартный вывод и в один или несколько файлов. 

При использовании конструкции `echo string | sudo tee /root/new_file` команда `tee` запускается от суперпользователя, соответственно имеет права на запись в файл.
