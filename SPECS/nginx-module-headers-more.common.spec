%define debug_package %{nil}
%global _build_id_links none
%undefine source_date_epoch_from_changelog
%global nginx_module_headers_more_version 0.40

Name: nginx-module-headers-more
Version: %{nginx_version}+%{nginx_module_headers_more_version}
Release: 1%{?dist}
Summary: nginx headers more shared module
License: BSD-2-Clause
URL: https://github.com/openresty/headers-more-nginx-module
Source0: %{url}/archive/v%{nginx_module_headers_more_version}/headers-more-nginx-module-%{nginx_module_headers_more_version}.tar.gz
BuildRequires: nginx-module-devel = %{nginx_version}

%description
Nginx module for adding, setting and clearing input and output headers.

%prep
%autosetup -n headers-more-nginx-module-%{nginx_module_headers_more_version}

%build
%nginx_modconfigure
%nginx_modbuild

%install
%{__install} -d %{buildroot}%{nginx_moddir} %{buildroot}%{nginx_modconfdir}
%{__install} -m 755 %{_vpath_builddir}/ngx_http_headers_more_filter_module.so %{buildroot}%{nginx_moddir}/ngx_http_headers_more_filter_module.so
echo 'load_module "%{nginx_moddir}/ngx_http_headers_more_filter_module.so";' > %{buildroot}%{nginx_modconfdir}/module-headers-more.conf

%files
%doc README.markdown
%license LICENSE
%dir %{nginx_modconfdir}
%{nginx_moddir}/ngx_http_headers_more_filter_module.so
%{nginx_modconfdir}/module-headers-more.conf
