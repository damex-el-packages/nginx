%define debug_package %{nil}
%global _build_id_links none
%undefine source_date_epoch_from_changelog
%global nginx_module_vozlt_vts_version 0.2.7

Name: nginx-module-vozlt-vts
Version: %{nginx_version}+%{nginx_module_vozlt_vts_version}
Release: 1%{?dist}
Summary: nginx vozlt vts shared module
License: BSD-2-Clause
URL: https://github.com/vozlt/nginx-module-vts
Source0: %{url}/archive/refs/tags/v%{nginx_module_vozlt_vts_version}.tar.gz
BuildRequires: nginx-module-devel = %{nginx_version}

%description
Nginx virtual host traffic status module.

%prep
%autosetup -n nginx-module-vts-%{nginx_module_vozlt_vts_version}

%build
%nginx_modconfigure
%nginx_modbuild

%install
%{__install} -d %{buildroot}%{nginx_moddir} %{buildroot}%{nginx_modconfdir}
%{__install} -m 755 %{_vpath_builddir}/ngx_http_vhost_traffic_status_module.so %{buildroot}%{nginx_moddir}/ngx_http_vhost_traffic_status_module.so
echo 'load_module "%{nginx_moddir}/ngx_http_vhost_traffic_status_module.so";' > %{buildroot}%{nginx_modconfdir}/module-vozlt-vts.conf

%files
%license LICENSE
%dir %{nginx_modconfdir}
%{nginx_moddir}/ngx_http_vhost_traffic_status_module.so
%{nginx_modconfdir}/module-vozlt-vts.conf
