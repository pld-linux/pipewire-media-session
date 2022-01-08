#
# Conditional build:
%bcond_without	apidocs		# Doxygen based documentation

Summary:	Example session manager for PipeWire
Name:		pipewire-media-session
Version:	0.4.1
Release:	3
License:	MIT
Group:		Libraries
Source0:	https://gitlab.freedesktop.org/pipewire/media-session/-/archive/%{version}/media-session-%{version}.tar.bz2
# Source0-md5:	5f6d9e82330c8102f97b099f5269286f
URL:		https://pipewire.org/
BuildRequires:	alsa-lib-devel >= 1.1.7
BuildRequires:	dbus-devel
%{?with_apidocs:BuildRequires:	doxygen}
BuildRequires:	gettext-tools
BuildRequires:	meson >= 0.56.0
BuildRequires:	ninja
BuildRequires:	pipewire-devel >= 0.3.39
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 2.011
BuildRequires:	systemd-devel
Requires(post,preun):	systemd-units >= 250.1
Requires:	pipewire-libs >= 0.3.39
Requires:	systemd-units >= 250.1
Provides:	pipewire-session-manager
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PipeWire Media Session is an example session manager for PipeWire.

%package apidocs
Summary:	API documentation for PipeWire Media Session
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for PipeWire Media Session.

%prep
%setup -q -n media-session-%{version}

%build
%meson build \
	-Ddocs=%{__enabled_disabled apidocs}

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

# packaged as %doc in -apidocs
%{?with_apidocs:%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/media-session/html}

%find_lang media-session

%clean
rm -rf $RPM_BUILD_ROOT

%post
%systemd_user_post pipewire-media-session.service

%preun
%systemd_user_preun pipewire-media-session.service

%files -f media-session.lang
%defattr(644,root,root,755)
%doc NEWS README.md
%attr(755,root,root) %{_bindir}/pipewire-media-session
%{systemduserunitdir}/pipewire-media-session.service
%dir %{_datadir}/pipewire/media-session.d
%{_datadir}/pipewire/media-session.d/media-session.conf
%{_datadir}/pipewire/media-session.d/v4l2-monitor.conf
%{_datadir}/pipewire/media-session.d/alsa-monitor.conf
%{_datadir}/pipewire/media-session.d/bluez-monitor.conf
%{_datadir}/pipewire/media-session.d/with-jack
%{_datadir}/pipewire/media-session.d/with-pulseaudio

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%doc build/doc/html/*
%endif
