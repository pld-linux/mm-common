Summary:	Common build files of the C++ binding libraries
Summary(pl.UTF-8):	Wspólne pliki do budowy bibliotek wiązań do C++
Name:		mm-common
Version:	1.0.4
Release:	1
License:	GPL v2+
Group:		Development/Tools
Source0:	https://download.gnome.org/sources/mm-common/1.0/%{name}-%{version}.tar.xz
# Source0-md5:	89b31b24a4dc5e3ea5f900d1c103ea24
URL:		https://www.gtkmm.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	rpm-perlprov
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides the build infrastructure and utilities shared
among the GNOME C++ binding libraries.

%description -l pl.UTF-8
Ten pakiet dostarcza infrastrukturę do budowania i narzędzia dzielone
pomiędzy biblioteki wiązań C++ do GNOME.

%prep
%setup -q

%{__sed} -i -e '1s,/usr/bin/env python3$,%{__python3},' util/mm-common-get.in

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/mm-common-get
%attr(755,root,root) %{_bindir}/mm-common-prepare
%docdir %{_docdir}/mm-common
%{_docdir}/mm-common
%{_aclocaldir}/mm-ax_cxx_compile_stdcxx.m4
%{_aclocaldir}/mm-ax_cxx_compile_stdcxx_11.m4
%{_aclocaldir}/mm-common.m4
%{_aclocaldir}/mm-dietlib.m4
%{_aclocaldir}/mm-doc.m4
%{_aclocaldir}/mm-module.m4
%{_aclocaldir}/mm-pkg.m4
%{_aclocaldir}/mm-warnings.m4
%{_datadir}/mm-common
%{_npkgconfigdir}/mm-common-libstdc++.pc
%{_npkgconfigdir}/mm-common-util.pc
%{_mandir}/man1/mm-common-get.1*
%{_mandir}/man1/mm-common-prepare.1*
