%include	/usr/lib/rpm/macros.perl
%define	pdir	Class
%define	pnam	Factory
Summary:	Base class for dynamic factory classes
Summary(pl):	Klasa bazowa do dynamicznych klas przemys³owych
Name:		perl-%{pdir}-%{pnam}
Version:	1.00
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is intended to provide a base class for dynamic factory
classes.

%description -l pl
Ten modu³ ma za zadanie dostarczyæ klasê bazow± do dynamicznych klas
przemys³owych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change*
%{perl_sitelib}/%{pdir}/%{pnam}.pm
%{_mandir}/man3/*
