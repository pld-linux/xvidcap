Summary:	XVidCap - Video Capture for X
Summary(pl):	XVidCap - przechwytywanie obrazu dla X
Name:		xvidcap
Version:	1.1.4pre3
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://dl.sourceforge.net/xvidcap/%{name}-%{version}.tar.gz
# Source0-md5:	d3364d12dab30902baa8da535604947f
URL:		http://xvidcap.sourceforge.net/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	ffmpeg-devel >= 0.4.9-3.20050806
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	pkgconfig
BuildRequires:	zlib-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Capture parts of your screen to single files for every frame or to an
MPEG stream.

This program does not use a special hardware driver to access the
video card. It just asks the X server about rectangular areas. This
means you need a fast machine (>= 133 MHz) and a fast harddrive. Big
frames (e.g. 384x288 = 1/2 PAL) at a high FPS rate are only possible
with very very fast systems :-)

%description -l pl
Ten pakiet s³u¿y do przechwytywania ekranu do pojedynczych plików z
ka¿d± ramk± lub strumienia MPEG.

Program nie u¿ywa ¿adnego specjalnego sterownika sprzêtowego do
dostêpu do karty graficznej - po prostu pobiera prostok±tne obszary od
serwera X. Oznacza to, ¿e trzeba mieæ szybk± maszynê (>= 133 MHz) i
szybki twardy dysk. Du¿e ramki (np. 384x288, czyli 1/2 PAL) z du¿ymi
FPS mo¿na przechwytywaæ tylko na bardzo bardzo szybkich systemach :-)

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--without-forced-embedded-ffmpeg
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_defaultdocdir},%{_mandir}/man1/}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_prefix}/doc/%{name}/INSTALL
mv $RPM_BUILD_ROOT%{_prefix}/doc/%{name} \
      $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}-%{version}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc %{_defaultdocdir}/%{name}-%{version}
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/glade
%{_datadir}/%{name}/glade/gnome-xvidcap.glade
%{_datadir}/%{name}/glade/xvidcap_logo.png
