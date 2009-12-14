#
%include	/usr/lib/rpm/macros.perl
#
Summary:	Common build files of the C++ binding libraries
Summary(pl.UTF-8):	Wspólne pliki do budowy bibliotek wiązań do C++
Name:		mm-common
Version:	0.8
Release:	1
License:	GPL v2 and GFDL
Group:		Development/Tools
Source0:	http://ftp.gnome.org/pub/GNOME/sources/mm-common/0.8/%{name}-%{version}.tar.bz2
# Source0-md5:	2a335530f02c35dec1deea4b3627b725
URL:		http://www.gtkmm.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	rpm-perlprov
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
%attr(755,root,root) %{_bindir}/mm-common-prepare
%docdir %{_docdir}/mm-common
%{_docdir}/mm-common/*
%{_aclocaldir}/*.m4
%{_datadir}/mm-common
%{_mandir}/man1/mm-common-prepare.1*
%{_npkgconfigdir}/mm-common-libstdc++.pc
