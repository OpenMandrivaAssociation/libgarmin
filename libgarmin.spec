%define alphatag 20090212
%define vcs svn

%define major 0
%define libname %mklibname garmin %{major}
%define develname %mklibname garmin -d

Summary:	C library to parse and use Garmin image files
Name:		libgarmin
Version:	0
Release:	%mkrel 0.1.%{alphatag}%{vcs}.1
Group:		System/Libraries
License:	GPLv2
URL:		http://libgarmin.sourceforge.net/
Source0:	libgarmin-%{alphatag}%{vcs}.tar.bz2
Source1:	libgarmin-checkout.sh
Patch0:		libgarmin-20090212-shared.diff
BuildRequires:	libtool
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

%description
Libgarmin is a library used to parse IMG files from Garmin GPS devices.

%package -n	%{libname}
Summary:	C library to parse and use Garmin image files
Group:		System/Libraries

%description -n	%{libname}
Libgarmin is a library used to parse IMG files from Garmin GPS devices.

%package -n	%{develname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Requires:	pkgconfig

%description -n	%{develname}
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%package	tools
Summary:	Various binaries to manipulate garmin IMG format image files
Group:		File tools

%description	tools
This package provides binaries manipulate garmin IMG format image files.

%prep

%setup -q -n %{name}-%{alphatag}
%patch0 -p1

%build
libtoolize --copy --force; aclocal; autoconf; automake --add-missing --copy

%configure2_5x

%make

%install
rm -rf %{buildroot}

%makeinstall_std INSTALL="install -p"

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root,-)
%doc AUTHORS README
%{_libdir}/*.so.%{major}*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/garmintypes.txt

%files -n %{develname}
%defattr(-,root,root,-)
%{_datadir}/%{name}/doc/*
%{_includedir}/*.h
%{_libdir}/*.*a
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc

%files tools
%defattr(-,root,root,-)
%{_bindir}/*

%changelog
* Mon Aug 02 2010 Oden Erikssson <oeriksson@mandriva.com> 0-0.1.20090212svn.1mdv2010.1
- initial Mandriva package (stolen from fedora, but provided as a shared library)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.7.20090212svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Apr 11 2009 Fabian Affolter <fabian@bernewireless.net> - 0-0.6.20090212svn
- Added virtual provide 
- Changed group tag
- Removed '--enable-static=no' to configure
- Removed INSTALL

* Thu Feb 12 2009 Fabian Affolter <fabian@bernewireless.net> - 0-0.5.20090212svn
- Updated from revision 315 to revision 320

* Sun Dec 14 2008 Fabian Affolter <fabian@bernewireless.net> - 0-0.4.20081214svn
- Updated from revision 307 to revision 315

* Mon Nov 10 2008 Fabian Affolter <fabian@bernewireless.net> - 0-0.3.20081026svn
- Added pkgconfig to devel-package
- Fixed %%doc stuff acc. #468631 comment #3

* Thu Oct 28 2008 Fabian Affolter <fabian@bernewireless.net> - 0-0.2.20081026svn
- Fixed license
- Don't delete *.a file
- Added '--enable-static=no' to configure

* Sun Oct 26 2008 Fabian Affolter <fabian@bernewireless.net> - 0-0.1.20081026svn
- Initial package for Fedora

