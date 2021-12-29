# Домашнее задание к занятию "3.1. Работа в терминале, лекция 1"

- Установите средство виртуализации [Oracle VirtualBox](https://www.virtualbox.org/).
- Установите средство автоматизации [Hashicorp Vagrant](https://www.vagrantup.com/).
- В вашем основном окружении подготовьте удобный для дальнейшей работы терминал. 

Обе программы установлены. Настроен удобный шелл (OhMyZSH+powerlevel10k).
![](https://github.com/rudenko-ma/netology.homeworks/blob/main/03-sysadmin-01-terminal/img/1_and_2.jpeg)

- С помощью базового файла конфигурации запустите Ubuntu 20.04 в VirtualBox посредством Vagrant:

Создал директорию с конфигурацией Vagrant. Выполнил команды.
![](https://github.com/rudenko-ma/netology.homeworks/blob/main/03-sysadmin-01-terminal/img/vagrant_commands.jpeg)

- Ознакомьтесь с графическим интерфейсом VirtualBox, посмотрите как выглядит виртуальная машина, которую создал для вас Vagrant, какие аппаратные ресурсы ей выделены. Какие ресурсы выделены по-умолчанию?

По умолчанию выделены следующие ресурсы: vCPU: 2, RAM: 1024 MB, HDD: 64Gb, Network: NAT, папка с файлом Vagrantfile подключается к ВМ как общая.
![](https://github.com/rudenko-ma/netology.homeworks/blob/main/03-sysadmin-01-terminal/img/vbox_vm_settings.jpeg)

- Ознакомьтесь с возможностями конфигурации VirtualBox через Vagrantfile: [документация](https://www.vagratup.com/docs/providers/virtualbox/configuration.html). Как добавить оперативной памяти или ресурсов процессора виртуальной машине?

Согласно документации добавить оперативной памяти или вируальных ядер можно посредством добавления в конфигурационный файл следующих строрк:
```
config.vm.provider "virtualbox" do |v|
  v.memory = 1024
  v.cpus = 2
end

```

- Команда `vagrant ssh` из директории, в которой содержится Vagrantfile, позволит вам оказаться внутри виртуальной машины без каких-либо дополнительных настроек. Попрактикуйтесь в выполнении обсуждаемых команд в терминале Ubuntu.

![](https://github.com/rudenko-ma/netology.homeworks/blob/main/03-sysadmin-01-terminal/img/vagrant_ssh.jpeg)

- Ознакомиться с разделами `man bash`, почитать о настройках самого bash:
    * длину журнала `history` можно задать переменной окружения `HISTSIZE` (это описывается в 977 строке мануала).
    * директива `ignoreboth` позволяет не сохранять команды начинающиеся с пробела и не дублировать повторно введенные команды. 


![](https://github.com/rudenko-ma/netology.homeworks/blob/main/03-sysadmin-01-terminal/img/histsize.jpeg)
![](https://github.com/rudenko-ma/netology.homeworks/blob/main/03-sysadmin-01-terminal/img/ignoreboth.jpeg)

- В каких сценариях использования применимы скобки `{}` и на какой строчке `man bash` это описано?

Вопрос не совсем понятен, но видимо имелась ввиду строка 1229.
![](https://github.com/rudenko-ma/netology.homeworks/blob/main/03-sysadmin-01-terminal/img/brace_expansion.jpeg)


- С учётом ответа на предыдущий вопрос, как создать однократным вызовом `touch` 100000 файлов? Получится ли аналогичным образом создать 300000? Если нет, то почему?

```
touch prefix-{1..100000}-suffix

```
По умолчанию создать таким образом 300000 файлов не получится потому что список имен файлов в раскрывшемся виде превысит рамер стека. Если это необходимо, мы можем увеличить размер стэка при помощи программы `ulimit`.
![](https://github.com/rudenko-ma/netology.homeworks/blob/main/03-sysadmin-01-terminal/img/300000_files.jpeg)


- В man bash поищите по `/\[\[`. Что делает конструкция `[[ -d /tmp ]]`

Данная конструкция вернет `True` если существует директория  `/tmp`.

- Основываясь на знаниях о просмотре текущих (например, PATH) и установке новых переменных; командах, которые мы рассматривали, добейтесь в выводе type -a bash в виртуальной машине наличия первым пунктом в списке:

![](https://github.com/rudenko-ma/netology.homeworks/blob/main/03-sysadmin-01-terminal/img/type_a_bash.jpeg)

- Чем отличается планирование команд с помощью `batch` и `at`?

Задание запланированное при помощи `batch` будет выполнено когда LA станет ниже 0.8
Задание запланированное при помощи `at` будет выполнено в указанное время.

