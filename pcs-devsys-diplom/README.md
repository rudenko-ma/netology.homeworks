# Курсовая работа по итогам модуля "DevOps и системное администрирование"

## Процесс установки и настройки ufw

```bash
vagrant@diplom:~$ sudo apt install ufw
Reading package lists... Done
Building dependency tree       
Reading state information... Done
ufw is already the newest version (0.36-6ubuntu1).
0 upgraded, 0 newly installed, 0 to remove and 76 not upgraded.
vagrant@diplom:~$ sudo ufw allow 22/tcp
Rules updated
Rules updated (v6)
vagrant@diplom:~$ sudo ufw allow 443/tcp
Rules updated
Rules updated (v6)
vagrant@diplom:~$ sudo ufw enable
Command may disrupt existing ssh connections. Proceed with operation (y|n)? y
Firewall is active and enabled on system startup
vagrant@diplom:~$ sudo ufw status verbose
Status: active
Logging: on (low)
Default: deny (incoming), allow (outgoing), disabled (routed)
New profiles: skip

To                         Action      From
--                         ------      ----
22/tcp                     ALLOW IN    Anywhere                  
443/tcp                    ALLOW IN    Anywhere                  
22/tcp (v6)                ALLOW IN    Anywhere (v6)             
443/tcp (v6)               ALLOW IN    Anywhere (v6)
```

## Процесс установки и выпуска сертификата с помощью hashicorp vault

<details>
  <summary>Установим vault согласно инструкции</summary>

  ```shell
vagrant@diplom:~$ curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo apt-key add -
OK
vagrant@diplom:~$ sudo apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main"
Get:1 https://apt.releases.hashicorp.com focal InRelease [14.6 kB]
Get:2 http://security.ubuntu.com/ubuntu focal-security InRelease [114 kB]
Get:3 https://apt.releases.hashicorp.com focal/main amd64 Packages [50.1 kB]
Hit:4 http://us.archive.ubuntu.com/ubuntu focal InRelease
Get:5 http://us.archive.ubuntu.com/ubuntu focal-updates InRelease [114 kB]
Get:6 http://security.ubuntu.com/ubuntu focal-security/main i386 Packages [395 kB]
Get:7 http://security.ubuntu.com/ubuntu focal-security/main amd64 Packages [1310 kB]
Get:8 http://security.ubuntu.com/ubuntu focal-security/main Translation-en [228 kB]
Get:9 http://security.ubuntu.com/ubuntu focal-security/main amd64 c-n-f Metadata [9732 B]
Get:10 http://security.ubuntu.com/ubuntu focal-security/restricted amd64 Packages [799 kB]
Get:11 http://security.ubuntu.com/ubuntu focal-security/restricted Translation-en [114 kB]
Get:12 http://us.archive.ubuntu.com/ubuntu focal-backports InRelease [108 kB]
Get:13 http://us.archive.ubuntu.com/ubuntu focal-updates/main amd64 Packages [1640 kB]
Get:14 http://us.archive.ubuntu.com/ubuntu focal-updates/main i386 Packages [615 kB]
Get:15 http://us.archive.ubuntu.com/ubuntu focal-updates/main Translation-en [312 kB]
Get:16 http://us.archive.ubuntu.com/ubuntu focal-updates/main amd64 c-n-f Metadata [14.8 kB]
Get:17 http://us.archive.ubuntu.com/ubuntu focal-updates/restricted amd64 Packages [853 kB]
Get:18 http://us.archive.ubuntu.com/ubuntu focal-updates/restricted Translation-en [122 kB]
Get:19 http://us.archive.ubuntu.com/ubuntu focal-updates/universe amd64 Packages [909 kB]
Get:20 http://us.archive.ubuntu.com/ubuntu focal-updates/universe i386 Packages [672 kB]
Get:21 http://us.archive.ubuntu.com/ubuntu focal-updates/multiverse amd64 Packages [23.8 kB]
Get:22 http://us.archive.ubuntu.com/ubuntu focal-updates/multiverse i386 Packages [8464 B]
Fetched 8425 kB in 11s (761 kB/s)
Reading package lists... Done
vagrant@diplom:~$ sudo apt-get update && sudo apt-get install vault
Hit:1 http://security.ubuntu.com/ubuntu focal-security InRelease
Hit:2 http://us.archive.ubuntu.com/ubuntu focal InRelease
Hit:3 http://us.archive.ubuntu.com/ubuntu focal-updates InRelease
Hit:4 http://us.archive.ubuntu.com/ubuntu focal-backports InRelease
Hit:5 https://apt.releases.hashicorp.com focal InRelease
Reading package lists... Done
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following NEW packages will be installed:
  vault
0 upgraded, 1 newly installed, 0 to remove and 77 not upgraded.
Need to get 69.6 MB of archives.
After this operation, 188 MB of additional disk space will be used.
Get:1 https://apt.releases.hashicorp.com focal/main amd64 vault amd64 1.9.4 [69.6 MB]
Fetched 69.6 MB in 24s (2902 kB/s)
Selecting previously unselected package vault.
(Reading database ... 111201 files and directories currently installed.)
Preparing to unpack .../archives/vault_1.9.4_amd64.deb ...
Unpacking vault (1.9.4) ...
Setting up vault (1.9.4) ...
Generating Vault TLS key and self-signed certificate...
Generating a RSA private key
............................................................................................................................................................................................................................................................................................................................................................++++
..............................................................................................................................................++++
writing new private key to 'tls.key'
-----
Vault TLS key and self-signed certificate have been generated in '/opt/vault/tls'.
vagrant@diplom:~$ vault --version
Vault v1.9.4 (fcbe948b2542a13ee8036ad07dd8ebf8554f56cb)
  ```
</details>

<details>
  <summary>Запустим сервер в отдельном терминале</summary>

  ```shell
  vagrant@diplom:~$ vault server -dev -dev-root-token-id root
==> Vault server configuration:

             Api Address: http://127.0.0.1:8200
                     Cgo: disabled
         Cluster Address: https://127.0.0.1:8201
              Go Version: go1.17.7
              Listener 1: tcp (addr: "127.0.0.1:8200", cluster address: "127.0.0.1:8201", max_request_duration: "1m30s", max_request_size: "33554432", tls: "disabled")
               Log Level: info
                   Mlock: supported: true, enabled: false
           Recovery Mode: false
                 Storage: inmem
                 Version: Vault v1.9.4
             Version Sha: fcbe948b2542a13ee8036ad07dd8ebf8554f56cb

==> Vault server started! Log data will stream in below:

2022-03-09T03:50:14.418Z [INFO]  proxy environment: http_proxy="" https_proxy="" no_proxy=""
2022-03-09T03:50:14.418Z [WARN]  no `api_addr` value specified in config or in VAULT_API_ADDR; falling back to detection if possible, but this value should be manually set
2022-03-09T03:50:14.419Z [INFO]  core: Initializing VersionTimestamps for core
2022-03-09T03:50:14.421Z [INFO]  core: security barrier not initialized
2022-03-09T03:50:14.422Z [INFO]  core: security barrier initialized: stored=1 shares=1 threshold=1
2022-03-09T03:50:14.422Z [INFO]  core: post-unseal setup starting
2022-03-09T03:50:14.424Z [INFO]  core: loaded wrapping token key
2022-03-09T03:50:14.424Z [INFO]  core: Recorded vault version: vault version=1.9.4 upgrade time="2022-03-09 03:50:14.424796027 +0000 UTC m=+0.059473166"
2022-03-09T03:50:14.425Z [INFO]  core: successfully setup plugin catalog: plugin-directory=""
2022-03-09T03:50:14.425Z [INFO]  core: no mounts; adding default mount table
2022-03-09T03:50:14.427Z [INFO]  core: successfully mounted backend: type=cubbyhole path=cubbyhole/
2022-03-09T03:50:14.428Z [INFO]  core: successfully mounted backend: type=system path=sys/
2022-03-09T03:50:14.428Z [INFO]  core: successfully mounted backend: type=identity path=identity/
2022-03-09T03:50:14.432Z [INFO]  core: successfully enabled credential backend: type=token path=token/
2022-03-09T03:50:14.433Z [INFO]  core: restoring leases
2022-03-09T03:50:14.433Z [INFO]  expiration: lease restore complete
2022-03-09T03:50:14.433Z [INFO]  rollback: starting rollback manager
2022-03-09T03:50:14.433Z [INFO]  identity: entities restored
2022-03-09T03:50:14.434Z [INFO]  identity: groups restored
2022-03-09T03:50:14.434Z [INFO]  core: post-unseal setup complete
2022-03-09T03:50:14.434Z [INFO]  core: root token generated
2022-03-09T03:50:14.434Z [INFO]  core: pre-seal teardown starting
2022-03-09T03:50:14.434Z [INFO]  rollback: stopping rollback manager
2022-03-09T03:50:14.434Z [INFO]  core: pre-seal teardown complete
2022-03-09T03:50:14.434Z [INFO]  core.cluster-listener.tcp: starting listener: listener_address=127.0.0.1:8201
2022-03-09T03:50:14.434Z [INFO]  core.cluster-listener: serving cluster requests: cluster_listen_address=127.0.0.1:8201
2022-03-09T03:50:14.434Z [INFO]  core: post-unseal setup starting
2022-03-09T03:50:14.434Z [INFO]  core: loaded wrapping token key
2022-03-09T03:50:14.434Z [INFO]  core: successfully setup plugin catalog: plugin-directory=""
2022-03-09T03:50:14.435Z [INFO]  core: successfully mounted backend: type=system path=sys/
2022-03-09T03:50:14.435Z [INFO]  core: successfully mounted backend: type=identity path=identity/
2022-03-09T03:50:14.435Z [INFO]  core: successfully mounted backend: type=cubbyhole path=cubbyhole/
2022-03-09T03:50:14.436Z [INFO]  core: successfully enabled credential backend: type=token path=token/
2022-03-09T03:50:14.436Z [INFO]  core: restoring leases
2022-03-09T03:50:14.436Z [INFO]  identity: entities restored
2022-03-09T03:50:14.436Z [INFO]  identity: groups restored
2022-03-09T03:50:14.436Z [INFO]  core: post-unseal setup complete
2022-03-09T03:50:14.436Z [INFO]  core: vault is unsealed
2022-03-09T03:50:14.438Z [INFO]  expiration: revoked lease: lease_id=auth/token/root/hba682b434092765345b1928e2b124248cab3edc096a841f71fb6c47d76cbef54
2022-03-09T03:50:14.440Z [INFO]  core: successful mount: namespace="" path=secret/ type=kv
2022-03-09T03:50:14.445Z [INFO]  expiration: lease restore complete
2022-03-09T03:50:14.446Z [INFO]  secrets.kv.kv_898691b9: collecting keys to upgrade
2022-03-09T03:50:14.446Z [INFO]  secrets.kv.kv_898691b9: done collecting keys: num_keys=1
2022-03-09T03:50:14.446Z [INFO]  secrets.kv.kv_898691b9: upgrading keys finished
2022-03-09T03:50:14.449Z [INFO]  rollback: starting rollback manager
WARNING! dev mode is enabled! In this mode, Vault runs entirely in-memory
and starts unsealed with a single unseal key. The root token is already
authenticated to the CLI, so you can immediately begin using Vault.

You may need to set the following environment variable:

    $ export VAULT_ADDR='http://127.0.0.1:8200'

The unseal key and root token are displayed below in case you want to
seal/unseal the Vault or re-authenticate.

Unseal Key: 7N9yUVE6lLmulU/ANbhF03wKueWfjcFyXzGNwNOMYfc=
Root Token: root

Development mode should NOT be used in production installations!
  ```
</details>

<details>
  <summary>Генерируем корневой сертификат</summary>

  ```shell
vagrant@diplom:~$ export VAULT_ADDR=http://127.0.0.1:8200
vagrant@diplom:~$ export VAULT_TOKEN=root
vagrant@diplom:~$ vault secrets enable pki
Success! Enabled the pki secrets engine at: pki/
vagrant@diplom:~$ vault secrets tune -max-lease-ttl=87600h pki
Success! Tuned the secrets engine at: pki/
vagrant@diplom:~$ vault write -field=certificate pki/root/generate/internal common_name="diplom.dev" tt
vagrant@diplom:~$ vault write pki/config/urls \
>      issuing_certificates="$VAULT_ADDR/v1/pki/ca" \
>      crl_distribution_points="$VAULT_ADDR/v1/pki/crl"
Success! Data written to: pki/config/urls

  ```
</details>

<details>
  <summary>Генерируем промежуточный сертификат</summary>

  ```shell
vagrant@diplom:~$ sudo apt install jq
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following additional packages will be installed:
  libjq1 libonig5
The following NEW packages will be installed:
  jq libjq1 libonig5
0 upgraded, 3 newly installed, 0 to remove and 77 not upgraded.
Need to get 313 kB of archives.
After this operation, 1062 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://us.archive.ubuntu.com/ubuntu focal/universe amd64 libonig5 amd64 6.9.4-1 [142 kB]
Get:2 http://us.archive.ubuntu.com/ubuntu focal-updates/universe amd64 libjq1 amd64 1.6-1ubuntu0.20.04.1 [121 kB]
Get:3 http://us.archive.ubuntu.com/ubuntu focal-updates/universe amd64 jq amd64 1.6-1ubuntu0.20.04.1 [50.2 kB]
Fetched 313 kB in 8s (38.5 kB/s)
Selecting previously unselected package libonig5:amd64.
(Reading database ... 111207 files and directories currently installed.)
Preparing to unpack .../libonig5_6.9.4-1_amd64.deb ...
Unpacking libonig5:amd64 (6.9.4-1) ...
Selecting previously unselected package libjq1:amd64.
Preparing to unpack .../libjq1_1.6-1ubuntu0.20.04.1_amd64.deb ...
Unpacking libjq1:amd64 (1.6-1ubuntu0.20.04.1) ...
Selecting previously unselected package jq.
Preparing to unpack .../jq_1.6-1ubuntu0.20.04.1_amd64.deb ...
Unpacking jq (1.6-1ubuntu0.20.04.1) ...
Setting up libonig5:amd64 (6.9.4-1) ...
Setting up libjq1:amd64 (1.6-1ubuntu0.20.04.1) ...
Setting up jq (1.6-1ubuntu0.20.04.1) ...
Processing triggers for man-db (2.9.1-1) ...
Processing triggers for libc-bin (2.31-0ubuntu9.2) ...
vagrant@diplom:~$ vault secrets enable -path=pki_int pki
Success! Enabled the pki secrets engine at: pki_int/
vagrant@diplom:~$ vault secrets tune -max-lease-ttl=43800h pki_int
Success! Tuned the secrets engine at: pki_int/
vagrant@diplom:~$ vault write -format=json pki_int/intermediate/generate/internal \
>      common_name="diplom.dev Intermediate Authority" \
>      | jq -r '.data.csr' > pki_intermediate.csr
vagrant@diplom:~$ vault write -format=json pki/root/sign-intermediate csr=@pki_intermediate.csr \
>      format=pem_bundle ttl="43800h" \
>      | jq -r '.data.certificate' > intermediate.cert.pem
vagrant@diplom:~$ vault write pki_int/intermediate/set-signed certificate=@intermediate.cert.pem
Success! Data written to: pki_int/intermediate/set-signed
  ```
</details>


<details>
  <summary></summary>

  ```shell
  ```
</details>


## Процесс установки и настройки сервера nginx

## Страница сервера nginx в браузере хоста не содержит предупреждений

## Скрипт генерации нового сертификата работает (сертификат сервера ngnix должен быть "зеленым")

## Crontab работает (выберите число и время так, чтобы показать что crontab запускается и делает что надо)

