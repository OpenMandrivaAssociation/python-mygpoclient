%define oname mygpoclient

Summary: Library for accessing my.gpodder.org web services
Name: python-%oname
Version: 1.10
Release: 3
Source0: http://thpinfo.com/2010/mygpoclient/mygpoclient-%{version}.tar.gz
License: GPLv3
Group: Development/Python
BuildArch: noarch
BuildRequires: python-devel
Url: https://thpinfo.com/2010/mygpoclient/

%description
The mygpoclient library allows developers to utilize a Pythonic
interface to the my.gpodder.org web services for synchronizing podcast
subscriptions. This page provides the public place for downloading
source releases of the library.

%prep
%autosetup -p1 -n %oname-%version

%build
%py_build

%install
%py_install

%files
%defattr(-,root,root)
%_bindir/mygpo*
%py_puresitedir/%oname
%py_puresitedir/*.egg-info
%{_mandir}/man1/*.1*
