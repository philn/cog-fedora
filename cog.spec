Name:           cog
Version:        0.18.4
Release:        1%{?dist}
Summary:        WPE launcher and webapp container

License:        MIT
URL:            https://github.com/igalia/cog
Source0:        https://wpewebkit.org/releases/%{name}-%{version}.tar.xz

BuildRequires: wpewebkit-devel
BuildRequires: gtk4-devel
BuildRequires: wpebackend-fdo-devel
BuildRequires: libepoxy-devel
BuildRequires: libdrm-devel
BuildRequires: libinput-devel
BuildRequires: libudev-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: cairo-devel
BuildRequires: egl-wayland-devel
BuildRequires: mesa-libgbm-devel
BuildRequires: wayland-devel
BuildRequires: wayland-protocols-devel
BuildRequires: gi-docgen
BuildRequires: meson
BuildRequires: gcc
BuildRequires: libmanette-devel

%description
Cog is a small single “window” launcher for the WebKit WPE port. It is small,
provides an optional user interface, and is suitable to be used as a Web
application container. The “window” may be fullscreen depending on the WPE
backend being used.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries, build data, and header
files for developing applications that use %{name}

%prep
%autosetup -p1 -n cog-%{version}

%build
%meson -Dplatforms=drm,headless,wayland,gtk4,x11

%meson_build

%install
%meson_install

%files
%{_bindir}/cog
%{_bindir}/cogctl
%{_libdir}/cog/modules
%{_libdir}/libcogcore.*

%files devel
%{_includedir}/cog
%{_libdir}/pkgconfig/*.pc

%doc NEWS
%{_mandir}/man1/cog*

%license COPYING

%changelog
%autochangelog
