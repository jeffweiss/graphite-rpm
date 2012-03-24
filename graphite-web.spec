%define name graphite-web
%define version 0.9.9
%define unmangled_version 0.9.9
%define release 1

Summary: Enterprise scalable realtime graphing
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.gz
License: Apache Software License 2.0
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Chris Davis <chrismd@gmail.com>
Url: https://launchpad.net/graphite
Requires: carbon whisper django-tagging bitmap bitmap-fonts-compat pycairo python-sqlite2 python-zope-interface Django

%description
UNKNOWN

%prep
%setup -n %{name}-%{unmangled_version}

%build
python setup.py build

%install
python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
