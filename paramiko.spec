#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x9C29BC560041E930 (jeff@bitprophet.org)
#
Name     : paramiko
Version  : 2.2.1
Release  : 32
URL      : http://pypi.debian.net/paramiko/paramiko-2.2.1.tar.gz
Source0  : http://pypi.debian.net/paramiko/paramiko-2.2.1.tar.gz
Source99 : http://pypi.debian.net/paramiko/paramiko-2.2.1.tar.gz.asc
Summary  : SSH2 protocol library
Group    : Development/Tools
License  : LGPL-2.1
Requires: paramiko-legacypython
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
BuildRequires : enum34
BuildRequires : ipaddress-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pyasn1
BuildRequires : pyasn1-modules
BuildRequires : pycrypto-python
BuildRequires : pynacl
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
This is a library for making SSH2 connections (client or server).
        Emphasis is on using SSH2 as an alternative to SSL for making secure
        connections between python scripts.  All major ciphers and hash methods
        are supported.  SFTP client and server mode are both supported too.

%package legacypython
Summary: legacypython components for the paramiko package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the paramiko package.


%package python
Summary: python components for the paramiko package.
Group: Default
Requires: paramiko-legacypython
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
%setup -q -n paramiko-2.2.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507163633
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python test.py
%install
export SOURCE_DATE_EPOCH=1507163633
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
