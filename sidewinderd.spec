%global srcname sidewinderd

Name: sidewinderd
Version: 0.4.4
Release: 1%{?dist}
License: MIT
Summary: This project provides support for gaming peripherals under Linux.
Url: https://github.com/tolga9009/%{srcname}
Source0: %{name}-%{version}.tar.gz

BuildArch: x86_64
#BuildArch: noarch

BuildRequires: cmake
BuildRequires: libconfig-devel
BuildRequires: tinyxml2-devel
BuildRequires: libudev-devel

%description
This project provides support for gaming peripherals under Linux. It was originally designed for the Microsoft SideWinder X4, but we have extended support for more keyboards. Our goal is to create a framework-like environment for rapid driver development under Linux.

#-- PREP, BUILD & INSTALL -----------------------------------------------------#
%prep
%autosetup
mkdir build

%build
cd build
cmake ..
make

%install
make install

#-- FILES ---------------------------------------------------------------------#
%files
#%doc README.md
%license LICENSE
%{_bindir}/sidewinderd

#-- CHANGELOG -----------------------------------------------------------------#
%changelog
* Fri May 30 2025 Cassandra Erica <cheezy> 0.4.4-1
