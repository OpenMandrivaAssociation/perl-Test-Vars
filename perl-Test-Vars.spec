%define upstream_name    Test-Vars
%define upstream_version 0.005

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Detects unused variables
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/Test-Vars-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires: perl(Module::Build)
BuildRequires:	perl(B)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(parent)
BuildArch:	noarch

%description
Test::Vars finds unused variables in order to keep the source code tidy.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Build.PL installdirs=vendor
./Build

%check
./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc Changes META.yml 
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.1.0-2mdv2011.0
+ Revision: 655229
- rebuild for updated spec-helper

* Mon Mar 29 2010 Jérôme Quelin <jquelin@mandriva.org> 0.1.0-1mdv2011.0
+ Revision: 528822
- import perl-Test-Vars


* Mon Mar 29 2010 cpan2dist 0.001-1mdv
- initial mdv release, generated with cpan2dist

