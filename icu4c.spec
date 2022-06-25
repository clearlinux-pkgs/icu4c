#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : icu4c
Version  : 70.1
Release  : 31
URL      : https://github.com/unicode-org/icu/releases/download/release-70-1/icu4c-70_1-src.tgz
Source0  : https://github.com/unicode-org/icu/releases/download/release-70-1/icu4c-70_1-src.tgz
Summary  : International Components for Unicode
Group    : Development/Tools
License  : BSD-3-Clause ICU NCSA
Requires: icu4c-bin = %{version}-%{release}
Requires: icu4c-data = %{version}-%{release}
Requires: icu4c-filemap = %{version}-%{release}
Requires: icu4c-lib = %{version}-%{release}
Requires: icu4c-license = %{version}-%{release}
Requires: icu4c-man = %{version}-%{release}
BuildRequires : doxygen
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : pkg-config
BuildRequires : sed

%description
ICU is a set of C and C++ libraries that provides robust and full-featured
Unicode and locale support. The library provides calendar support, conversions
for many character sets, language sensitive collation, date
and time formatting, support for many locales, message catalogs
and resources, message formatting, normalization, number and currency
formatting, time zones support, transliteration, word, line and
sentence breaking, etc.

This package contains the Unicode character database and derived
properties, along with converters and time zones data.

This package contains the runtime libraries for ICU. It does
not contain any of the data files needed at runtime and present in the
`icu' and `icu-locales` packages.

%package bin
Summary: bin components for the icu4c package.
Group: Binaries
Requires: icu4c-data = %{version}-%{release}
Requires: icu4c-license = %{version}-%{release}
Requires: icu4c-filemap = %{version}-%{release}

%description bin
bin components for the icu4c package.


%package data
Summary: data components for the icu4c package.
Group: Data

%description data
data components for the icu4c package.


%package dev
Summary: dev components for the icu4c package.
Group: Development
Requires: icu4c-lib = %{version}-%{release}
Requires: icu4c-bin = %{version}-%{release}
Requires: icu4c-data = %{version}-%{release}
Provides: icu4c-devel = %{version}-%{release}
Requires: icu4c = %{version}-%{release}

%description dev
dev components for the icu4c package.


%package dev32
Summary: dev32 components for the icu4c package.
Group: Default
Requires: icu4c-lib32 = %{version}-%{release}
Requires: icu4c-bin = %{version}-%{release}
Requires: icu4c-data = %{version}-%{release}
Requires: icu4c-dev = %{version}-%{release}

%description dev32
dev32 components for the icu4c package.


%package filemap
Summary: filemap components for the icu4c package.
Group: Default

%description filemap
filemap components for the icu4c package.


%package lib
Summary: lib components for the icu4c package.
Group: Libraries
Requires: icu4c-data = %{version}-%{release}
Requires: icu4c-license = %{version}-%{release}
Requires: icu4c-filemap = %{version}-%{release}

%description lib
lib components for the icu4c package.


%package lib32
Summary: lib32 components for the icu4c package.
Group: Default
Requires: icu4c-data = %{version}-%{release}
Requires: icu4c-license = %{version}-%{release}

%description lib32
lib32 components for the icu4c package.


%package license
Summary: license components for the icu4c package.
Group: Default

%description license
license components for the icu4c package.


%package man
Summary: man components for the icu4c package.
Group: Default

%description man
man components for the icu4c package.


%prep
%setup -q -n icu
cd %{_builddir}/icu
pushd ..
cp -a icu build32
popd
pushd ..
cp -a icu buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656126146
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used "
pushd source
%configure --disable-static
make  %{?_smp_mflags}
popd

pushd ../build32/source
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
unset PKG_CONFIG_PATH
pushd ../buildavx2/source
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
%configure --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
pushd source; make %{?_smp_mflags} check; popd

%install
export SOURCE_DATE_EPOCH=1656126146
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/icu4c
cp %{_builddir}/icu/LICENSE %{buildroot}/usr/share/package-licenses/icu4c/dbcb5c4a57f45a48c971c06928a7c99fb5656f06
cp %{_builddir}/icu/license.html %{buildroot}/usr/share/package-licenses/icu4c/06e7821c4127e21850f5c981698443b6f31e0ef1
pushd ../build32/source
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
if [ -d %{buildroot}/usr/share/pkgconfig ]
then
pushd %{buildroot}/usr/share/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
pushd ../buildavx2/source
%make_install_v3
popd
pushd source
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib32/icu/70.1/Makefile.inc
/usr/lib32/icu/70.1/pkgdata.inc
/usr/lib32/icu/Makefile.inc
/usr/lib32/icu/current
/usr/lib32/icu/pkgdata.inc
/usr/lib64/icu/70.1/Makefile.inc
/usr/lib64/icu/70.1/pkgdata.inc
/usr/lib64/icu/Makefile.inc
/usr/lib64/icu/current
/usr/lib64/icu/pkgdata.inc

%files bin
%defattr(-,root,root,-)
/usr/bin/derb
/usr/bin/escapesrc
/usr/bin/genbrk
/usr/bin/genccode
/usr/bin/gencfu
/usr/bin/gencmn
/usr/bin/gencnval
/usr/bin/gendict
/usr/bin/gennorm2
/usr/bin/genrb
/usr/bin/gensprep
/usr/bin/icu-config
/usr/bin/icuexportdata
/usr/bin/icuinfo
/usr/bin/icupkg
/usr/bin/makeconv
/usr/bin/pkgdata
/usr/bin/uconv
/usr/share/clear/optimized-elf/bin*

%files data
%defattr(-,root,root,-)
/usr/share/icu/70.1/LICENSE
/usr/share/icu/70.1/config/mh-linux
/usr/share/icu/70.1/install-sh
/usr/share/icu/70.1/mkinstalldirs

%files dev
%defattr(-,root,root,-)
/usr/include/unicode/alphaindex.h
/usr/include/unicode/appendable.h
/usr/include/unicode/basictz.h
/usr/include/unicode/brkiter.h
/usr/include/unicode/bytestream.h
/usr/include/unicode/bytestrie.h
/usr/include/unicode/bytestriebuilder.h
/usr/include/unicode/calendar.h
/usr/include/unicode/caniter.h
/usr/include/unicode/casemap.h
/usr/include/unicode/char16ptr.h
/usr/include/unicode/chariter.h
/usr/include/unicode/choicfmt.h
/usr/include/unicode/coleitr.h
/usr/include/unicode/coll.h
/usr/include/unicode/compactdecimalformat.h
/usr/include/unicode/curramt.h
/usr/include/unicode/currpinf.h
/usr/include/unicode/currunit.h
/usr/include/unicode/datefmt.h
/usr/include/unicode/dbbi.h
/usr/include/unicode/dcfmtsym.h
/usr/include/unicode/decimfmt.h
/usr/include/unicode/docmain.h
/usr/include/unicode/dtfmtsym.h
/usr/include/unicode/dtintrv.h
/usr/include/unicode/dtitvfmt.h
/usr/include/unicode/dtitvinf.h
/usr/include/unicode/dtptngen.h
/usr/include/unicode/dtrule.h
/usr/include/unicode/edits.h
/usr/include/unicode/enumset.h
/usr/include/unicode/errorcode.h
/usr/include/unicode/fieldpos.h
/usr/include/unicode/filteredbrk.h
/usr/include/unicode/fmtable.h
/usr/include/unicode/format.h
/usr/include/unicode/formattedvalue.h
/usr/include/unicode/fpositer.h
/usr/include/unicode/gender.h
/usr/include/unicode/gregocal.h
/usr/include/unicode/icudataver.h
/usr/include/unicode/icuplug.h
/usr/include/unicode/idna.h
/usr/include/unicode/listformatter.h
/usr/include/unicode/localebuilder.h
/usr/include/unicode/localematcher.h
/usr/include/unicode/localpointer.h
/usr/include/unicode/locdspnm.h
/usr/include/unicode/locid.h
/usr/include/unicode/measfmt.h
/usr/include/unicode/measunit.h
/usr/include/unicode/measure.h
/usr/include/unicode/messagepattern.h
/usr/include/unicode/msgfmt.h
/usr/include/unicode/normalizer2.h
/usr/include/unicode/normlzr.h
/usr/include/unicode/nounit.h
/usr/include/unicode/numberformatter.h
/usr/include/unicode/numberrangeformatter.h
/usr/include/unicode/numfmt.h
/usr/include/unicode/numsys.h
/usr/include/unicode/parseerr.h
/usr/include/unicode/parsepos.h
/usr/include/unicode/platform.h
/usr/include/unicode/plurfmt.h
/usr/include/unicode/plurrule.h
/usr/include/unicode/ptypes.h
/usr/include/unicode/putil.h
/usr/include/unicode/rbbi.h
/usr/include/unicode/rbnf.h
/usr/include/unicode/rbtz.h
/usr/include/unicode/regex.h
/usr/include/unicode/region.h
/usr/include/unicode/reldatefmt.h
/usr/include/unicode/rep.h
/usr/include/unicode/resbund.h
/usr/include/unicode/schriter.h
/usr/include/unicode/scientificnumberformatter.h
/usr/include/unicode/search.h
/usr/include/unicode/selfmt.h
/usr/include/unicode/simpleformatter.h
/usr/include/unicode/simpletz.h
/usr/include/unicode/smpdtfmt.h
/usr/include/unicode/sortkey.h
/usr/include/unicode/std_string.h
/usr/include/unicode/strenum.h
/usr/include/unicode/stringoptions.h
/usr/include/unicode/stringpiece.h
/usr/include/unicode/stringtriebuilder.h
/usr/include/unicode/stsearch.h
/usr/include/unicode/symtable.h
/usr/include/unicode/tblcoll.h
/usr/include/unicode/timezone.h
/usr/include/unicode/tmunit.h
/usr/include/unicode/tmutamt.h
/usr/include/unicode/tmutfmt.h
/usr/include/unicode/translit.h
/usr/include/unicode/tzfmt.h
/usr/include/unicode/tznames.h
/usr/include/unicode/tzrule.h
/usr/include/unicode/tztrans.h
/usr/include/unicode/ubidi.h
/usr/include/unicode/ubiditransform.h
/usr/include/unicode/ubrk.h
/usr/include/unicode/ucal.h
/usr/include/unicode/ucasemap.h
/usr/include/unicode/ucat.h
/usr/include/unicode/uchar.h
/usr/include/unicode/ucharstrie.h
/usr/include/unicode/ucharstriebuilder.h
/usr/include/unicode/uchriter.h
/usr/include/unicode/uclean.h
/usr/include/unicode/ucnv.h
/usr/include/unicode/ucnv_cb.h
/usr/include/unicode/ucnv_err.h
/usr/include/unicode/ucnvsel.h
/usr/include/unicode/ucol.h
/usr/include/unicode/ucoleitr.h
/usr/include/unicode/uconfig.h
/usr/include/unicode/ucpmap.h
/usr/include/unicode/ucptrie.h
/usr/include/unicode/ucsdet.h
/usr/include/unicode/ucurr.h
/usr/include/unicode/udat.h
/usr/include/unicode/udata.h
/usr/include/unicode/udateintervalformat.h
/usr/include/unicode/udatpg.h
/usr/include/unicode/udisplaycontext.h
/usr/include/unicode/uenum.h
/usr/include/unicode/ufieldpositer.h
/usr/include/unicode/uformattable.h
/usr/include/unicode/uformattedvalue.h
/usr/include/unicode/ugender.h
/usr/include/unicode/uidna.h
/usr/include/unicode/uiter.h
/usr/include/unicode/uldnames.h
/usr/include/unicode/ulistformatter.h
/usr/include/unicode/uloc.h
/usr/include/unicode/ulocdata.h
/usr/include/unicode/umachine.h
/usr/include/unicode/umisc.h
/usr/include/unicode/umsg.h
/usr/include/unicode/umutablecptrie.h
/usr/include/unicode/unifilt.h
/usr/include/unicode/unifunct.h
/usr/include/unicode/unimatch.h
/usr/include/unicode/unirepl.h
/usr/include/unicode/uniset.h
/usr/include/unicode/unistr.h
/usr/include/unicode/unorm.h
/usr/include/unicode/unorm2.h
/usr/include/unicode/unum.h
/usr/include/unicode/unumberformatter.h
/usr/include/unicode/unumberrangeformatter.h
/usr/include/unicode/unumsys.h
/usr/include/unicode/uobject.h
/usr/include/unicode/upluralrules.h
/usr/include/unicode/uregex.h
/usr/include/unicode/uregion.h
/usr/include/unicode/ureldatefmt.h
/usr/include/unicode/urename.h
/usr/include/unicode/urep.h
/usr/include/unicode/ures.h
/usr/include/unicode/uscript.h
/usr/include/unicode/usearch.h
/usr/include/unicode/uset.h
/usr/include/unicode/usetiter.h
/usr/include/unicode/ushape.h
/usr/include/unicode/uspoof.h
/usr/include/unicode/usprep.h
/usr/include/unicode/ustdio.h
/usr/include/unicode/ustream.h
/usr/include/unicode/ustring.h
/usr/include/unicode/ustringtrie.h
/usr/include/unicode/utext.h
/usr/include/unicode/utf.h
/usr/include/unicode/utf16.h
/usr/include/unicode/utf32.h
/usr/include/unicode/utf8.h
/usr/include/unicode/utf_old.h
/usr/include/unicode/utmscale.h
/usr/include/unicode/utrace.h
/usr/include/unicode/utrans.h
/usr/include/unicode/utypes.h
/usr/include/unicode/uvernum.h
/usr/include/unicode/uversion.h
/usr/include/unicode/vtzone.h
/usr/lib64/libicudata.so
/usr/lib64/libicui18n.so
/usr/lib64/libicuio.so
/usr/lib64/libicutest.so
/usr/lib64/libicutu.so
/usr/lib64/libicuuc.so
/usr/lib64/pkgconfig/icu-i18n.pc
/usr/lib64/pkgconfig/icu-io.pc
/usr/lib64/pkgconfig/icu-uc.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libicudata.so
/usr/lib32/libicui18n.so
/usr/lib32/libicuio.so
/usr/lib32/libicutest.so
/usr/lib32/libicutu.so
/usr/lib32/libicuuc.so
/usr/lib32/pkgconfig/32icu-i18n.pc
/usr/lib32/pkgconfig/32icu-io.pc
/usr/lib32/pkgconfig/32icu-uc.pc
/usr/lib32/pkgconfig/icu-i18n.pc
/usr/lib32/pkgconfig/icu-io.pc
/usr/lib32/pkgconfig/icu-uc.pc

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-icu4c

%files lib
%defattr(-,root,root,-)
/usr/lib64/glibc-hwcaps/x86-64-v3/libicudata.so
/usr/lib64/glibc-hwcaps/x86-64-v3/libicudata.so.70
/usr/lib64/glibc-hwcaps/x86-64-v3/libicudata.so.70.1
/usr/lib64/glibc-hwcaps/x86-64-v3/libicui18n.so
/usr/lib64/glibc-hwcaps/x86-64-v3/libicui18n.so.70
/usr/lib64/glibc-hwcaps/x86-64-v3/libicui18n.so.70.1
/usr/lib64/glibc-hwcaps/x86-64-v3/libicuio.so
/usr/lib64/glibc-hwcaps/x86-64-v3/libicuio.so.70
/usr/lib64/glibc-hwcaps/x86-64-v3/libicuio.so.70.1
/usr/lib64/glibc-hwcaps/x86-64-v3/libicutest.so
/usr/lib64/glibc-hwcaps/x86-64-v3/libicutest.so.70
/usr/lib64/glibc-hwcaps/x86-64-v3/libicutest.so.70.1
/usr/lib64/glibc-hwcaps/x86-64-v3/libicutu.so
/usr/lib64/glibc-hwcaps/x86-64-v3/libicutu.so.70
/usr/lib64/glibc-hwcaps/x86-64-v3/libicutu.so.70.1
/usr/lib64/glibc-hwcaps/x86-64-v3/libicuuc.so
/usr/lib64/glibc-hwcaps/x86-64-v3/libicuuc.so.70
/usr/lib64/glibc-hwcaps/x86-64-v3/libicuuc.so.70.1
/usr/lib64/libicudata.so.70
/usr/lib64/libicudata.so.70.1
/usr/lib64/libicui18n.so.70
/usr/lib64/libicui18n.so.70.1
/usr/lib64/libicuio.so.70
/usr/lib64/libicuio.so.70.1
/usr/lib64/libicutest.so.70
/usr/lib64/libicutest.so.70.1
/usr/lib64/libicutu.so.70
/usr/lib64/libicutu.so.70.1
/usr/lib64/libicuuc.so.70
/usr/lib64/libicuuc.so.70.1

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libicudata.so.70
/usr/lib32/libicudata.so.70.1
/usr/lib32/libicui18n.so.70
/usr/lib32/libicui18n.so.70.1
/usr/lib32/libicuio.so.70
/usr/lib32/libicuio.so.70.1
/usr/lib32/libicutest.so.70
/usr/lib32/libicutest.so.70.1
/usr/lib32/libicutu.so.70
/usr/lib32/libicutu.so.70.1
/usr/lib32/libicuuc.so.70
/usr/lib32/libicuuc.so.70.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/icu4c/06e7821c4127e21850f5c981698443b6f31e0ef1
/usr/share/package-licenses/icu4c/dbcb5c4a57f45a48c971c06928a7c99fb5656f06

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/derb.1
/usr/share/man/man1/genbrk.1
/usr/share/man/man1/gencfu.1
/usr/share/man/man1/gencnval.1
/usr/share/man/man1/gendict.1
/usr/share/man/man1/genrb.1
/usr/share/man/man1/icu-config.1
/usr/share/man/man1/icuexportdata.1
/usr/share/man/man1/makeconv.1
/usr/share/man/man1/pkgdata.1
/usr/share/man/man1/uconv.1
/usr/share/man/man8/genccode.8
/usr/share/man/man8/gencmn.8
/usr/share/man/man8/gensprep.8
/usr/share/man/man8/icupkg.8
