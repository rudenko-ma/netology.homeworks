# Домашнее задание к занятию "3.5. Файловые системы"

## 1. Узнайте о [sparse](https://ru.wikipedia.org/wiki/%D0%A0%D0%B0%D0%B7%D1%80%D0%B5%D0%B6%D1%91%D0%BD%D0%BD%D1%8B%D0%B9_%D1%84%D0%B0%D0%B9%D0%BB) (разряженных) файлах.

На заметку:
```
# создание разряженного файла
truncate -s200G ./sparse-file

# преобразование обычного файла в разрежённый (выполнение поиска дыр и записи их расположения (смещений и длин) в метаданные файла):
cp --sparse=always ./simple-file ./sparse-file
```

## 2. Могут ли файлы, являющиеся жесткой ссылкой на один объект, иметь разные права доступа и владельца? Почему?

Нет, не могут. Жесткая ссылка указывает на тот же самый `inode`, следовательно: права, содержимое и свойства файла будут идентичны.

## 3. Сделайте `vagrant destroy` на имеющийся инстанс Ubuntu. Замените содержимое Vagrantfile конфигурацией, которая создаст новую виртуальную машину с двумя дополнительными неразмеченными дисками по 2.5 Гб.

Скорректировал вопрос, так как в моем случае в качестве гипервизора для `vagrant` используется `kvm`. Получившийся конфиг:

```
ENV['VAGRANT_DEFAULT_PROVIDER'] = 'libvirt'

Vagrant.configure("2") do |config|
  config.vm.define "u20fs" do |h|
    h.vm.hostname = "u20fs"
    h.vm.box = "generic/ubuntu2004"
    h.vm.box_check_update = false
    h.vm.provider :libvirt do |v|
      v.memory = 1024
      v.cpus = 1
      v.storage :file, :size => '2560M', :type => 'qcow2', :bus => 'scsi'
      v.storage :file, :size => '2560M', :type => 'qcow2', :bus => 'scsi'
    end
  end
end

```

## 4. Используя `fdisk`, разбейте первый диск на 2 раздела: 2 Гб, оставшееся пространство.

<details>
  <summary>Создание двух разделов:</summary>

  ```
  vagrant@u20fs:~$ sudo fdisk /dev/sda

Welcome to fdisk (util-linux 2.34).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.

Device does not contain a recognized partition table.
Created a new DOS disklabel with disk identifier 0x715c9424.

Command (m for help): n
Partition type
   p   primary (0 primary, 0 extended, 4 free)
   e   extended (container for logical partitions)
Select (default p): p
Partition number (1-4, default 1): 1
First sector (2048-5242879, default 2048): 
Last sector, +/-sectors or +/-size{K,M,G,T,P} (2048-5242879, default 5242879): +2G

Created a new partition 1 of type 'Linux' and of size 2 GiB.

Command (m for help): n
Partition type
   p   primary (1 primary, 0 extended, 3 free)
   e   extended (container for logical partitions)
Select (default p): p
Partition number (2-4, default 2): 2
First sector (4196352-5242879, default 4196352): 
Last sector, +/-sectors or +/-size{K,M,G,T,P} (4196352-5242879, default 5242879): 

Created a new partition 2 of type 'Linux' and of size 511 MiB.

Command (m for help): p
Disk /dev/sda: 2.51 GiB, 2684354560 bytes, 5242880 sectors
Disk model: QEMU HARDDISK   
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x715c9424

Device     Boot   Start     End Sectors  Size Id Type
/dev/sda1          2048 4196351 4194304    2G 83 Linux
/dev/sda2       4196352 5242879 1046528  511M 83 Linux

Command (m for help): w
The partition table has been altered.
Calling ioctl() to re-read partition table.
Syncing disks.
  ```
</details>

![](https://github.com/rudenko-ma/netology.homeworks/blob/main/03-sysadmin-05-fs/img/q4.png)

## 5. Используя `sfdisk`, перенесите данную таблицу разделов на второй диск.

<details>
  <summary>Копирование таблицы разделов:</summary>

  ```
  vagrant@u20fs:~$ sudo sfdisk -d /dev/sda | sudo sfdisk /dev/sdb
Checking that no-one is using this disk right now ... OK

Disk /dev/sdb: 2.51 GiB, 2684354560 bytes, 5242880 sectors
Disk model: QEMU HARDDISK   
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes

>>> Script header accepted.
>>> Script header accepted.
>>> Script header accepted.
>>> Script header accepted.
>>> Created a new DOS disklabel with disk identifier 0x715c9424.
/dev/sdb1: Created a new partition 1 of type 'Linux' and of size 2 GiB.
/dev/sdb2: Created a new partition 2 of type 'Linux' and of size 511 MiB.
/dev/sdb3: Done.

New situation:
Disklabel type: dos
Disk identifier: 0x715c9424

Device     Boot   Start     End Sectors  Size Id Type
/dev/sdb1          2048 4196351 4194304    2G 83 Linux
/dev/sdb2       4196352 5242879 1046528  511M 83 Linux

The partition table has been altered.
Calling ioctl() to re-read partition table.
Syncing disks.
  ```
</details>

![](https://github.com/rudenko-ma/netology.homeworks/blob/main/03-sysadmin-05-fs/img/q5.png)

## 6. Соберите `mdadm` RAID1 на паре разделов 2 Гб.

<details>
  <summary>Создаём RAID1:</summary>

  ```
  vagrant@u20fs:~$ sudo mdadm -C -v /dev/md0 -l1 -n2 /dev/sd{a1,b1}
mdadm: Note: this array has metadata at the start and
    may not be suitable as a boot device.  If you plan to
    store '/boot' on this device please ensure that
    your boot-loader understands md/v1.x metadata, or use
    --metadata=0.90
mdadm: size set to 2094080K
Continue creating array? y
mdadm: Defaulting to version 1.2 metadata
mdadm: array /dev/md0 started.
  ```
</details>

![](https://github.com/rudenko-ma/netology.homeworks/blob/main/03-sysadmin-05-fs/img/q6.png)

## 7. Соберите `mdadm` RAID0 на второй паре маленьких разделов.

<details>
  <summary>Создаём RAID0:</summary>

  ```
  vagrant@u20fs:~$ sudo mdadm -C -v /dev/md1 -l0 -n2 /dev/sd{a2,b2}
mdadm: chunk size defaults to 512K
mdadm: Defaulting to version 1.2 metadata
mdadm: array /dev/md1 started.
  ```
</details>

![](https://github.com/rudenko-ma/netology.homeworks/blob/main/03-sysadmin-05-fs/img/q7.png)

## 8. Создайте 2 независимых PV на получившихся md-устройствах.

Создаем два `Physical Vollume`:
```
vagrant@u20fs:~$ sudo pvcreate /dev/md0 /dev/md1
  Physical volume "/dev/md0" successfully created.
  Physical volume "/dev/md1" successfully created.
vagrant@u20fs:~$ sudo pvdisplay 
  --- Physical volume ---
  PV Name               /dev/md1
  VG Name               vg-all
  PV Size               1018.00 MiB / not usable 2.00 MiB
  Allocatable           yes 
  PE Size               4.00 MiB
  Total PE              254
  Free PE               254
  Allocated PE          0
  PV UUID               9RBSJh-xSl0-OqEq-VWIh-ISWv-OOLT-tyt5BM
   
  --- Physical volume ---
  PV Name               /dev/md0
  VG Name               vg-all
  PV Size               <2.00 GiB / not usable 0   
  Allocatable           yes 
  PE Size               4.00 MiB
  Total PE              511
  Free PE               511
  Allocated PE          0
  PV UUID               fbGwe8-GMma-rrWe-W0Ou-xDCc-n1cd-3crnBh
```

## 9. Создайте общую volume-group на этих двух PV.

Создаем общую `Volume Group`:
```
vagrant@u20fs:~$ sudo vgcreate vg-all /dev/md1 /dev/md0
  Volume group "vg-all" successfully created
vagrant@u20fs:~$ sudo vgdisplay
  --- Volume group ---
  VG Name               vg-all
  System ID             
  Format                lvm2
  Metadata Areas        2
  Metadata Sequence No  1
  VG Access             read/write
  VG Status             resizable
  MAX LV                0
  Cur LV                0
  Open LV               0
  Max PV                0
  Cur PV                2
  Act PV                2
  VG Size               <2.99 GiB
  PE Size               4.00 MiB
  Total PE              765
  Alloc PE / Size       0 / 0   
  Free  PE / Size       765 / <2.99 GiB
  VG UUID               iOvjLq-z3Rc-1f65-da4D-z0KU-zGDS-W073fI
```

## 10. Создайте LV размером 100 Мб, указав его расположение на PV с RAID0.

Создаём `Logical Volume`:
```
vagrant@u20fs:~$ sudo lvcreate -L 100M -n lv100M vg-all /dev/md1
  Logical volume "lv100M" created.
vagrant@u20fs:~$ sudo lvdisplay 
  --- Logical volume ---
  LV Path                /dev/vg-all/lv100M
  LV Name                lv100M
  VG Name                vg-all
  LV UUID                GJjwHd-4CLh-s7Zm-zrDb-J1wr-tiYg-6yCb4I
  LV Write Access        read/write
  LV Creation host, time u20fs, 2022-01-25 09:49:50 +0000
  LV Status              available
  # open                 0
  LV Size                100.00 MiB
  Current LE             25
  Segments               1
  Allocation             inherit
  Read ahead sectors     auto
  - currently set to     4096
  Block device           253:0
```

## 11. Создайте `mkfs.ext4` ФС на получившемся LV.

Форматируем `lv100M` в `EXT4`:
```
vagrant@u20fs:~$ sudo mkfs.ext4 /dev/vg-all/lv100M
mke2fs 1.45.5 (07-Jan-2020)
Discarding device blocks: done                            
Creating filesystem with 25600 4k blocks and 25600 inodes

Allocating group tables: done                            
Writing inode tables: done                            
Creating journal (1024 blocks): done
Writing superblocks and filesystem accounting information: done
```

## 12. Смонтируйте этот раздел в любую директорию, например, `/tmp/new`.

Создаем директорию, монтируем `LV` и проверяем:
```
vagrant@u20fs:~$ mkdir -p /tmp/new
vagrant@u20fs:~$ sudo mount /dev/vg-all/lv100M /tmp/new
vagrant@u20fs:~$ df -H | grep lv100M
/dev/mapper/vg--all-lv100M   98M   74k   90M   1% /tmp/new
```

## 13. Поместите туда тестовый файл, например `wget https://mirror.yandex.ru/ubuntu/ls-lR.gz -O /tmp/new/test.gz`.

Загружаем файл на новый раздел (предварительно получив права):
```
vagrant@u20fs:~$ sudo chown -R vagrant:vagrant /tmp/new
vagrant@u20fs:~$ wget https://mirror.yandex.ru/ubuntu/ls-lR.gz -O /tmp/new/test.gz
--2022-01-25 11:06:33--  https://mirror.yandex.ru/ubuntu/ls-lR.gz
Resolving mirror.yandex.ru (mirror.yandex.ru)... 213.180.204.183, 2a02:6b8::183
Connecting to mirror.yandex.ru (mirror.yandex.ru)|213.180.204.183|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 22054145 (21M) [application/octet-stream]
Saving to: ‘/tmp/new/test.gz’

/tmp/new/test.gz          100%[=====================================>]  21.03M  5.94MB/s    in 3.5s    

2022-01-25 11:06:38 (5.94 MB/s) - ‘/tmp/new/test.gz’ saved [22054145/22054145]

```

## 14. Прикрепите вывод `lsblk`.

```
vagrant@u20fs:~$ lsblk
NAME                 MAJ:MIN RM   SIZE RO TYPE  MOUNTPOINT
sda                    8:0    0   2.5G  0 disk  
├─sda1                 8:1    0     2G  0 part  
│ └─md0                9:0    0     2G  0 raid1 
└─sda2                 8:2    0   511M  0 part  
  └─md1                9:1    0  1018M  0 raid0 
    └─vg--all-lv100M 253:0    0   100M  0 lvm   /tmp/new
sdb                    8:16   0   2.5G  0 disk  
├─sdb1                 8:17   0     2G  0 part  
│ └─md0                9:0    0     2G  0 raid1 
└─sdb2                 8:18   0   511M  0 part  
  └─md1                9:1    0  1018M  0 raid0 
    └─vg--all-lv100M 253:0    0   100M  0 lvm   /tmp/new
vda                  252:0    0   128G  0 disk  
├─vda1               252:1    0   487M  0 part  /boot
├─vda2               252:2    0   1.9G  0 part  [SWAP]
└─vda3               252:3    0 125.6G  0 part  /

```

## 15. Протестируйте целостность файла.

Целостность файла не нарушена.
```
vagrant@u20fs:~$ gzip -t /tmp/new/test.gz 
vagrant@u20fs:~$ echo $?
0
```

## 16. Используя pvmove, переместите содержимое PV с RAID0 на RAID1.

```
vagrant@u20fs:~$ sudo pvmove -n /dev/vg-all/lv100M /dev/md1 /dev/md0
  /dev/md1: Moved: 88.00%
  /dev/md1: Moved: 100.00%
vagrant@u20fs:~$ lsblk
NAME                 MAJ:MIN RM   SIZE RO TYPE  MOUNTPOINT
sda                    8:0    0   2.5G  0 disk  
├─sda1                 8:1    0     2G  0 part  
│ └─md0                9:0    0     2G  0 raid1 
│   └─vg--all-lv100M 253:0    0   100M  0 lvm   /tmp/new
└─sda2                 8:2    0   511M  0 part  
  └─md1                9:1    0  1018M  0 raid0 
sdb                    8:16   0   2.5G  0 disk  
├─sdb1                 8:17   0     2G  0 part  
│ └─md0                9:0    0     2G  0 raid1 
│   └─vg--all-lv100M 253:0    0   100M  0 lvm   /tmp/new
└─sdb2                 8:18   0   511M  0 part  
  └─md1                9:1    0  1018M  0 raid0 
vda                  252:0    0   128G  0 disk  
├─vda1               252:1    0   487M  0 part  /boot
├─vda2               252:2    0   1.9G  0 part  [SWAP]
└─vda3               252:3    0 125.6G  0 part  /
```

## 17. Сделайте `--fail` на устройство в вашем RAID1 md.

```
vagrant@u20fs:~$ sudo mdadm /dev/md0 -f /dev/sdb1
mdadm: set /dev/sdb1 faulty in /dev/md0
vagrant@u20fs:~$ sudo mdadm -D /dev/md0
/dev/md0:
           Version : 1.2
     Creation Time : Tue Jan 25 09:13:26 2022
        Raid Level : raid1
        Array Size : 2094080 (2045.00 MiB 2144.34 MB)
     Used Dev Size : 2094080 (2045.00 MiB 2144.34 MB)
      Raid Devices : 2
     Total Devices : 2
       Persistence : Superblock is persistent

       Update Time : Tue Jan 25 11:26:47 2022
             State : clean, degraded 
    Active Devices : 1
   Working Devices : 1
    Failed Devices : 1
     Spare Devices : 0

Consistency Policy : resync

              Name : u20fs:0  (local to host u20fs)
              UUID : 49711e16:cab80c2e:1d12d88f:f26648cc
            Events : 21

    Number   Major   Minor   RaidDevice State
       0       8        1        0      active sync   /dev/sda1
       -       0        0        1      removed

       1       8       17        -      faulty   /dev/sdb1
```

## 18. Подтвердите выводом `dmesg`, что RAID1 работает в деградированном состоянии.

```
vagrant@u20fs:~$ dmesg -T | grep raid1
...
[Tue Jan 25 11:26:51 2022] md/raid1:md0: Disk failure on sdb1, disabling device.
                           md/raid1:md0: Operation continuing on 1 devices.
```

## 19. Протестируйте целостность файла, несмотря на "сбойный" диск он должен продолжать быть доступен.

Файл по-прежнему цел и доступен.
```
vagrant@u20fs:~$ gzip -t /tmp/new/test.gz
vagrant@u20fs:~$ echo $?
0
```

## 20. Погасите тестовый хост, `vagrant destroy`.

```
# vagrant destroy
    default: Are you sure you want to destroy the 'default' VM? [y/N] y
==> default: Destroying VM and associated drives...
```
