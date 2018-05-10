#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : thin-provisioning-tools
Version  : 0.7.6
Release  : 6
URL      : https://github.com/jthornber/thin-provisioning-tools/archive/v0.7.6.tar.gz
Source0  : https://github.com/jthornber/thin-provisioning-tools/archive/v0.7.6.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: thin-provisioning-tools-bin
Requires: thin-provisioning-tools-doc
BuildRequires : autoconf
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : boost-dev
BuildRequires : expat-dev
BuildRequires : libaio-dev
BuildRequires : libtool-dev
BuildRequires : sed

%description
Introduction
============
A suite of tools for manipulating the metadata of the dm-thin, dm-cache and
dm-era device-mapper targets.

%package bin
Summary: bin components for the thin-provisioning-tools package.
Group: Binaries

%description bin
bin components for the thin-provisioning-tools package.


%package doc
Summary: doc components for the thin-provisioning-tools package.
Group: Documentation

%description doc
doc components for the thin-provisioning-tools package.


%prep
%setup -q -n thin-provisioning-tools-0.7.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1525367322
%reconfigure --disable-static --enable-testing
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1525367322
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cache_check
/usr/bin/cache_dump
/usr/bin/cache_metadata_size
/usr/bin/cache_repair
/usr/bin/cache_restore
/usr/bin/cache_writeback
/usr/bin/era_check
/usr/bin/era_dump
/usr/bin/era_invalidate
/usr/bin/era_restore
/usr/bin/pdata_tools
/usr/bin/thin_check
/usr/bin/thin_delta
/usr/bin/thin_dump
/usr/bin/thin_ls
/usr/bin/thin_metadata_size
/usr/bin/thin_repair
/usr/bin/thin_restore
/usr/bin/thin_rmap
/usr/bin/thin_trim

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man8/*
