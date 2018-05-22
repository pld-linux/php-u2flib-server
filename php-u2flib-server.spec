# TODO: tests? (BR: phpunit)
%include	/usr/lib/rpm/macros.php
Summary:	PHP library for U2F implementation
Summary(pl.UTF-8):	Biblioteka PHP do implementowania U2F
Name:		php-u2flib-server
Version:	1.0.1
Release:	1
License:	BSD
Group:		Development/Languages/PHP
Source0:	https://developers.yubico.com/php-u2flib-server/Releases/%{name}-%{version}.tar.gz
# Source0-md5:	a8c806f48862d549376789a728e2cd0e
URL:		https://developers.yubico.com/php-u2flib-server/
%if %{with phpdeps}
BuildRequires:	/usr/bin/php
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
%endif
BuildRequires:	rpmbuild(macros) >= 1.654
Requires:	php(core) >= 5.6
Requires:	php(openssl)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Serverside U2F library for PHP. Provides functionality for registering
tokens and authentication with said tokens.

%description -l pl.UTF-8
Biblioteka strony serwerowej U2F dla PHP. Zapewnia funkcjonalność do
rejestrowania tokenów i uwierzytelniania nimi.

%package phpdoc
Summary:	Online manual for u2flib-server library
Summary(pl.UTF-8):	Dokumentacja online do biblioteki u2flib-server
Group:		Documentation
Requires:	php-dirs

%description phpdoc
Online manual for u2flib-server library.

%description phpdoc -l pl.UTF-8
Dokumentacja online do biblioteki u2flib-server.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{php_data_dir}
cp -pr src/u2flib_server $RPM_BUILD_ROOT%{php_data_dir}

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -pr examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

install -d $RPM_BUILD_ROOT%{_docdir}/phpdoc/u2flib_server
cp -pr apidocs/* $RPM_BUILD_ROOT%{_docdir}/phpdoc/u2flib_server

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog NEWS README
%{php_data_dir}/u2flib_server
%{_examplesdir}/%{name}-%{version}

%files phpdoc
%defattr(644,root,root,755)
%{_docdir}/phpdoc/u2flib_server
