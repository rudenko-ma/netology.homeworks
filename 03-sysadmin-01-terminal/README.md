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

1. Команда `vagrant ssh` из директории, в которой содержится Vagrantfile, позволит вам оказаться внутри виртуальной машины без каких-либо дополнительных настроек. Попрактикуйтесь в выполнении обсуждаемых команд в терминале Ubuntu.

1. Ознакомиться с разделами `man bash`, почитать о настройках самого bash:
    * какой переменной можно задать длину журнала `history`, и на какой строчке manual это описывается?
    * что делает директива `ignoreboth` в bash?
1. В каких сценариях использования применимы скобки `{}` и на какой строчке `man bash` это описано?
1. С учётом ответа на предыдущий вопрос, как создать однократным вызовом `touch` 100000 файлов? Получится ли аналогичным образом создать 300000? Если нет, то почему?
1. В man bash поищите по `/\[\[`. Что делает конструкция `[[ -d /tmp ]]`
1. Основываясь на знаниях о просмотре текущих (например, PATH) и установке новых переменных; командах, которые мы рассматривали, добейтесь в выводе type -a bash в виртуальной машине наличия первым пунктом в списке:

	```bash
	bash is /tmp/new_path_directory/bash
	bash is /usr/local/bin/bash
	bash is /bin/bash
	```

	(прочие строки могут отличаться содержимым и порядком)
    В качестве ответа приведите команды, которые позволили вам добиться указанного вывода или соответствующие скриншоты.

1. Чем отличается планирование команд с помощью `batch` и `at`?

1. Завершите работу виртуальной машины чтобы не расходовать ресурсы компьютера и/или батарею ноутбука.
