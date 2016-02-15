#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : paramiko
Version  : 1.16.0
Release  : 15
URL      : https://pypi.python.org/packages/source/p/paramiko/paramiko-1.16.0.tar.gz
Source0  : https://pypi.python.org/packages/source/p/paramiko/paramiko-1.16.0.tar.gz
Summary  : SSH2 protocol library
Group    : Development/Tools
License  : LGPL-2.1
Requires: paramiko-python
BuildRequires : ecdsa
BuildRequires : ecdsa-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pycrypto-python
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
========
paramiko
========
:Paramiko: Python SSH module
:License: LGPL
:Homepage: https://github.com/paramiko/paramiko/
:API docs: http://docs.paramiko.org

%package python
Summary: python components for the paramiko package.
Group: Default
Requires: ecdsa-python
Requires: pycrypto-python

%description python
python components for the paramiko package.


%prep
%setup -q -n paramiko-1.16.0

%build
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
