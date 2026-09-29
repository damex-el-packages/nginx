%define debug_package %{nil}
%global _build_id_links none
%undefine source_date_epoch_from_changelog
%global nginx_module_sts_version 0.1.1

Name: nginx-module-sts
Version: %{nginx_version}+%{nginx_module_sts_version}
Release: 1%{?dist}
Summary: nginx sts shared module
License: BSD-2-Clause
URL: https://github.com/vozlt/nginx-module-sts
Source0: %{url}/archive/v%{nginx_module_sts_version}/nginx-module-sts-%{nginx_module_sts_version}.tar.gz
BuildRequires: nginx-module-devel = %{nginx_version}
Requires: nginx-module-stream-sts

%description
Nginx stream server traffic status display module.

%prep
%autosetup -n nginx-module-sts-%{nginx_module_sts_version}

%build
%nginx_modconfigure --with-stream
%nginx_modbuild

%install
%{__install} -d %{buildroot}%{nginx_moddir} %{buildroot}%{nginx_modconfdir}
%{__install} -m 755 %{_vpath_builddir}/ngx_http_stream_server_traffic_status_module.so %{buildroot}%{nginx_moddir}/ngx_http_stream_server_traffic_status_module.so
echo 'load_module "%{nginx_moddir}/ngx_http_stream_server_traffic_status_module.so";' > %{buildroot}%{nginx_modconfdir}/module-sts.conf

%files
%license LICENSE
%dir %{nginx_modconfdir}
%{nginx_moddir}/ngx_http_stream_server_traffic_status_module.so
%{nginx_modconfdir}/module-sts.conf
