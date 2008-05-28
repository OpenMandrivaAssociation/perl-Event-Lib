%define realname   Event-Lib
%define version    1.03
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Perl extentions for event-based programming
Source:     http://www.cpan.org/modules/by-module/Event/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
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
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

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



