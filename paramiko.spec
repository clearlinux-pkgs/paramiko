#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : paramiko
Version  : 2.0.2
Release  : 20
URL      : http://pypi.debian.net/paramiko/paramiko-2.0.2.tar.gz
Source0  : http://pypi.debian.net/paramiko/paramiko-2.0.2.tar.gz
Summary  : SSH2 protocol library
Group    : Development/Tools
License  : LGPL-2.1
Requires: paramiko-python
BuildRequires : cffi
BuildRequires : cryptography
BuildRequires : ecdsa
BuildRequires : ecdsa-python
BuildRequires : enum34-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pyasn1
BuildRequires : pyasn1-modules
BuildRequires : pycrypto-python
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six
BuildRequires : six-python

%description
========
Paramiko
========
.. Continuous integration and code coverage badges
.. image:: https://travis-ci.org/paramiko/paramiko.svg?branch=master
:target: https://travis-ci.org/paramiko/paramiko
.. image:: https://coveralls.io/repos/paramiko/paramiko/badge.svg?branch=master&service=github
:target: https://coveralls.io/github/paramiko/paramiko?branch=master

%package python
Summary: python components for the paramiko package.
Group: Default
Requires: cryptography

%description python
python components for the paramiko package.


%prep
%setup -q -n paramiko-2.0.2

%build
export LANG=C
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python test.py
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
