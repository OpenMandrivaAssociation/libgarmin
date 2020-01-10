%define alphatag 20090212
%define vcs svn

%define major 0
%define libname %mklibname garmin %{major}
%define devname %mklibname garmin -d

Summary:	C library to parse and use Garmin image files
Name:		libgarmin
Version:	0
Release:	0.1.%{alphatag}%{vcs}.1
Group:		System/Libraries
License:	GPLv2
URL:		http://libgarmin.sourceforge.net/
Source0:	libgarmin-%{alphatag}%{vcs}.tar.bz2
Source1:	libgarmin-checkout.sh
Patch0:		libgarmin-20090212-shared.diff
BuildRequires:	libtool

%description
Libgarmin is a library used to parse IMG files from Garmin GPS devices.

%package	tools
Summary:	Various binaries to manipulate garmin IMG format image files
Group:		File tools

%description	tools
This package provides binaries manipulate garmin IMG format image files.

%package -n	%{libname}
Summary:	C library to parse and use Garmin image files
Group:		System/Libraries

%description -n	%{libname}
Libgarmin is a library used to parse IMG files from Garmin GPS devices.

%package -n	%{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%prep
%setup -qn %{name}-%{alphatag}
%autopatch -p1

%build
#libtoolize --copy --force; aclocal; autoconf; automake --add-missing --copy
autoreconf -fi
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std INSTALL="install -p"

%files tools
%doc AUTHORS README
%{_bindir}/*

%files -n %{libname}
%{_libdir}/*.so.%{major}*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/garmintypes.txt

%files -n %{devname}
%{_datadir}/%{name}/doc/*
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc

