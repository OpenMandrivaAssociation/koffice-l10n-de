Name: koffice-l10n-de
Version: 2.3.2
Release: %mkrel 2
Summary: Language files for KOffice German
Group: System/Internationalization
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License: GPLv2+
URL: https://www.koffice.org
BuildArch: noarch
Source: ftp://ftp.kde.org/pub/kde/stable/koffice-%version/src/koffice-l10n/%name-%version.tar.bz2
BuildRequires: gettext >= 0.15
BuildRequires: kdelibs4-devel
Requires: locales-de
Requires: koffice-core
Provides: koffice-l10n

%description 
Provides German translations for KOffice.

%files 
%defattr(-,root,root,-)
%{_kde_datadir}/*/*/*

#------------------------------------------------------------------------------------------------

%prep
%setup -q -n %name-%version

%build
%cmake_kde4
%make

%install
rm -rf %buildroot
%makeinstall_std -C build

%clean
rm -rf %buildroot


%changelog
* Sat Feb 26 2011 Funda Wang <fwang@mandriva.org> 2.3.2-2mdv2011.0
+ Revision: 639847
- rebuild

* Fri Feb 18 2011 Funda Wang <fwang@mandriva.org> 2.3.2-1
+ Revision: 638330
- New version 2.3.2

* Thu Jan 20 2011 Funda Wang <fwang@mandriva.org> 2.3.1-1
+ Revision: 631766
- New version 2.3.1

* Thu Dec 30 2010 Funda Wang <fwang@mandriva.org> 2.3.0-1mdv2011.0
+ Revision: 626267
- New version 2.3.0

* Thu Dec 09 2010 Funda Wang <fwang@mandriva.org> 2.2.91-1mdv2011.0
+ Revision: 617999
- New version 2.2.91

* Thu Nov 18 2010 Funda Wang <fwang@mandriva.org> 2.2.84-1mdv2011.0
+ Revision: 598546
- New version 2.2.84

* Fri Oct 29 2010 Funda Wang <fwang@mandriva.org> 2.2.83-1mdv2011.0
+ Revision: 589874
- New version 2.2.83

* Wed Oct 06 2010 Funda Wang <fwang@mandriva.org> 2.2.82-1mdv2011.0
+ Revision: 583741
- new version 2.2.82

* Wed Sep 15 2010 Funda Wang <fwang@mandriva.org> 2.2.81-1mdv2011.0
+ Revision: 578538
- new version 2.2.81

* Sat Aug 28 2010 Funda Wang <fwang@mandriva.org> 2.2.2-1mdv2011.0
+ Revision: 573623
- new version 2.2.2

* Sun Jul 11 2010 Funda Wang <fwang@mandriva.org> 2.2.1-1mdv2011.0
+ Revision: 550684
- new version 2.2.1

* Thu May 27 2010 Funda Wang <fwang@mandriva.org> 2.2.0-1mdv2010.1
+ Revision: 546365
- new version 2.2.0

* Wed Apr 28 2010 Funda Wang <fwang@mandriva.org> 2.1.91-1mdv2010.1
+ Revision: 540368
- new version 2.1.91

* Sat Apr 17 2010 Funda Wang <fwang@mandriva.org> 2.1.82-1mdv2010.1
+ Revision: 535718
- New version 2.1.82

* Thu Jan 14 2010 Funda Wang <fwang@mandriva.org> 2.1.1-1mdv2010.1
+ Revision: 491254
- new version 2.1.1

* Tue Nov 24 2009 Funda Wang <fwang@mandriva.org> 2.1.0-1mdv2010.1
+ Revision: 469504
- new version 2.1.0

* Fri Nov 13 2009 Funda Wang <fwang@mandriva.org> 2.0.91-1mdv2010.1
+ Revision: 465542
- new version 2.0.91

* Thu Sep 17 2009 Funda Wang <fwang@mandriva.org> 2.0.82-1mdv2010.0
+ Revision: 443708
- new version 2.0.82

* Wed Aug 12 2009 Funda Wang <fwang@mandriva.org> 2.0.2-1mdv2010.0
+ Revision: 415390
- new version 2.0.2

* Sat Jun 27 2009 Funda Wang <fwang@mandriva.org> 2.0.1-1mdv2010.0
+ Revision: 389643
- new version 2.0.1

* Thu May 28 2009 Funda Wang <fwang@mandriva.org> 2.0.0-1mdv2010.0
+ Revision: 380397
- New verison 2.0.0
- new version 1.9.99.0

* Sun Feb 01 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.9.98.6-1mdv2009.1
+ Revision: 335944
- Update to beta6

* Sat Jan 17 2009 Funda Wang <fwang@mandriva.org> 1.9.98.5-1mdv2009.1
+ Revision: 330476
- new version 1.9.98.5

* Thu Dec 11 2008 Funda Wang <fwang@mandriva.org> 1.9.98.3-1mdv2009.1
+ Revision: 312663
- new version 1.9.98.3

* Thu Nov 20 2008 Funda Wang <fwang@mandriva.org> 1.9.98.2-1mdv2009.1
+ Revision: 305028
- add source and spec
- Created package structure for koffice-l10n-de.


* Mon Feb 26 2007 Laurent Montel <lmontel@mandriva.com> 1.6.2-2mdv2007.0
+ Revision: 125736
- Fix spec file
- 1.6.2

* Thu Nov 30 2006 Laurent Montel <lmontel@mandriva.com> 1.6.1-2mdv2007.1
+ Revision: 89112
- Fix spec file
- 1.6.1

* Mon Nov 06 2006 Laurent Montel <lmontel@mandriva.com> 1.6.0-2mdv2007.1
+ Revision: 76936
- Fix spec file
- 1.6.0
- Import koffice-l10n-de

* Thu Jul 13 2006 Laurent MONTEL <lmontel@mandriva.com> 1.5.1-3
- Requires koffice-apps

* Sun May 28 2006 Laurent MONTEL <lmontel@mandriva.com> 1.5.1-2
- Use %%mkrel

* Thu May 25 2006 Laurent MONTEL <lmontel@mandriva.com> 1.5.1-1mdk
- 1.5.1

* Thu Apr 13 2006 Laurent MONTEL <lmontel@mandriva.com> 1.5.0-1mdk
- 1.5.0

* Fri Mar 31 2006 Laurent MONTEL <lmontel@mandriva.com> 1.5-0.rc1.1mdk
- 1.5.0-rc1

* Tue Oct 18 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 1.4.2-1mdk
- 1.4.2

* Sat Aug 13 2005 Laurent MONTEL <lmontel@mandriva.com> 20mdk
- Remove conflict with kde-i18n

* Fri Jul 29 2005 Laurent MONTEL <lmontel@mandriva.com> 10mdk
- Fix provides koffice-l10n

* Tue Jul 26 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 1.4.1-1mdk
- 1.4.1

* Sat Jun 18 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 1.4.0-1mdk
- 1.4.0

* Wed Apr 20 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 1.3.91-1mdk
- 1.3.91

* Wed Nov 17 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 1.3.5-1mdk
- 1.3.5

* Thu Oct 14 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 1.3.4-1mdk
- 1.3.4

* Wed Sep 22 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 1.3.3-1mdk
- 1.3.3

* Tue Jul 06 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 1.3.2-1mdk
- 1.3.2

* Wed May 05 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 1.3.1-1mdk
- 1.3.1

