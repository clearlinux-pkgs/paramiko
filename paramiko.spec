#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : paramiko
Version  : 2.4.2
Release  : 61
URL      : https://github.com/paramiko/paramiko/archive/2.4.2.tar.gz
Source0  : https://github.com/paramiko/paramiko/archive/2.4.2.tar.gz
Summary  : SSH2 protocol library
Group    : Development/Tools
License  : LGPL-2.1
Requires: paramiko-license = %{version}-%{release}
Requires: paramiko-python = %{version}-%{release}
Requires: paramiko-python3 = %{version}-%{release}
Requires: PyNaCl
Requires: bcrypt
Requires: cryptography
Requires: pyasn1
BuildRequires : PyNaCl
BuildRequires : bcrypt
BuildRequires : buildreq-distutils3
BuildRequires : cffi
BuildRequires : cryptography
BuildRequires : ecdsa
BuildRequires : ecdsa-python
BuildRequires : pyasn1
BuildRequires : pyasn1-modules
BuildRequires : setuptools-python

%description
========
Paramiko
========
.. Continuous integration and code coverage badges
.. image:: https://travis-ci.org/paramiko/paramiko.svg?branch=master
:target: https://travis-ci.org/paramiko/paramiko
.. image:: https://codecov.io/gh/paramiko/paramiko/branch/master/graph/badge.svg
:target: https://codecov.io/gh/paramiko/paramiko

%package license
Summary: license components for the paramiko package.
Group: Default

%description license
license components for the paramiko package.


%package python
Summary: python components for the paramiko package.
Group: Default
Requires: paramiko-python3 = %{version}-%{release}

%description python
python components for the paramiko package.


%package python3
Summary: python3 components for the paramiko package.
Group: Default
Requires: python3-core
Provides: pypi(paramiko)
Requires: pypi(bcrypt)
Requires: pypi(cryptography)
Requires: pypi(pynacl)

%description python3
python3 components for the paramiko package.


%prep
%setup -q -n paramiko-2.4.2
cd %{_builddir}/paramiko-2.4.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603397600
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/paramiko
cp %{_builddir}/paramiko-2.4.2/LICENSE %{buildroot}/usr/share/package-licenses/paramiko/b12c713656a9b98b6980a52bb068154cfdcbdd99
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/paramiko/b12c713656a9b98b6980a52bb068154cfdcbdd99

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
