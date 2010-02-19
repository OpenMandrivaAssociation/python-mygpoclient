%define oname mygpoclient
%define name python-%oname
%define version 1.1
%define release %mkrel 1

Summary: Library for accessing my.gpodder.org web services
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://thpinfo.com/2010/mygpoclient/%{oname}-%{version}.tar.gz
License: GPLv3
Group: Development/Python
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
BuildRequires: python-devel
Requires: python-simplejson
Url: http://thpinfo.com/2010/mygpoclient/

%description
The mygpoclient library allows developers to utilize a Pythonic
interface to the my.gpodder.org web services for synchronizing podcast
subscriptions. This page provides the public place for downloading
source releases of the library.

%prep
%setup -q -n %oname-%version

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS README
%py_puresitedir/%oname
%py_puresitedir/*.egg-info
