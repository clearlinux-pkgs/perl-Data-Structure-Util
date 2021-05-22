#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Data-Structure-Util
Version  : 0.16
Release  : 18
URL      : https://cpan.metacpan.org/authors/id/A/AN/ANDYA/Data-Structure-Util-0.16.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/A/AN/ANDYA/Data-Structure-Util-0.16.tar.gz
Summary  : 'Change nature of data within a structure'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Data-Structure-Util-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Test::Pod)

%description
This module provides useful method to modify the nature of data within a structure

%package dev
Summary: dev components for the perl-Data-Structure-Util package.
Group: Development
Provides: perl-Data-Structure-Util-devel = %{version}-%{release}
Requires: perl-Data-Structure-Util = %{version}-%{release}

%description dev
dev components for the perl-Data-Structure-Util package.


%package perl
Summary: perl components for the perl-Data-Structure-Util package.
Group: Default
Requires: perl-Data-Structure-Util = %{version}-%{release}

%description perl
perl components for the perl-Data-Structure-Util package.


%prep
%setup -q -n Data-Structure-Util-0.16
cd %{_builddir}/Data-Structure-Util-0.16

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
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

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Data::Structure::Util.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Data/Structure/Util.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Data/Structure/Util/Util.so
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Data/Structure/Util/autosplit.ix
