Summary:	XVidCap - Video Capture for X
Name:		xvidcap
Version:	1.1.3
Release:	0.1
License:	GPL
Group:		-
Source0:	http://download.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	ea896ffd35d6fe6d2abf51b38605f5fd
Patch0:		%{name}-DESTDIR.patch
URL:		http://xvidcap.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ffmpeg-devel
BuildRequires:	gtk+2-devel
BuildRequires:	zlib-devel
BuildRequires:	libpng-devel
BuildRequires:	libjpeg-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Capture parts of your screen to single files for every frame or to an mpeg
stream.

This program does not use a special hardware driver to access the video card.
It just asks the X server about rectangular areas. This means you need a fast
machine (>= 133 MHz) and a fast harddrive. Big frames (e.g. 384x288 = 1/2 PAL)
at a high FPS rate are only possible with very very fast systems :-)

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-gtk2
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_defaultdocdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
	
echo '.so xvidcap.1' > $RPM_BUILD_ROOT%{_mandir}/man1/gvidcap.1

rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/%{name}_%{version}/INSTALL
mv $RPM_BUILD_ROOT%{_datadir}/doc/%{name}_%{version} \
	$RPM_BUILD_ROOT%{_defaultdocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_defaultdocdir}/%{name}-%{version}
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
