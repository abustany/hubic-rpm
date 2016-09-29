%define version_major 2.1.0
%define version_minor 53

%global debug_package %{nil}

Name:		hubiC
Version:	%{version_major}.%{version_minor}
Release:	1%{?dist}
Summary:	hubiC allows you to synchronize a local folder with your hubiC account

Group:		System Environment/Daemons
License:	OVH
URL:		http://mir7.ovh.net/ovh-applications/hubic/hubiC-Linux/
Source0:	http://mir7.ovh.net/ovh-applications/hubic/hubiC-Linux/%{version_major}/hubiC-Linux-%{version}-linux.tar.gz

BuildRequires:	make
Requires:	mono-core dbus

%description
This client provides:

* A background synchronization service which expose a DBus API to communicate
  with 3rd party frontends
* Basic command line tools to control the background service


%prep
%setup -q -n hubic


%build


%install
make install PREFIX=%{buildroot}%{_prefix} RUNTIME_PREFIX=%{_prefix} DBUSSERVICE_DIR=%{buildroot}%{_datadir}/dbus-1/services


%files
%{_bindir}/hubic
%{_prefix}/lib/hubic/hubiC.exe
%{_prefix}/lib/hubic/hubic-service
%{_prefix}/lib/hubic/*.dll
%{_datadir}/dbus-1/services/com.hubiC.service
%{_datadir}/icons/hicolor/16x16/hubic.png
%{_datadir}/icons/hicolor/64x64/hubic.png
%{_datadir}/icons/hicolor/128x128/hubic.png

%{_mandir}/man1/hubic.1.gz
%{_docdir}/hubic/dbusapi/*
%{_docdir}/hubic/README.gz
%{_docdir}/hubic/changelog.gz
%{_docdir}/hubic/copyright


%changelog
* Thu Sep 29 2016 Adrien Bustany <adrien@bustany.org> - 2.1.0.53-1
- Initial packaging
