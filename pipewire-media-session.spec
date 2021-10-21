Summary:	Example session manager for PipeWire
Name:		pipewire-media-session
Version:	0.4.0
Release:	1
License:	MIT
Group:		Libraries
Source0:	https://gitlab.freedesktop.org/pipewire/media-session/-/archive/%{version}/media-session-%{version}.tar.bz2
# Source0-md5:	079d951f7bc3383ddb11d2b34d0cdb32
URL:		https://pipewire.org/
BuildRequires:	alsa-lib-devel >= 1.1.7
BuildRequires:	dbus-devel
BuildRequires:	doxygen
BuildRequires:	gettext-tools
BuildRequires:	meson >= 0.56.0
BuildRequires:	ninja
BuildRequires:	pipewire-devel >= 0.3.39
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	systemd-devel
Requires:	pipewire-libs >= 0.3.39
Provides:	pipewire-session-manager
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PipeWire Media Session is an example session manager for PipeWire.

%prep
%setup -q -n media-session-%{version}

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang media-session

%clean
rm -rf $RPM_BUILD_ROOT

%files -f media-session.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pipewire-media-session
%{systemduserunitdir}/pipewire-media-session.service
%dir %{_datadir}/pipewire/media-session.d
%{_datadir}/pipewire/media-session.d/media-session.conf
%{_datadir}/pipewire/media-session.d/v4l2-monitor.conf
%{_datadir}/pipewire/media-session.d/alsa-monitor.conf
%{_datadir}/pipewire/media-session.d/bluez-monitor.conf
%{_datadir}/pipewire/media-session.d/with-jack
%{_datadir}/pipewire/media-session.d/with-pulseaudio
