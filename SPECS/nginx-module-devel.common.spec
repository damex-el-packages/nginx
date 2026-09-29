%define debug_package %{nil}
%undefine source_date_epoch_from_changelog

Name: nginx-module-devel
Version: %{nginx_version}
Release: 1%{?dist}
Summary: nginx module development files
License: BSD-2-Clause
URL: https://nginx.org
Source0: https://nginx.org/download/nginx-%{nginx_version}.tar.gz
Requires: gcc
Requires: make
Requires: openssl-devel
Requires: pcre2-devel
Requires: zlib-devel
Conflicts: nginx-mod-devel

%description
Nginx module development files for nginx.org nginx.

%prep
%autosetup -n nginx-%{nginx_version}

%build

%install
%{__install} -d %{buildroot}%{_usrsrc} %{buildroot}%{_rpmmacrodir} %{buildroot}%{_fileattrsdir}
%{__cp} -a %{_builddir}/nginx-%{nginx_version} %{buildroot}%{_usrsrc}/nginx-%{nginx_version}
cat > %{buildroot}%{_rpmmacrodir}/macros.nginxmods <<'EOF'
%%_nginx_abiversion %{nginx_version}
%%_nginx_srcdir %{_usrsrc}/nginx-%{nginx_version}
%%_nginx_buildsrcdir nginx-src
%%_nginx_modsrcdir ..
%%_nginx_modbuilddir ../%%{_vpath_builddir}
%%nginx_moddir %{_libdir}/nginx/modules
%%nginx_modconfdir %{_datadir}/nginx/modules

%%nginx_modrequires Requires: nginx-r%%{_nginx_abiversion}

%%nginx_modconfigure(:-:) \
  %%undefine _strict_symbol_defs_build \
  cp -a "%%{_nginx_srcdir}" "%%{_nginx_buildsrcdir}" \
  cd "%%{_nginx_buildsrcdir}" \
  ./configure --with-compat --with-cc-opt="%%{optflags}" --with-ld-opt="%%{build_ldflags} -Wl,-E" --add-dynamic-module="$(realpath %%{_nginx_modsrcdir})" --builddir="$(realpath %%{_nginx_modbuilddir})" %%{**} \
  cd -

%%nginx_modbuild %%{__make} -C "%%{_nginx_buildsrcdir}" %%{_make_output_sync} %%{?_smp_mflags} %%{_make_verbose} modules
EOF
cat > %{buildroot}%{_fileattrsdir}/nginxmods.attr <<'EOF'
%%__nginxmods_requires() nginx-r%%{_nginx_abiversion}
%%__nginxmods_path ^%%{_prefix}/lib(64)?/nginx/modules/.*\\.so$
EOF

%files
%license LICENSE
%{_usrsrc}/nginx-%{nginx_version}
%{_rpmmacrodir}/macros.nginxmods
%{_fileattrsdir}/nginxmods.attr
