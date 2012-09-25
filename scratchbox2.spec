%define git 20120925
%define version	2.0
%define rel 0
%define release %mkrel 0.git%{git}.%{rel}

#% define major		1
#% define libname	% mklibname % name % major
#% define libnamedev	% mklibname -d % name

Name:		scratchbox2
Version:	%{version}
Release:	%{release}
Summary:	Scratchbox 2 is a cross-compilation engine
Group:		Emulators
License:	LGPL+
URL:		https://maemo.gitorious.org/scratchbox2
Source0:	%{name}-%{git}.tar.bz2
Patch0:		scratchbox2-2.0-use-system-lua.patch
Patch1:		scratchbox2-2.0-noarch.patch
BuildRequires:	lua-devel
Requires:	fakeroot

%description
Scratchbox 2 is a cross-compilation engine,
it can be used to create a highly flexible SDK. 

#=================================================

%prep
%setup -q -n %{name}-%{git}
%patch0 -p1
%patch1 -p1

%build
./autogen.sh
#% configure2_5x
#% make

%install
%makeinstall_std prefix=%{buildroot}/%{_prefix}


%files
%{_bindir}/sb2*
%{_mandir}/man1/*.xz
%{_datadir}/%{name}
%{_libdir}/libsb2/*.so*
