#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : thin-provisioning-tools
Version  : 0.8.5
Release  : 10
URL      : https://github.com/jthornber/thin-provisioning-tools/archive/v0.8.5/thin-provisioning-tools-0.8.5.tar.gz
Source0  : https://github.com/jthornber/thin-provisioning-tools/archive/v0.8.5/thin-provisioning-tools-0.8.5.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: thin-provisioning-tools-bin = %{version}-%{release}
Requires: thin-provisioning-tools-license = %{version}-%{release}
Requires: thin-provisioning-tools-man = %{version}-%{release}
BuildRequires : autoconf
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : boost-dev
BuildRequires : expat-dev
BuildRequires : libaio-dev
BuildRequires : libtool-dev
BuildRequires : sed
Patch1: resolve_functionname_conflict.patch

%description
Introduction
============
A suite of tools for manipulating the metadata of the dm-thin, dm-cache and
dm-era device-mapper targets.

%package bin
Summary: bin components for the thin-provisioning-tools package.
Group: Binaries
Requires: thin-provisioning-tools-license = %{version}-%{release}

%description bin
bin components for the thin-provisioning-tools package.


%package license
Summary: license components for the thin-provisioning-tools package.
Group: Default

%description license
license components for the thin-provisioning-tools package.


%package man
Summary: man components for the thin-provisioning-tools package.
Group: Default

%description man
man components for the thin-provisioning-tools package.


%prep
%setup -q -n thin-provisioning-tools-0.8.5
cd %{_builddir}/thin-provisioning-tools-0.8.5
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1592660215
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%reconfigure --disable-static --enable-testing
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1592660215
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/thin-provisioning-tools
cp %{_builddir}/thin-provisioning-tools-0.8.5/COPYING %{buildroot}/usr/share/package-licenses/thin-provisioning-tools/8624bcdae55baeef00cd11d5dfcfa60f68710a02
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

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/thin-provisioning-tools/8624bcdae55baeef00cd11d5dfcfa60f68710a02

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/cache_check.8
/usr/share/man/man8/cache_dump.8
/usr/share/man/man8/cache_metadata_size.8
/usr/share/man/man8/cache_repair.8
/usr/share/man/man8/cache_restore.8
/usr/share/man/man8/cache_writeback.8
/usr/share/man/man8/era_check.8
/usr/share/man/man8/era_dump.8
/usr/share/man/man8/era_invalidate.8
/usr/share/man/man8/era_restore.8
/usr/share/man/man8/thin_check.8
/usr/share/man/man8/thin_delta.8
/usr/share/man/man8/thin_dump.8
/usr/share/man/man8/thin_ls.8
/usr/share/man/man8/thin_metadata_size.8
/usr/share/man/man8/thin_repair.8
/usr/share/man/man8/thin_restore.8
/usr/share/man/man8/thin_rmap.8
/usr/share/man/man8/thin_trim.8
