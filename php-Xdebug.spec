#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-Xdebug
Version  : 3.1.5
Release  : 15
URL      : https://pecl.php.net/get/xdebug-3.1.5.tgz
Source0  : https://pecl.php.net/get/xdebug-3.1.5.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : PHP-3.01
BuildRequires : buildreq-php

%description
======
With this debug client you can control the Xdebug server. For compilation and
installation see the INSTALL file.

%prep
%setup -q -n xdebug-3.1.5
cd %{_builddir}/xdebug-3.1.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static
make  %{?_smp_mflags}

%install
%make_install


%files
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20210902/xdebug.so
