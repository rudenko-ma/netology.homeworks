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
  <summary>Создаем роль</summary>

  ```shell
vagrant@diplom:~$ vault write pki_int/roles/diplom-dev \
>      allowed_domains="diplom.dev" \
>      allow_bare_domains=true \
>      alt_names="diplom.dev,localhost" \
>      allow_subdomains=true \
>      max_ttl="720h"
Success! Data written to: pki_int/roles/diplom-dev
  ```
</details>

<details>
  <summary>Запрашиваем данные сертификата сайта, сохраняем данные в файл в формате JSON и формируем файлы сертификата и ключа</summary>

  ```shell
vagrant@diplom:~$ vault write --format=json pki_int/issue/diplom-dev common_name="diplom.dev" ttl="720h" | tee certs.json
{
  "request_id": "04374b66-bd05-0fe3-5d5d-ef207a2ce122",
  "lease_id": "",
  "lease_duration": 0,
  "renewable": false,
  "data": {
    "ca_chain": [
      "-----BEGIN CERTIFICATE-----\nMIIDpDCCAoygAwIBAgIUK/gha/tVm5QDQnqR2NqQ6dJFLnowDQYJKoZIhvcNAQEL\nBQAwFTETMBEGA1UEAxMKZGlwbG9tLmRldjAeFw0yMjAzMTAwNDQzNDVaFw0yNzAz\nMDkwNDQ0MTVaMCwxKjAoBgNVBAMTIWRpcGxvbS5kZXYgSW50ZXJtZWRpYXRlIEF1\ndGhvcml0eTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBALvogE4CUmAw\nDYbI16TzC3rYbtuSsd6vYxlfX7RXw2CwNDTWo4w5ePG6dTDZp5Xo+wA4Yqk1tTcd\nH1WGALmsGIEQrKBfFwEmVcd5o/xTe+pz4SnHsVUkKhmurIZuvAUApCuRfErPr3NW\nXe4ZeDPy/jKMJWFNPzWKWLyDlOBtb3ch5shGdkd0C24y2fioUcPGFgUKyx+vEZkK\ndAoz45NjMgtUOrUot05SBapoSnkrWhkzt/yZ2USTqmcX8c1S4jc1hY10DDPuLx/I\nwCD1eXHyEcg7e6+xmOckQBeVxizkh1haIgTcCU7ScAydpOW6rZ8GdDCYjBlAAnvQ\nQvH+YeF3sNECAwEAAaOB1DCB0TAOBgNVHQ8BAf8EBAMCAQYwDwYDVR0TAQH/BAUw\nAwEB/zAdBgNVHQ4EFgQUSwVTfEwxERKcuKKBesnViRi7ZSEwHwYDVR0jBBgwFoAU\nCBfZ+PPLqRR5sCPwbU+5r8GGdR8wOwYIKwYBBQUHAQEELzAtMCsGCCsGAQUFBzAC\nhh9odHRwOi8vMTI3LjAuMC4xOjgyMDAvdjEvcGtpL2NhMDEGA1UdHwQqMCgwJqAk\noCKGIGh0dHA6Ly8xMjcuMC4wLjE6ODIwMC92MS9wa2kvY3JsMA0GCSqGSIb3DQEB\nCwUAA4IBAQDO7ICvAWDzuu9kFtFbFjiOqYclgLKhdnIowTBPrNJhd0f5MG1pkN9R\n1uEL5YR/mGoftcWeoNGfyaE7T0F/bearr9UN4bd51yVTq9Ay0IWaBs8nnkgAPEpr\n0HE0ugECzVftdguBgmcVs9aYxSaRyV7HcOlhzjTWplgxds6WzhOFNZMLaiRTy/FO\niFdJzbwR/sMltU3gsEn5MmZd/1HDjpjYXBz5ic24MN+bGKr1JgZeFzBvsGuhDqAg\nt0SR08lvlj8lZSPcj/xL7R8yaOSWFkOsVPQeyyP3vZjM/bHh54MgqcgttV8BMi7X\nyo9ONJ6Cddgxuyb/bshBNkLsZHtNNbWY\n-----END CERTIFICATE-----"
    ],
    "certificate": "-----BEGIN CERTIFICATE-----\nMIIDWTCCAkGgAwIBAgIUIgOclPfyvc84JJOz5GzB79jCyA8wDQYJKoZIhvcNAQEL\nBQAwLDEqMCgGA1UEAxMhZGlwbG9tLmRldiBJbnRlcm1lZGlhdGUgQXV0aG9yaXR5\nMB4XDTIyMDMxNjEwMzQwOVoXDTIyMDQxNTEwMzQzOVowFTETMBEGA1UEAxMKZGlw\nbG9tLmRldjCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAKOVSZfRUcHz\niAbGL3jU5qM91xxwC+dylVGJsxqL9ZMEC2aJjRW5PtMWHGF9KSpwxgMjFT8nlhKD\n276pQOmsCij/P6EUB4ZtYKgOfo23EJkuEgOw3boFqpP72VxedO+CsD0TgksuYkKS\nYO+bvk7bihoOqlFEyOo9mxCP/lQbt7s+2MWqsXhXv/ZR1QtmEfh1Upz+g6T0bRV4\nxwKOKipa3BNxQibuXgpdMmdGpSnnMRnJW8Ez2TswtQzNX4drNZTFi0kTbzfE6kjD\nV2llVrd+Zsgx2MM2jf+8QvTWznZYkk76dneFxy2oSPL7I1PtTprBTKEmkVAmwUoR\nmMsXHocMfU8CAwEAAaOBiTCBhjAOBgNVHQ8BAf8EBAMCA6gwHQYDVR0lBBYwFAYI\nKwYBBQUHAwEGCCsGAQUFBwMCMB0GA1UdDgQWBBQyHYiJOIIcYEKGYPwMehIyM6EL\nEDAfBgNVHSMEGDAWgBRLBVN8TDEREpy4ooF6ydWJGLtlITAVBgNVHREEDjAMggpk\naXBsb20uZGV2MA0GCSqGSIb3DQEBCwUAA4IBAQBnzfqgtl0S3FriIg1FJEowZQLW\nbbOrzSa6WYrSe4REPK2I9D6jG0pdp/hz7my+CCf2GQf+9i5d0vat0+K+hRG7xbtx\n9ucTJ8+tsCtxvCWXKO1mrHy3Y/yUWLfr4s/ThqlyyaMk/0FQHS/t8zlA3nfveGtO\nTMDFuIvEJsFnPcx/5feQpKQyq4GF85Sh3CDRT7scCIvXq3GjueOEhp73XbrGWfDj\nyXLR8y9ccjlfOL/22KwN2/2NkNBeDd7gvX5UW9+uWLlL9kYBDKKOWrRlB4FfDGLF\nxUSjdvNvjmYG9uYbrLHeE6Wwa1Birux/oXjL/1ETkUukQhJ0E3NfN5IZFwir\n-----END CERTIFICATE-----",
    "expiration": 1650018879,
    "issuing_ca": "-----BEGIN CERTIFICATE-----\nMIIDpDCCAoygAwIBAgIUK/gha/tVm5QDQnqR2NqQ6dJFLnowDQYJKoZIhvcNAQEL\nBQAwFTETMBEGA1UEAxMKZGlwbG9tLmRldjAeFw0yMjAzMTAwNDQzNDVaFw0yNzAz\nMDkwNDQ0MTVaMCwxKjAoBgNVBAMTIWRpcGxvbS5kZXYgSW50ZXJtZWRpYXRlIEF1\ndGhvcml0eTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBALvogE4CUmAw\nDYbI16TzC3rYbtuSsd6vYxlfX7RXw2CwNDTWo4w5ePG6dTDZp5Xo+wA4Yqk1tTcd\nH1WGALmsGIEQrKBfFwEmVcd5o/xTe+pz4SnHsVUkKhmurIZuvAUApCuRfErPr3NW\nXe4ZeDPy/jKMJWFNPzWKWLyDlOBtb3ch5shGdkd0C24y2fioUcPGFgUKyx+vEZkK\ndAoz45NjMgtUOrUot05SBapoSnkrWhkzt/yZ2USTqmcX8c1S4jc1hY10DDPuLx/I\nwCD1eXHyEcg7e6+xmOckQBeVxizkh1haIgTcCU7ScAydpOW6rZ8GdDCYjBlAAnvQ\nQvH+YeF3sNECAwEAAaOB1DCB0TAOBgNVHQ8BAf8EBAMCAQYwDwYDVR0TAQH/BAUw\nAwEB/zAdBgNVHQ4EFgQUSwVTfEwxERKcuKKBesnViRi7ZSEwHwYDVR0jBBgwFoAU\nCBfZ+PPLqRR5sCPwbU+5r8GGdR8wOwYIKwYBBQUHAQEELzAtMCsGCCsGAQUFBzAC\nhh9odHRwOi8vMTI3LjAuMC4xOjgyMDAvdjEvcGtpL2NhMDEGA1UdHwQqMCgwJqAk\noCKGIGh0dHA6Ly8xMjcuMC4wLjE6ODIwMC92MS9wa2kvY3JsMA0GCSqGSIb3DQEB\nCwUAA4IBAQDO7ICvAWDzuu9kFtFbFjiOqYclgLKhdnIowTBPrNJhd0f5MG1pkN9R\n1uEL5YR/mGoftcWeoNGfyaE7T0F/bearr9UN4bd51yVTq9Ay0IWaBs8nnkgAPEpr\n0HE0ugECzVftdguBgmcVs9aYxSaRyV7HcOlhzjTWplgxds6WzhOFNZMLaiRTy/FO\niFdJzbwR/sMltU3gsEn5MmZd/1HDjpjYXBz5ic24MN+bGKr1JgZeFzBvsGuhDqAg\nt0SR08lvlj8lZSPcj/xL7R8yaOSWFkOsVPQeyyP3vZjM/bHh54MgqcgttV8BMi7X\nyo9ONJ6Cddgxuyb/bshBNkLsZHtNNbWY\n-----END CERTIFICATE-----",
    "private_key": "-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEAo5VJl9FRwfOIBsYveNTmoz3XHHAL53KVUYmzGov1kwQLZomN\nFbk+0xYcYX0pKnDGAyMVPyeWEoPbvqlA6awKKP8/oRQHhm1gqA5+jbcQmS4SA7Dd\nugWqk/vZXF5074KwPROCSy5iQpJg75u+TtuKGg6qUUTI6j2bEI/+VBu3uz7Yxaqx\neFe/9lHVC2YR+HVSnP6DpPRtFXjHAo4qKlrcE3FCJu5eCl0yZ0alKecxGclbwTPZ\nOzC1DM1fh2s1lMWLSRNvN8TqSMNXaWVWt35myDHYwzaN/7xC9NbOdliSTvp2d4XH\nLahI8vsjU+1OmsFMoSaRUCbBShGYyxcehwx9TwIDAQABAoIBAGoL/9eR9USdEhQC\nKwhUTOiK0Ic5BB6ZI7/mWtvc2+jg+FsS1Qm+O8IwVVnGAAfpcBTci4uTqDB8ltp1\ncwWJaFTHlIJiL7av9bc9HkHU6cfEHB2UbUmJHtosrO66tWgH+yS9HvyKJ10s8/ah\nqrAIlvDpjPR+eRmRspL8Jk50YZnazJlsPXyGAb2v3hJChVAPsnfuFE6hVLy+6Lzy\n2GhP2kGPfpfptP8sZw7NVaOPVbr3Ktrg4bZoYlXESXqLfD5lHlmM105YscKkg4Jd\nQZDnKgsHrh3Ovam3or+2xpmcw1ELPMDnXDXw5mMYfYQIq5UHQCgLDWkCYr4VxOVt\nuuCEJzECgYEA1wVph3lFA/MUnsH+frUOCP837kFei6q7CohWSaWSbOXaraK298+Y\nB4oepHuS/iN5Bkzuhuz+Ld+jfTx+biSTZLN9LRRA7+fJJxS626lHvyOWpUFB7mw2\n03fIgxCcOWVSwkPr6enEqLdKlStEsgUeSdL2nc5rnVR3/QoQGEyh5mUCgYEAwsJJ\nPqvdJ2nLtHK8bdp4FWCZ9Qijd0JMzyUzZd5O9/LgiVAFhtWX5wJkPjtz35p3rnZ6\nS1UKseV698M5eqZbaLE2eLwbDJFcS5jPVUlhMHUHzFRvBEvGDOD8X2yDIq8rCYi3\nfbeAApf7s6um9oXt44+1HkyyF3WpyXr+wWc9b6MCgYAwbs2ocE51Z0mbwQK8M7gn\nmqVUi3DqcNiUtMUK7bqfwN6TAfXIt//8osXoMtWXXRIjsyx/Q961IozG5ttrn917\nb1qgztEZuNH8dZTpaaX5jeCe9KYPOFzZIUAPFay62PHdRENdewSLJE4ub4KXvsNl\nyZk3Tom69I3ad2vMrWZCaQKBgEbCliAKC1DdlGBca2+yN3z02xr254VV9lgwmOsD\nCUf223OoOknR4t3QtaESsrfkBGXDsA0cucUGrlXEfWa9eGqiMDtPhLhdO95Ph8zh\n20jizFGFv8wcx7k4KRl2cHKyl/1fyeMIP58xnwaZcBETeen69YArt2zkmCqW4GZe\nXyjnAoGBAJt3/+avLjmICSyRpaX/lhvOZ+Ew6X940jdsa19OvkHqDu8aLd3cqZHs\nfzaWZguKm9TpJPNU7eZmu42TRC1fiGd9bNocXpYz6lu9J12tNEC9rp/s5tCkCSNd\nSjOHs6hKDncPUkeeH2ouMBijkBF1ZMbuVlwy9CR8YYvOQjr1MZWv\n-----END RSA PRIVATE KEY-----",
    "private_key_type": "rsa",
    "serial_number": "22:03:9c:94:f7:f2:bd:cf:38:24:93:b3:e4:6c:c1:ef:d8:c2:c8:0f"
  },
  "warnings": null
}
vagrant@diplom:~$ cat certs.json | jq -r .data.certificate > diplom.dev.crtvagrant@diplom:~$ ls
vagrant@diplom:~$ cat certs.json | jq -r .data.issuing_ca >> diplom.dev.crt
vagrant@diplom:~$ cat certs.json | jq -r .data.private_key > diplom.dev.key
  ```
</details>

## Процесс установки и настройки сервера nginx

<details>
  <summary>Устанавливаем NginX и проверяем его статус</summary>

  ```shell
vagrant@diplom:~$ sudo apt install nginx
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following additional packages will be installed:
  fontconfig-config fonts-dejavu-core libfontconfig1 libgd3 libjbig0 libjpeg-turbo8 libjpeg8
  libnginx-mod-http-image-filter libnginx-mod-http-xslt-filter libnginx-mod-mail libnginx-mod-stream
  libtiff5 libwebp6 libxpm4 nginx-common nginx-core
Suggested packages:
  libgd-tools fcgiwrap nginx-doc ssl-cert
The following NEW packages will be installed:
  fontconfig-config fonts-dejavu-core libfontconfig1 libgd3 libjbig0 libjpeg-turbo8 libjpeg8
  libnginx-mod-http-image-filter libnginx-mod-http-xslt-filter libnginx-mod-mail libnginx-mod-stream
  libtiff5 libwebp6 libxpm4 nginx nginx-common nginx-core
0 upgraded, 17 newly installed, 0 to remove and 77 not upgraded.
Need to get 2432 kB of archives.
After this operation, 7891 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://us.archive.ubuntu.com/ubuntu focal/main amd64 fonts-dejavu-core all 2.37-1 [1041 kB]
Get:2 http://us.archive.ubuntu.com/ubuntu focal/main amd64 fontconfig-config all 2.13.1-2ubuntu3 [28.8 kB]
Get:3 http://us.archive.ubuntu.com/ubuntu focal/main amd64 libfontconfig1 amd64 2.13.1-2ubuntu3 [114 kB]
Get:4 http://us.archive.ubuntu.com/ubuntu focal-updates/main amd64 libjpeg-turbo8 amd64 2.0.3-0ubuntu1.20.04.1 [117 kB]
Get:5 http://us.archive.ubuntu.com/ubuntu focal/main amd64 libjpeg8 amd64 8c-2ubuntu8 [2194 B]        
Get:6 http://us.archive.ubuntu.com/ubuntu focal/main amd64 libjbig0 amd64 2.1-3.1build1 [26.7 kB]     
Get:7 http://us.archive.ubuntu.com/ubuntu focal-updates/main amd64 libwebp6 amd64 0.6.1-2ubuntu0.20.04.1 [185 kB]
Get:8 http://us.archive.ubuntu.com/ubuntu focal-updates/main amd64 libtiff5 amd64 4.1.0+git191117-2ubuntu0.20.04.2 [162 kB]
Get:9 http://us.archive.ubuntu.com/ubuntu focal/main amd64 libxpm4 amd64 1:3.5.12-1 [34.0 kB]         
Get:10 http://us.archive.ubuntu.com/ubuntu focal-updates/main amd64 libgd3 amd64 2.2.5-5.2ubuntu2.1 [118 kB]
Get:11 http://us.archive.ubuntu.com/ubuntu focal-updates/main amd64 nginx-common all 1.18.0-0ubuntu1.2 [37.5 kB]
Get:12 http://us.archive.ubuntu.com/ubuntu focal-updates/main amd64 libnginx-mod-http-image-filter amd64 1.18.0-0ubuntu1.2 [14.4 kB]
Get:13 http://us.archive.ubuntu.com/ubuntu focal-updates/main amd64 libnginx-mod-http-xslt-filter amd64 1.18.0-0ubuntu1.2 [12.7 kB]
Get:14 http://us.archive.ubuntu.com/ubuntu focal-updates/main amd64 libnginx-mod-mail amd64 1.18.0-0ubuntu1.2 [42.5 kB]
Get:15 http://us.archive.ubuntu.com/ubuntu focal-updates/main amd64 libnginx-mod-stream amd64 1.18.0-0ubuntu1.2 [67.3 kB]
Get:16 http://us.archive.ubuntu.com/ubuntu focal-updates/main amd64 nginx-core amd64 1.18.0-0ubuntu1.2 [425 kB]
Get:17 http://us.archive.ubuntu.com/ubuntu focal-updates/main amd64 nginx all 1.18.0-0ubuntu1.2 [3620 B]
Fetched 2432 kB in 8s (293 kB/s)                                                                      
Preconfiguring packages ...
Selecting previously unselected package fonts-dejavu-core.
(Reading database ... 111224 files and directories currently installed.)
Preparing to unpack .../00-fonts-dejavu-core_2.37-1_all.deb ...
Unpacking fonts-dejavu-core (2.37-1) ...
Selecting previously unselected package fontconfig-config.
Preparing to unpack .../01-fontconfig-config_2.13.1-2ubuntu3_all.deb ...
Unpacking fontconfig-config (2.13.1-2ubuntu3) ...
Selecting previously unselected package libfontconfig1:amd64.
Preparing to unpack .../02-libfontconfig1_2.13.1-2ubuntu3_amd64.deb ...
Unpacking libfontconfig1:amd64 (2.13.1-2ubuntu3) ...
Selecting previously unselected package libjpeg-turbo8:amd64.
Preparing to unpack .../03-libjpeg-turbo8_2.0.3-0ubuntu1.20.04.1_amd64.deb ...
Unpacking libjpeg-turbo8:amd64 (2.0.3-0ubuntu1.20.04.1) ...
Selecting previously unselected package libjpeg8:amd64.
Preparing to unpack .../04-libjpeg8_8c-2ubuntu8_amd64.deb ...
Unpacking libjpeg8:amd64 (8c-2ubuntu8) ...
Selecting previously unselected package libjbig0:amd64.
Preparing to unpack .../05-libjbig0_2.1-3.1build1_amd64.deb ...
Unpacking libjbig0:amd64 (2.1-3.1build1) ...
Selecting previously unselected package libwebp6:amd64.
Preparing to unpack .../06-libwebp6_0.6.1-2ubuntu0.20.04.1_amd64.deb ...
Unpacking libwebp6:amd64 (0.6.1-2ubuntu0.20.04.1) ...
Selecting previously unselected package libtiff5:amd64.
Preparing to unpack .../07-libtiff5_4.1.0+git191117-2ubuntu0.20.04.2_amd64.deb ...
Unpacking libtiff5:amd64 (4.1.0+git191117-2ubuntu0.20.04.2) ...
Selecting previously unselected package libxpm4:amd64.
Preparing to unpack .../08-libxpm4_1%3a3.5.12-1_amd64.deb ...
Unpacking libxpm4:amd64 (1:3.5.12-1) ...
Selecting previously unselected package libgd3:amd64.
Preparing to unpack .../09-libgd3_2.2.5-5.2ubuntu2.1_amd64.deb ...
Unpacking libgd3:amd64 (2.2.5-5.2ubuntu2.1) ...
Selecting previously unselected package nginx-common.
Preparing to unpack .../10-nginx-common_1.18.0-0ubuntu1.2_all.deb ...
Unpacking nginx-common (1.18.0-0ubuntu1.2) ...
Selecting previously unselected package libnginx-mod-http-image-filter.
Preparing to unpack .../11-libnginx-mod-http-image-filter_1.18.0-0ubuntu1.2_amd64.deb ...
Unpacking libnginx-mod-http-image-filter (1.18.0-0ubuntu1.2) ...
Selecting previously unselected package libnginx-mod-http-xslt-filter.
Preparing to unpack .../12-libnginx-mod-http-xslt-filter_1.18.0-0ubuntu1.2_amd64.deb ...
Unpacking libnginx-mod-http-xslt-filter (1.18.0-0ubuntu1.2) ...
Selecting previously unselected package libnginx-mod-mail.
Preparing to unpack .../13-libnginx-mod-mail_1.18.0-0ubuntu1.2_amd64.deb ...
Unpacking libnginx-mod-mail (1.18.0-0ubuntu1.2) ...
Selecting previously unselected package libnginx-mod-stream.
Preparing to unpack .../14-libnginx-mod-stream_1.18.0-0ubuntu1.2_amd64.deb ...
Unpacking libnginx-mod-stream (1.18.0-0ubuntu1.2) ...
Selecting previously unselected package nginx-core.
Preparing to unpack .../15-nginx-core_1.18.0-0ubuntu1.2_amd64.deb ...
Unpacking nginx-core (1.18.0-0ubuntu1.2) ...
Selecting previously unselected package nginx.
Preparing to unpack .../16-nginx_1.18.0-0ubuntu1.2_all.deb ...
Unpacking nginx (1.18.0-0ubuntu1.2) ...
Setting up libxpm4:amd64 (1:3.5.12-1) ...
Setting up nginx-common (1.18.0-0ubuntu1.2) ...
Created symlink /etc/systemd/system/multi-user.target.wants/nginx.service → /lib/systemd/system/nginx.service.
Setting up libjbig0:amd64 (2.1-3.1build1) ...
Setting up libnginx-mod-http-xslt-filter (1.18.0-0ubuntu1.2) ...
Setting up libwebp6:amd64 (0.6.1-2ubuntu0.20.04.1) ...
Setting up fonts-dejavu-core (2.37-1) ...
Setting up libjpeg-turbo8:amd64 (2.0.3-0ubuntu1.20.04.1) ...
Setting up libjpeg8:amd64 (8c-2ubuntu8) ...
Setting up libnginx-mod-mail (1.18.0-0ubuntu1.2) ...
Setting up fontconfig-config (2.13.1-2ubuntu3) ...
Setting up libnginx-mod-stream (1.18.0-0ubuntu1.2) ...
Setting up libtiff5:amd64 (4.1.0+git191117-2ubuntu0.20.04.2) ...
Setting up libfontconfig1:amd64 (2.13.1-2ubuntu3) ...
Setting up libgd3:amd64 (2.2.5-5.2ubuntu2.1) ...
Setting up libnginx-mod-http-image-filter (1.18.0-0ubuntu1.2) ...
Setting up nginx-core (1.18.0-0ubuntu1.2) ...
Setting up nginx (1.18.0-0ubuntu1.2) ...
Processing triggers for ufw (0.36-6ubuntu1) ...
Processing triggers for systemd (245.4-4ubuntu3.13) ...
Processing triggers for man-db (2.9.1-1) ...
Processing triggers for libc-bin (2.31-0ubuntu9.2) ...
vagrant@diplom:~$ systemctl status nginx
● nginx.service - A high performance web server and a reverse proxy server
     Loaded: loaded (/lib/systemd/system/nginx.service; enabled; vendor preset: enabled)
     Active: active (running) since Wed 2022-03-16 10:43:10 UTC; 2min 54s ago
       Docs: man:nginx(8)
   Main PID: 15075 (nginx)
      Tasks: 2 (limit: 1071)
     Memory: 3.5M
     CGroup: /system.slice/nginx.service
             ├─15075 nginx: master process /usr/sbin/nginx -g daemon on; master_process on;
             └─15076 nginx: worker process

Mar 16 10:43:10 diplom systemd[1]: Starting A high performance web server and a reverse proxy server...
Mar 16 10:43:10 diplom systemd[1]: Started A high performance web server and a reverse proxy server.
  ```
</details>

<details>
  <summary>Создаем директорию сайта, индексный файл и меняем права</summary>

  ```shell
vagrant@diplom:~$ sudo mkdir -p /var/www/diplom.dev
vagrant@diplom:~$ sudo vim /var/www/diplom.dev/index.html
vagrant@diplom:~$ cat /var/www/diplom.dev/index.html
<!DOCTYPE html>
<html>
<head>
<title>PCS-DEVSYS-DIPLOM</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>
<h1>This page served with SSL encryption!</h1>
</body>
</html>
vagrant@diplom:~$ sudo chown -R root:www-data /var/www/diplom.dev
vagrant@diplom:~$ sudo chmod -R 755 /var/www/diplom.dev

  ```
</details>

<details>
  <summary>Создаем конфигурацию сайта, копируем сертификаты и перезагружаем nginx</summary>

  ```shell
vagrant@diplom:~$ sudo vim /etc/nginx/sites-available/diplom.dev 
vagrant@diplom:~$ cat /etc/nginx/sites-available/diplom.dev 
server {
        listen 443 ssl http2;
        server_name diplom.dev;
        ssl_protocols TLSv1.2 TLSv1.1;
        ssl_certificate ssl/diplom.dev.crt;
        ssl_certificate_key ssl/diplom.dev.key;
        root /var/www/diplom.dev;
        index index.html index.htm;
        location / {
                try_files $uri $uri/ =404;
        }
}
vagrant@diplom:~$ sudo mkdir /etc/nginx/ssl
vagrant@diplom:~$ sudo cp diplom.dev* /etc/nginx/ssl
vagrant@diplom:~$ sudo systemctl reload nginx
  ```
</details>

## Страница сервера nginx в браузере хоста не содержит предупреждений

![Сертификат действителен, предупреждений нет](https://github.com/rudenko-ma/netology.homeworks/blob/main/pcs-devsys-diplom/img/diplom.dev.1.png)

## Скрипт генерации нового сертификата работает (сертификат сервера ngnix должен быть "зеленым")

<details>
  <summary></summary>

  ```shell


  ```
</details>

## Crontab работает (выберите число и время так, чтобы показать что crontab запускается и делает что надо)

