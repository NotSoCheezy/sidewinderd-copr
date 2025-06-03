%global srcname sidewinderd

Name: sidewinderd
Version: 0.4.4
Release: 2%{?dist}
License: MIT
Summary: This project provides support for gaming peripherals under Linux.
Url: https://github.com/tolga9009/%{srcname}
Source0: %{srcname}-%{version}.tar.gz

#ExclusiveArch: x86_64
#BuildArch: noarch

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: g++
BuildRequires: libconfig-devel
BuildRequires: tinyxml2-devel
BuildRequires: libudev-devel

%description
This project provides support for gaming peripherals under Linux. It was originally designed for the Microsoft SideWinder X4, but we have extended support for more keyboards. Our goal is to create a framework-like environment for rapid driver development under Linux.

#-- PREP, BUILD & INSTALL -----------------------------------------------------#
%prep
#%autosetup
%setup -q

%build
cmake .
make

%install
make install DESTDIR=%{buildroot}

#-- FILES ---------------------------------------------------------------------#
%files
#%doc README.md
#%license LICENSE
%{_exec_prefix}/local/bin/sidewinderd
%{_exec_prefix}/local/lib/systemd/system/sidewinderd.service
%{_sysconfdir}/sidewinderd.conf

#-- CHANGELOG -----------------------------------------------------------------#
%changelog
* Mon Jun 02 2025 NotSoCheezy <redacted@gmail.com> - 0.4.4-2
- Initial package

