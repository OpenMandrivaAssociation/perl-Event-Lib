%define realname Event-Lib
%define upstream_version 1.03

Summary:	Perl extentions for event-based programming
Name:		perl-%{realname}
Version:	%perl_convert_version %upstream_version
Release:	6
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{realname}
Source0:	http://www.cpan.org/modules/by-module/Event/%{realname}-%{upstream_version}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	pkgconfig(libevent)

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
should have a look at the "EXAMPLE:	A SIMPLE TCP SERVER" manpage to get a
feeling about how it all fits together.

%prep
%setup -qn %{realname}-%{upstream_version} 

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# those tests fail with test::harness 3.x
# cf  https://rt.cpan.org/Ticket/Display.html?id=35355
# and http://rt.cpan.org/Public/Bug/Display.html?id=36130
#rm t/20_signal.t t/51_cleanup_persistent.t
#make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*

