%define debug_package %{nil}

Name: damex-nginx-release
Version: 0.1.0
Release: 1%{?dist}
Summary: damex nginx repository configuration
License: MIT
URL: https://yum-repositories.damex.org
BuildArch: noarch

%description

%prep

%build

%install
%{__install} -d %{buildroot}%{_sysconfdir}/yum.repos.d
%{__cat} <<'EOF' > %{buildroot}%{_sysconfdir}/yum.repos.d/damex-nginx.repo
[damex-nginx]
name = damex-nginx
baseurl = https://yum-repositories.damex.org/nginx/el/$releasever/$basearch
gpgcheck = 1
repo_gpgcheck = 1
gpgkey = https://yum-repositories.damex.org/nginx/nginx-2036-09-26.asc
EOF

%files
%defattr(-,root,root,-)
%config %{_sysconfdir}/yum.repos.d/damex-nginx.repo

%changelog
* %(date -u +"%%a %%b %%d %%Y") Roman Kuzmitskii <el-packages@damex.org> - %{version}-%{release}
- History: https://github.com/damex-el-packages/nginx/commits/production
