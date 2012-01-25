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



