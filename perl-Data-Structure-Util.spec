#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Data-Structure-Util
Version  : 0.16
Release  : 6
URL      : https://cpan.metacpan.org/authors/id/A/AN/ANDYA/Data-Structure-Util-0.16.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/A/AN/ANDYA/Data-Structure-Util-0.16.tar.gz
Summary  : 'Change nature of data within a structure'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Data-Structure-Util-lib = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Test::Pod)

%description
This module provides useful method to modify the nature of data within a structure

%package dev
Summary: dev components for the perl-Data-Structure-Util package.
Group: Development
Requires: perl-Data-Structure-Util-lib = %{version}-%{release}
Provides: perl-Data-Structure-Util-devel = %{version}-%{release}

%description dev
dev components for the perl-Data-Structure-Util package.


%package lib
Summary: lib components for the perl-Data-Structure-Util package.
Group: Libraries

%description lib
lib components for the perl-Data-Structure-Util package.


%prep
%setup -q -n Data-Structure-Util-0.16

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Data/Structure/Util.pm
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/auto/Data/Structure/Util/autosplit.ix

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Data::Structure::Util.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/auto/Data/Structure/Util/Util.so
