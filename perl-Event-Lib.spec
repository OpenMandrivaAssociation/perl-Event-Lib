%define realname   Event-Lib
%define upstream_version    1.03
%define release    %mkrel 4

Name:       perl-%{realname}
Version:    %perl_convert_version %upstream_version
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Perl extentions for event-based programming
Source:     http://www.cpan.org/modules/by-module/Event/%{realname}-%{upstream_version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{upstream_version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: libevent-devel

%description
This module is a Perl wrapper around libevent(3) as available from the
http://www.monkey.org/~provos/libevent/ manpage. It allows to execute a
function whenever a given event on a filehandle happens, a timeout occurs
or a signal is received.

Under the hood, one of the available mechanisms for asynchronously dealing
with events is used. This could be 'select', 'poll', 'epoll', 'devpoll' or
'kqueue'. The idea is that you don't have to worry about those details and
the various interfaces they offer. _Event::Lib_ offers a unified interface
to all of them (but see the "CONFIGURATION" manpage further below).

Once you've skimmed through the next two sections (or maybe even now), you
should have a look at the "EXAMPLE: A SIMPLE TCP SERVER" manpage to get a
feeling about how it all fits together.

%prep
%setup -q -n %{realname}-%{upstream_version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
# those tests fail with test::harness 3.x
# cf  https://rt.cpan.org/Ticket/Display.html?id=35355
# and http://rt.cpan.org/Public/Bug/Display.html?id=36130
rm t/20_signal.t t/51_cleanup_persistent.t
%make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*





%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.30.0-4mdv2012.0
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Thu Dec 29 2011 Götz Waschk <waschk@mandriva.org> 1.30.0-3
+ Revision: 748202
- rebuild

* Wed Dec 22 2010 Oden Eriksson <oeriksson@mandriva.com> 1.30.0-2mdv2011.0
+ Revision: 623877
- rebuilt against libevent 2.x

* Wed Jul 21 2010 Jérôme Quelin <jquelin@mandriva.org> 1.30.0-1mdv2011.0
+ Revision: 556555
- remove faulty tests failing with test::harness 3.x

* Tue Jul 28 2009 Götz Waschk <waschk@mandriva.org> 1.30.0-1mdv2010.0
+ Revision: 401504
- use perl version macro

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.03-2mdv2009.0
+ Revision: 268480
- rebuild early 2009.0 package (before pixel changes)
- fix extra spacing at top of description

* Wed May 28 2008 Götz Waschk <waschk@mandriva.org> 1.03-1mdv2009.0
+ Revision: 212550
- import perl-Event-Lib


