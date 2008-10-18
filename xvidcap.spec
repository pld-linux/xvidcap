#
# Conditional build:
%bcond_without	system_ffmpeg		# use system ffmpeg
#
Summary:	XVidCap - Video Capture for X
Summary(pl.UTF-8):	XVidCap - przechwytywanie obrazu dla X
Name:		xvidcap
Version:	1.1.7
Release:	3
Epoch:		1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://dl.sourceforge.net/xvidcap/%{name}-%{version}.tar.gz
# Source0-md5:	b39a682d3ef9fcbf424af771936780e2
Patch0:		%{name}-ffmpeg.patch
URL:		http://xvidcap.sourceforge.net/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	dbus-glib-devel
%{?with_system_ffmpeg:BuildRequires:	ffmpeg-devel >= 0.4.9-3.20050806}
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	intltool
BuildRequires:	libglade2-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.198
BuildRequires:	scrollkeeper
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	zlib-devel
Requires(post,postun):	scrollkeeper
Suggests:	mplayer
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Capture parts of your screen to single files for every frame or to an
MPEG stream.

This program does not use a special hardware driver to access the
video card. It just asks the X server about rectangular areas. This
means you need a fast machine (>= 133 MHz) and a fast harddrive. Big
frames (e.g. 384x288 = 1/2 PAL) at a high FPS rate are only possible
with very very fast systems :-)

%description -l pl.UTF-8
Ten pakiet służy do przechwytywania ekranu do pojedynczych plików z
każdą ramką lub strumienia MPEG.

Program nie używa żadnego specjalnego sterownika sprzętowego do
dostępu do karty graficznej - po prostu pobiera prostokątne obszary od
serwera X. Oznacza to, że trzeba mieć szybką maszynę (>= 133 MHz) i
szybki twardy dysk. Duże ramki (np. 384x288, czyli 1/2 PAL) z dużymi
FPS można przechwytywać tylko na bardzo bardzo szybkich systemach :-)

%prep
%setup -q
%patch0 -p1

%build
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?with_system_ffmpeg:--without-forced-embedded-ffmpeg}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_docdir},%{_mandir}/man1}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post

%postun
%scrollkeeper_update_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog README TODO.tasks
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%attr(755,root,root) %{_datadir}/%{name}/ppm2mpeg.sh
%dir %{_datadir}/%{name}/glade
%{_datadir}/%{name}/glade/gnome-xvidcap.glade
%{_datadir}/%{name}/glade/xvidcap_logo.png
%{_datadir}/dbus-1/services/net.jarre_de_the.Xvidcap.service
%{_mandir}/man1/xvidcap.1*
%{_mandir}/man1/xvidcap-dbus-client.1*
%lang(de) %{_mandir}/de/man1/xvidcap.1*
%lang(de) %{_mandir}/de/man1/xvidcap-dbus-client.1*
%lang(es) %{_mandir}/es/man1/xvidcap.1*
%lang(it) %{_mandir}/it/man1/xvidcap.1*
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
