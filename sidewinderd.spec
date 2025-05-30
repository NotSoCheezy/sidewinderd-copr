%global srcname sidewinderd

Name: sidewinderd
Version: 0.4.4
Release: 1%{?dist}
License: MIT
Summary: This project provides support for gaming peripherals under Linux.
Url: https://github.com/tolga9009/%{srcname}
Source0: %{name}-%{version}.tar.gz

BuildArch: noarch

BuildRequires: cmake
BuildRequires: libconfig-devel
BuildRequires: tinyxml2-devel
BuildRequires: libudev-devel

%description
This project provides support for gaming peripherals under Linux. It was originally designed for the Microsoft SideWinder X4, but we have extended support for more keyboards. Our goal is to create a framework-like environment for rapid driver development under Linux.

#-- PREP, BUILD & INSTALL -----------------------------------------------------#
%prep
%autosetup

%build
%py3_build

%install
%py3_install

#-- FILES ---------------------------------------------------------------------#
%files
#%doc README.md
%license LICENSE
%{_bindir}/sidewinderd

#-- CHANGELOG -----------------------------------------------------------------#
%changelog



