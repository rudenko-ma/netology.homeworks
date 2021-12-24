# Домашнее задание к занятию «2.4. Инструменты Git»

Для выполнения заданий в этом разделе давайте склонируем репозиторий с исходным кодом 
терраформа https://github.com/hashicorp/terraform 

В виде результата напишите текстом ответы на вопросы и каким образом эти ответы были получены. 

## 1. Найдите полный хеш и комментарий коммита, хеш которого начинается на `aefea`.

Хэш: `aefead2207ef7e2aa5dc81a34aedf0cad4c32545`

Комментарий: `Update CHANGELOG.md`

```
# git show --summary --format="%H %B" aefea
aefead2207ef7e2aa5dc81a34aedf0cad4c32545 Update CHANGELOG.md
```

## 2. Какому тегу соответствует коммит `85024d3`?

Коммит `85024d3` соответствует тегу `v0.12.23`.

```
# git show --summary --oneline 85024d3
85024d310 (tag: v0.12.23) v0.12.23
```

## 3. Сколько родителей у коммита `b8d720`? Напишите их хеши.

У мерж-коммита `b8d720` два родителя.

Хэш первого: `56cd7859e05c36c06b56d013b55a252d0bb7e158`

Хэш второго: `9ea88f22fc6269854151c571162c5bcf958bee2b`

```
# git show --summary --format=%P b8d720
56cd7859e05c36c06b56d013b55a252d0bb7e158 9ea88f22fc6269854151c571162c5bcf958bee2b
```

## 4. Перечислите хеши и комментарии всех коммитов которые были сделаны между тегами v0.12.23 и v0.12.24.

Коммиты между тегами v0.12.23 и v0.12.24 (не включая их):
1. `b14b74c4939dcab573326f4e3ee2a62e23e12f89` [Website] vmc provider links
1. `3f235065b9347a758efadc92295b540ee0a5e26e` Update CHANGELOG.md
1. `6ae64e247b332925b872447e9ce869657281c2bf` registry: Fix panic when server is unreachable
Non-HTTP errors previously resulted in a panic due to dereferencing the
resp pointer while it was nil, as part of rendering the error message.
This commit changes the error message formatting to cope with a nil
response, and extends test coverage.
Fixes #24384
5c619ca1baf2e21a155fcdb4c264cc9e24a2a353 website: Remove links to the getting started guide's old location
Since these links were in the soon-to-be-deprecated 0.11 language section, I
think we can just remove them without needing to find an equivalent link.
1. `06275647e2b53d97d4f0a19a0fec11f6d69820b5` Update CHANGELOG.md
1. `d5f9411f5108260320064349b757f55c09bc4b80` command: Fix bug when using terraform login on Windows
1. `4b6d06cc5dcb78af637bbb19c198faff37a066ed` Update CHANGELOG.md
1. `dd01a35078f040ca984cdd349f18d0b67e486c35` Update CHANGELOG.md
1. `225466bc3e5f35baa5d07197bbc079345b77525e` Cleanup after v0.12.23 release

Сначала получаем хеш коммита с тегом `v0.12.24`

```
# git show --summary --oneline v0.12.24
tag v0.12.24

v0.12.24
-----BEGIN PGP SIGNATURE-----
Version: GnuPG v1

iQEcBAABAgAGBQJec4nlAAoJEFGFLYc0j/xMSvoIAK0z57IgGyIs8ghpFaksZkRl
XJOrZjP1szlXRMAoMNkef46VUDNjrdPBo+xSHuRxbxFpC2vQwqtwA3Dk8W/KaX5F
AkJXqtWlpyZiWrNMWsXt0AN8CjiaIF5zgrIWvpawGbPU6APOC6FpQiG8WFUobX9p
yRKMOTARAYO1bNgSr8Tgtvv2djRl3PIe6Im9/qyi7S2cFCV9ql8nRLBMPPvZ5xzr
3gehdozVGSJ2C1rI0R3DXAu+q9W6KZsZOhBEsBb/2X/M9chiH6JDbT7bvvgXX34P
gyvcohmWnVwm5Oaurco1hdZFipN+qGMc3EEB3sqoSW0ASTmjocYr44hT3O7/iD0=
=UdsJ
-----END PGP SIGNATURE-----
33ff1c03b (tag: v0.12.24) v0.12.24
```

Затем получаем список всех комитов между тегами, убираем пустые строки и последний коммит по хешу.

```
# git show --summary --format="%H %B" v0.12.23..v0.12.24 | grep -vE "^$|^33ff1c03b"
b14b74c4939dcab573326f4e3ee2a62e23e12f89 [Website] vmc provider links
3f235065b9347a758efadc92295b540ee0a5e26e Update CHANGELOG.md
6ae64e247b332925b872447e9ce869657281c2bf registry: Fix panic when server is unreachable
Non-HTTP errors previously resulted in a panic due to dereferencing the
resp pointer while it was nil, as part of rendering the error message.
This commit changes the error message formatting to cope with a nil
response, and extends test coverage.
Fixes #24384
5c619ca1baf2e21a155fcdb4c264cc9e24a2a353 website: Remove links to the getting started guide's old location
Since these links were in the soon-to-be-deprecated 0.11 language section, I
think we can just remove them without needing to find an equivalent link.
06275647e2b53d97d4f0a19a0fec11f6d69820b5 Update CHANGELOG.md
d5f9411f5108260320064349b757f55c09bc4b80 command: Fix bug when using terraform login on Windows
4b6d06cc5dcb78af637bbb19c198faff37a066ed Update CHANGELOG.md
dd01a35078f040ca984cdd349f18d0b67e486c35 Update CHANGELOG.md
225466bc3e5f35baa5d07197bbc079345b77525e Cleanup after v0.12.23 release
```

## 5. Найдите коммит в котором была создана функция `func providerSource`, ее определение в коде выглядит так `func providerSource(...)` (вместо троеточего перечислены аргументы).

Функция `func providerSource` была создана в коммите `8c928e83589d90a031f811fae52a81be7153e82f`.

```
# git log -S "func providerSource("
commit 8c928e83589d90a031f811fae52a81be7153e82f
Author: Martin Atkins <mart@degeneration.co.uk>
Date:   Thu Apr 2 18:04:39 2020 -0700

    main: Consult local directories as potential mirrors of providers
    
    This restores some of the local search directories we used to include when
    searching for provider plugins in Terraform 0.12 and earlier. The
    directory structures we are expecting in these are different than before,
    so existing directory contents will not be compatible without
    restructuring, but we need to retain support for these local directories
    so that users can continue to sideload third-party provider plugins until
    the explicit, first-class provider mirrors configuration (in CLI config)
    is implemented, at which point users will be able to override these to
    whatever directories they want.
    
    This also includes some new search directories that are specific to the
    operating system where Terraform is running, following the documented
    layout conventions of that platform. In particular, this follows the
    XDG Base Directory specification on Unix systems, which has been a
    somewhat-common request to better support "sideloading" of packages via
    standard Linux distribution package managers and other similar mechanisms.
    While it isn't strictly necessary to add that now, it seems ideal to do
    all of the changes to our search directory layout at once so that our
    documentation about this can cleanly distinguish "0.12 and earlier" vs.
    "0.13 and later", rather than having to document a complex sequence of
    smaller changes.
    
    Because this behavior is a result of the integration of package main with
    package command, this behavior is verified using an e2etest rather than
    a unit test. That test, TestInitProvidersVendored, is also fixed here to
    create a suitable directory structure for the platform where the test is
    being run. This fixes TestInitProvidersVendored.

```

## 6. Найдите все коммиты в которых была изменена функция `globalPluginDirs`.

Коммиты, в которых была изменена функция:
1. `78b122055` Remove config.go and update things using its aliases
1. `52dbf9483` keep .terraform.d/plugins for discovery
1. `41ab0aef7` Add missing OS_ARCH dir to global plugin paths
1. `66ebff90c` move some more plugin search path logic to command
1. `8364383c3` Push plugin discovery down into command package

Сначала находим файл в котором определена функция.

```
# git grep -p "globalPluginDirs("
commands.go=func initCommands(
commands.go:            GlobalPluginDirs: globalPluginDirs(),
commands.go=func credentialsSource(config *cliconfig.Config) (auth.CredentialsSource, error) {
commands.go:    helperPlugins := pluginDiscovery.FindPlugins("credentials", globalPluginDirs())
plugins.go=import (
plugins.go:func globalPluginDirs() []string {

```

Затем ищем комиты затрагивающие эту функцию.

```
#  git log -L :globalPluginDirs:plugins.go --no-patch --oneline
78b122055 Remove config.go and update things using its aliases
52dbf9483 keep .terraform.d/plugins for discovery
41ab0aef7 Add missing OS_ARCH dir to global plugin paths
66ebff90c move some more plugin search path logic to command
8364383c3 Push plugin discovery down into command package
```

## 7. Кто автор функции `synchronizedWriters`?

Автор функции `synchronizedWriters` : Martin Atkins

Находим все коммиты затрагивающие определенение функции, выводим только имя автора и оставляем последнюю строку.

```
git log -S "func synchronizedWriters" --format="%an" | tail -n1
Martin Atkins
```