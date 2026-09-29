# nginx

## Description

This repository contains spec files for building `nginx` module RPM packages.

Packages are built and published by [spec-package-builder](https://github.com/damex-el-packages/spec-package-builder) pipeline.

Modules are built against upstream `nginx` from `nginx.org`.
Module package version is `<nginx version>+<module version>`, same as `nginx.org` module packages.
Each module package requires exactly `nginx` version it is built against.

`nginx-module-devel` provides same build macros as `nginx-mod-devel` from `Red Hat Enterprise Linux`, built against `nginx.org` source.
Its version is `nginx` version it carries source of.
Module spec files use `%nginx_modconfigure`, `%nginx_modbuild`, `%nginx_moddir` and `%nginx_modconfdir` same way as distribution modules.

Currently, packages and their corresponding spec files are built and tested only for `Red Hat Enterprise Linux 9`, `Red Hat Enterprise Linux 10` and its derivatives like `Alma Linux 9`, `Alma Linux 10`, `Rocky Linux 9` and `Rocky Linux 10`.

[Follow here if you want to add modules or nginx versions](#usage).

[Follow here if you want to use prebuilt packages](#using-prebuilt-packages).

## Usage

### Layout

```
SPECS/nginx-module-devel.common.spec
SPECS/nginx-module-devel-<nginx branch>.spec
SPECS/nginx-module-<module>.common.spec
SPECS/nginx-module-<module>-<nginx branch>.spec
SPECS/el9/<spec> -> ../<spec>
SPECS/el10/<spec> -> ../<spec>
```

Common spec file holds package logic.
Branch spec file sets `nginx_version` and includes common spec file.
Symlink in `SPECS/el9` or `SPECS/el10` enables build for that distribution.

### Adding nginx version

Module build requires `nginx-module-devel` of same version from this repository.
Publish `nginx-module-devel` first, add modules for that version after:

1. Add or bump `SPECS/nginx-module-devel-<nginx branch>.spec` and push to `production`.
2. After publish, add or bump `SPECS/nginx-module-<module>-<nginx branch>.spec` for each module and push to `production`.

## Using prebuilt packages

### Add damex-nginx repository with prebuilt packages

To add `damex-nginx` repository to `Red Hat Enterprise Linux 9` install the following package:

```sh
# x86_64
https://yum-repositories.damex.org/nginx/el/9/x86_64/damex-nginx-release-0.1.0-1.el9.x86_64.rpm
# aarch64
https://yum-repositories.damex.org/nginx/el/9/aarch64/damex-nginx-release-0.1.0-1.el9.aarch64.rpm
```

To add `damex-nginx` repository to `Red Hat Enterprise Linux 10` install the following package:

```sh
# x86_64
https://yum-repositories.damex.org/nginx/el/10/x86_64/damex-nginx-release-0.1.0-1.el10.x86_64.rpm
# aarch64
https://yum-repositories.damex.org/nginx/el/10/aarch64/damex-nginx-release-0.1.0-1.el10.aarch64.rpm
```

Alternatively, it can be done manually by adding the following configuration to `/etc/yum.repos.d/damex-nginx.repo`:

```sh
[damex-nginx]
name = damex-nginx
baseurl = https://yum-repositories.damex.org/nginx/el/$releasever/$basearch
gpgcheck = 1
repo_gpgcheck = 1
gpgkey = https://yum-repositories.damex.org/nginx/nginx-2036-09-26.asc
```

### List of prebuilt packages

| Package                   | nginx  | Repository  | Architecture    | Distributives                                           |
|---------------------------|--------|-------------|-----------------|---------------------------------------------------------|
| nginx-module-devel        | 1.30.5 | damex-nginx | x86_64, aarch64 | Red Hat Enterprise Linux 9, Red Hat Enterprise Linux 10 |
| nginx-module-headers-more | 1.30.5 | damex-nginx | x86_64, aarch64 | Red Hat Enterprise Linux 9, Red Hat Enterprise Linux 10 |
| nginx-module-vts          | 1.30.5 | damex-nginx | x86_64, aarch64 | Red Hat Enterprise Linux 9, Red Hat Enterprise Linux 10 |

Modules require `nginx` from `nginx.org` repository.
Add `nginx.org` repository as described in [nginx.org documentation](https://nginx.org/en/linux_packages.html#RHEL).

### Loading modules

Each module installs its `load_module` configuration to `/usr/share/nginx/modules`, same as distribution modules.
`nginx.org` configuration does not include that directory.
Add following line to top of `/etc/nginx/nginx.conf` once to load installed modules automatically:

```sh
include /usr/share/nginx/modules/*.conf;
```
