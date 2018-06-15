#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : paramiko
Version  : 2.4.1
Release  : 40
URL      : https://github.com/paramiko/paramiko/archive/2.4.1.tar.gz
Source0  : https://github.com/paramiko/paramiko/archive/2.4.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: paramiko-python3
Requires: paramiko-python
Requires: bcrypt
Requires: cryptography
Requires: pyasn1
Requires: pynacl
BuildRequires : bcrypt
BuildRequires : cffi
BuildRequires : cryptography
BuildRequires : ecdsa
BuildRequires : ecdsa-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pyasn1
BuildRequires : pyasn1-modules
BuildRequires : pynacl

BuildRequires : python3-dev
BuildRequires : setuptools
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

%package python
Summary: python components for the paramiko package.
Group: Default
Requires: paramiko-python3

%description python
python components for the paramiko package.


%package python3
Summary: python3 components for the paramiko package.
Group: Default
Requires: python3-core

%description python3
python3 components for the paramiko package.


%prep
%setup -q -n paramiko-2.4.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523556827
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
