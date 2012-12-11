%define oname mygpoclient
%define name python-%oname
%define version 1.6
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
Url: http://thpinfo.com/2010/mygpoclient/

%description
The mygpoclient library allows developers to utilize a Pythonic
interface to the my.gpodder.org web services for synchronizing podcast
subscriptions. This page provides the public place for downloading
source releases of the library.

%prep
%setup -q -n %oname-%version
%apply_patches

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
%_bindir/bpsync
%py_puresitedir/%oname
%py_puresitedir/*.egg-info


%changelog
* Fri Aug 05 2011 Götz Waschk <waschk@mandriva.org> 1.6-1mdv2012.0
+ Revision: 693273
- update to new version 1.6

* Tue Nov 02 2010 Funda Wang <fwang@mandriva.org> 1.5-2mdv2011.0
+ Revision: 591742
- rebuild for py 2.7

* Sun Oct 10 2010 Götz Waschk <waschk@mandriva.org> 1.5-1mdv2011.0
+ Revision: 584541
- new version
- drop patch

* Mon Sep 27 2010 Götz Waschk <waschk@mandriva.org> 1.4-2mdv2011.0
+ Revision: 581208
- fix server response checking (bug #1131)

* Mon Apr 26 2010 Götz Waschk <waschk@mandriva.org> 1.4-1mdv2010.1
+ Revision: 538917
- update to new version 1.4

* Mon Apr 26 2010 Götz Waschk <waschk@mandriva.org> 1.3-1mdv2010.1
+ Revision: 538815
- new version
- add bpsync tool

* Mon Mar 15 2010 Götz Waschk <waschk@mandriva.org> 1.2-1mdv2010.1
+ Revision: 519818
- update to new version 1.2
- remove dep on simplejson

* Fri Feb 19 2010 Götz Waschk <waschk@mandriva.org> 1.1-1mdv2010.1
+ Revision: 508386
- update to new version 1.1

* Thu Feb 04 2010 Götz Waschk <waschk@mandriva.org> 1.0-2mdv2010.1
+ Revision: 500722
- add dep on simplejson

* Thu Feb 04 2010 Götz Waschk <waschk@mandriva.org> 1.0-1mdv2010.1
+ Revision: 500715
- import python-mygpoclient


