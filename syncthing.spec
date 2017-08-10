# Generate devel rpm
%global with_devel 1

# Build project from bundled dependencies
%if 0%{?rhel}
%global with_bundled 1
%else
%global with_bundled 0
%endif

# Build with debug info rpm
%global with_debug 1

# Run tests in check section
%global with_check 1

# Generate unit-test rpm
%global with_unit_test 1

# Build server tools
%global with_tools 1


%if 0%{?with_debug}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif

%global provider        github
%global provider_tld    com
%global project         syncthing
%global repo            syncthing
%global long_name       golang-%{provider}-%{project}-%{repo}
# https://github.com/syncthing/syncthing
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global commit          1fc2ab444b3a3bf2ab1e2e2a9e5f1f4987103b00
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

# commit 1fc2ab444b3a3bf2ab1e2e2a9e5f1f4987103b00 == version 0.14.35


Name:           syncthing
Summary:        Continuous File Synchronization
Version:        0.14.35
Release:        2%{?dist}

# syncthing (MPLv2.0) bundles angular (MIT), bootstrap (MIT), and font-awesome (MIT/OFL)
License:        MPLv2.0 and MIT and OFL

URL:            https://syncthing.net
Source0:        https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-source-v%{version}.tar.gz

# Patch build.go script so go build doesn't install deps
# and produces debug-enabled binaries for rpm
Patch0:         00-go-build-flags.patch

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 aarch64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}

BuildRequires:  systemd
%{?systemd_requires}

%if ! 0%{?with_bundled}
BuildRequires:  golang(github.com/AudriusButkevicius/go-nat-pmp)
BuildRequires:  golang(github.com/AudriusButkevicius/pfilter)
BuildRequires:  golang(github.com/bkaradzic/go-lz4)
BuildRequires:  golang(github.com/calmh/du)
BuildRequires:  golang(github.com/calmh/luhn)
BuildRequires:  golang(github.com/calmh/xdr)
BuildRequires:  golang(github.com/ccding/go-stun/stun)
BuildRequires:  golang(github.com/chmduquesne/rollinghash/adler32)
BuildRequires:  golang(github.com/gobwas/glob)
BuildRequires:  golang(github.com/gogo/protobuf/gogoproto)
BuildRequires:  golang(github.com/gogo/protobuf/proto)
BuildRequires:  golang(github.com/jackpal/gateway)
BuildRequires:  golang(github.com/kardianos/osext)
BuildRequires:  golang(github.com/minio/sha256-simd)
BuildRequires:  golang(github.com/rcrowley/go-metrics)
BuildRequires:  golang(github.com/sasha-s/go-deadlock)
BuildRequires:  golang(github.com/syndtr/goleveldb/leveldb)
BuildRequires:  golang(github.com/syndtr/goleveldb/leveldb/errors)
BuildRequires:  golang(github.com/syndtr/goleveldb/leveldb/iterator)
BuildRequires:  golang(github.com/syndtr/goleveldb/leveldb/opt)
BuildRequires:  golang(github.com/syndtr/goleveldb/leveldb/storage)
BuildRequires:  golang(github.com/syndtr/goleveldb/leveldb/util)
BuildRequires:  golang(github.com/thejerf/suture)
BuildRequires:  golang(github.com/vitrun/qart)
BuildRequires:  golang(github.com/xtaci/kcp-go)
BuildRequires:  golang(github.com/xtaci/smux)
BuildRequires:  golang(golang.org/x/net/context)
BuildRequires:  golang(golang.org/x/net/ipv4)
BuildRequires:  golang(golang.org/x/net/ipv6)
BuildRequires:  golang(golang.org/x/net/proxy)
BuildRequires:  golang(golang.org/x/text/unicode/norm)
BuildRequires:  golang(golang.org/x/time/rate)
%endif

Provides:       %{long_name} = %{version}-%{release}

Provides:       bundled(angular) = 1.2.9
Provides:       bundled(angular-dirPagination) = 759009c
Provides:       bundled(angular-translate) = 2.9.0.1
Provides:       bundled(angular-translate-loader-static-files) = 2.11.0
Provides:       bundled(bootstrap) = 3.3.5
Provides:       bundled(font-awesome) = 4.5.0
Provides:       bundled(jquery) = 2.2.2


%description
Syncthing replaces other file synchronization services with something
open, trustworthy and decentralized. Your data is your data alone and
you deserve to choose where it is stored, if it is shared with some
third party and how it's transmitted over the Internet.

Using syncthing, that control is returned to you.


%if 0%{?with_devel}
%package        devel
Summary:        Continuous File Synchronization (development files)
Provides:       %{long_name}-devel = %{version}-%{release}
BuildArch:      noarch

Requires:       golang(github.com/AudriusButkevicius/go-nat-pmp)
Requires:       golang(github.com/AudriusButkevicius/pfilter)
Requires:       golang(github.com/bkaradzic/go-lz4)
Requires:       golang(github.com/calmh/du)
Requires:       golang(github.com/calmh/luhn)
Requires:       golang(github.com/calmh/xdr)
Requires:       golang(github.com/ccding/go-stun/stun)
Requires:       golang(github.com/chmduquesne/rollinghash/adler32)
Requires:       golang(github.com/gobwas/glob)
Requires:       golang(github.com/gogo/protobuf/gogoproto)
Requires:       golang(github.com/gogo/protobuf/proto)
Requires:       golang(github.com/jackpal/gateway)
Requires:       golang(github.com/kardianos/osext)
Requires:       golang(github.com/minio/sha256-simd)
Requires:       golang(github.com/rcrowley/go-metrics)
Requires:       golang(github.com/sasha-s/go-deadlock)
Requires:       golang(github.com/syndtr/goleveldb/leveldb)
Requires:       golang(github.com/syndtr/goleveldb/leveldb/errors)
Requires:       golang(github.com/syndtr/goleveldb/leveldb/iterator)
Requires:       golang(github.com/syndtr/goleveldb/leveldb/opt)
Requires:       golang(github.com/syndtr/goleveldb/leveldb/storage)
Requires:       golang(github.com/syndtr/goleveldb/leveldb/util)
Requires:       golang(github.com/thejerf/suture)
Requires:       golang(github.com/vitrun/qart)
Requires:       golang(github.com/xtaci/kcp-go)
Requires:       golang(github.com/xtaci/smux)
Requires:       golang(golang.org/x/net/context)
Requires:       golang(golang.org/x/net/ipv4)
Requires:       golang(golang.org/x/net/ipv6)
Requires:       golang(golang.org/x/net/proxy)
Requires:       golang(golang.org/x/text/unicode/norm)
Requires:       golang(golang.org/x/time/rate)

Provides:       golang(%{import_path}/lib/auto) = %{version}-%{release}
Provides:       golang(%{import_path}/lib/beacon) = %{version}-%{release}
Provides:       golang(%{import_path}/lib/config) = %{version}-%{release}
Provides:       golang(%{import_path}/lib/connections) = %{version}-%{release}
Provides:       golang(%{import_path}/lib/db) = %{version}-%{release}
Provides:       golang(%{import_path}/lib/dialer) = %{version}-%{release}
Provides:       golang(%{import_path}/lib/discover) = %{version}-%{release}
Provides:       golang(%{import_path}/lib/events) = %{version}-%{release}
Provides:       golang(%{import_path}/lib/fs) = %{version}-%{release}
Provides:       golang(%{import_path}/lib/ignore) = %{version}-%{release}
Provides:       golang(%{import_path}/lib/logger) = %{version}-%{release}
Provides:       golang(%{import_path}/lib/model) = %{version}-%{release}
Provides:       golang(%{import_path}/lib/nat) = %{version}-%{release}
Provides:       golang(%{import_path}/lib/osutil) = %{version}-%{release}
Provides:       golang(%{import_path}/lib/pmp) = %{version}-%{release}
Provides:       golang(%{import_path}/lib/protocol) = %{version}-%{release}
Provides:       golang(%{import_path}/lib/rand) = %{version}-%{release}
Provides:       golang(%{import_path}/lib/rc) = %{version}-%{release}
Provides:       golang(%{import_path}/lib/relay/client) = %{version}-%{release}
Provides:       golang(%{import_path}/lib/relay/protocol) = %{version}-%{release}
Provides:       golang(%{import_path}/lib/scanner) = %{version}-%{release}
Provides:       golang(%{import_path}/lib/sha256) = %{version}-%{release}
Provides:       golang(%{import_path}/lib/signature) = %{version}-%{release}
Provides:       golang(%{import_path}/lib/stats) = %{version}-%{release}
Provides:       golang(%{import_path}/lib/sync) = %{version}-%{release}
Provides:       golang(%{import_path}/lib/tlsutil) = %{version}-%{release}
Provides:       golang(%{import_path}/lib/upgrade) = %{version}-%{release}
Provides:       golang(%{import_path}/lib/upnp) = %{version}-%{release}
Provides:       golang(%{import_path}/lib/util) = %{version}-%{release}
Provides:       golang(%{import_path}/lib/versioner) = %{version}-%{release}
Provides:       golang(%{import_path}/lib/weakhash) = %{version}-%{release}

%if 0%{?with_bundled}
Provides:       bundled(golang(github.com/AudriusButkevicius/cli)) = 7f561c78b5a4aad858d9fd550c92b5da6d55efbb
Provides:       bundled(golang(github.com/AudriusButkevicius/go-nat-pmp)) = 452c97607362b2ab5a7839b8d1704f0396b640ca
Provides:       bundled(golang(github.com/AudriusButkevicius/pfilter)) = 09b3cfdd04de89f0196caecb0b335d7149a6593a
Provides:       bundled(golang(github.com/bkaradzic/go-lz4)) = 7224d8d8f27ef618c0a95f1ae69dbb0488abc33a
Provides:       bundled(golang(github.com/calmh/du)) = dd9dc2043353249b2910b29dcfd6f6d4e64f39be
Provides:       bundled(golang(github.com/calmh/luhn)) = 0c8388ff95fa92d4094011e5a04fc99dea3d1632
Provides:       bundled(golang(github.com/calmh/xdr)) = 08e072f9cb164f943a92eb59f90f3abc64ac6e8f
Provides:       bundled(golang(github.com/ccding/go-stun/stun)) = 04a4eed61c57ecc9903f8983d1d2c17b88d2e9e1
Provides:       bundled(golang(github.com/chmduquesne/rollinghash)) = 043b8fdecc9816f0011a056f6d92f9a091ab63dd
Provides:       bundled(golang(github.com/cznic/b)) = aaaa43c92e509a827e63540510bc94c3003ef2e1
Provides:       bundled(golang(github.com/cznic/fileutil)) = 90cf820aafe8f7df39416fdbb932029ff99bd1ab
Provides:       bundled(golang(github.com/cznic/internal/buffer)) = e5e1c3e9165d0a72507c2bbb0ffac1c02b8d3f7c
Provides:       bundled(golang(github.com/cznic/internal/file)) = e5e1c3e9165d0a72507c2bbb0ffac1c02b8d3f7c
Provides:       bundled(golang(github.com/cznic/internal/slice)) = e5e1c3e9165d0a72507c2bbb0ffac1c02b8d3f7c
Provides:       bundled(golang(github.com/cznic/lldb)) = bea8611dd5c407f3c5eab9f9c68e887a27dc6f0e
Provides:       bundled(golang(github.com/cznic/mathutil)) = 1447ad269d64ca91aa8d7079baa40b6fc8b965e7
Provides:       bundled(golang(github.com/cznic/ql)) = bd2055c7674ac80c520815dfe85082844cd246d4
Provides:       bundled(golang(github.com/cznic/sortutil)) = 4c7342852e65c2088c981288f2c5610d10b9f7f4
Provides:       bundled(golang(github.com/cznic/strutil)) = 43a89592ed56c227c7fdb1fcaf7d1d08be02ec54
Provides:       bundled(golang(github.com/cznic/zappy)) = 2533cb5b45cc6c07421468ce262899ddc9d53fb7
Provides:       bundled(golang(github.com/d4l3k/messagediff)) = 2fe2a1d40db6c23619ae5bcc8f80a5b43c40581b
Provides:       bundled(golang(github.com/edsrzf/mmap-go)) = 0bce6a6887123b67a60366d2c9fe2dfb74289d2e
Provides:       bundled(golang(github.com/gobwas/glob)) = 51eb1ee00b6d931c66d229ceeb7c31b985563420
Provides:       bundled(golang(github.com/gogo/protobuf)) = efccd33a0c20aa078705571d5ddbfa14c8395a63
Provides:       bundled(golang(github.com/golang/groupcache/lru)) = 72d04f9fcdec7d3821820cc4a6f150eae553639a
Provides:       bundled(golang(github.com/golang/protobuf/proto)) = 2bba0603135d7d7f5cb73b2125beeda19c09f4ef
Provides:       bundled(golang(github.com/golang/protobuf/ptypes/any)) = 2bba0603135d7d7f5cb73b2125beeda19c09f4ef
Provides:       bundled(golang(github.com/golang/snappy)) = 553a641470496b2327abcac10b36396bd98e45c9
Provides:       bundled(golang(github.com/jackpal/gateway)) = 5795ac81146e01d3fab7bcf21c043c3d6a32b006
Provides:       bundled(golang(github.com/kardianos/osext)) = 9d302b58e975387d0b4d9be876622c86cefe64be
Provides:       bundled(golang(github.com/klauspost/cpuid)) = 09cded8978dc9e80714c4d85b0322337b0a1e5e0
Provides:       bundled(golang(github.com/klauspost/reedsolomon)) = 5abf0ee302ccf4834e84f63ff74eca3e8b88e4e2
Provides:       bundled(golang(github.com/lib/pq)) = 2704adc878c21e1329f46f6e56a1c387d788ff94
Provides:       bundled(golang(github.com/minio/sha256-simd)) = 6124d070eb4e7001c244b6ccc282620a5dce44a0
Provides:       bundled(golang(github.com/onsi/ginkgo)) = 77a8c1e5c40d6bb6c5eb4dd4bdce9763564f6298
Provides:       bundled(golang(github.com/onsi/gomega)) = 334b8f472b3af5d541c5642701c1e29e2126f486
Provides:       bundled(golang(github.com/oschwald/geoip2-golang)) = 0fd242da7906550802871efe101abfdb1cc550a8
Provides:       bundled(golang(github.com/oschwald/maxminddb-golang)) = 697da8075d2061aa8ed639346443f5d3e8c80b30
Provides:       bundled(golang(github.com/petermattis/goid)) = caab6446a35a918488a0f52d4b0bd088a60f3511
Provides:       bundled(golang(github.com/pkg/errors)) = ff09b135c25aae272398c51a07235b90a75aa4f0
Provides:       bundled(golang(github.com/rcrowley/go-metrics)) = 1f30fe9094a513ce4c700b9a54458bbb0c96996c
Provides:       bundled(golang(github.com/remyoudompheng/bigfft)) = a8e77ddfb93284b9d58881f597c820a2875af336
Provides:       bundled(golang(github.com/sasha-s/go-deadlock)) = 341000892f3dd25f440e6231e8533eb3688ed7ec
Provides:       bundled(golang(github.com/stathat/go)) = 74669b9f388d9d788c97399a0824adbfee78400e
Provides:       bundled(golang(github.com/syndtr/goleveldb/leveldb)) = 3c5717caf1475fd25964109a0fc640bd150fce43
Provides:       bundled(golang(github.com/thejerf/suture)) = 0ac47afae95ad5bc5184ed346bc945168e883f5d
Provides:       bundled(golang(github.com/vitrun/qart/coding)) = bf64b92db6b05651d6c25a3dabf2d543b360c0aa
Provides:       bundled(golang(github.com/vitrun/qart/gf256)) = bf64b92db6b05651d6c25a3dabf2d543b360c0aa
Provides:       bundled(golang(github.com/vitrun/qart/qr)) = bf64b92db6b05651d6c25a3dabf2d543b360c0aa
Provides:       bundled(golang(github.com/xtaci/kcp-go)) = 0b0731ef3f184a8985edcb4ca26a4b0598c6dc1a
Provides:       bundled(golang(github.com/xtaci/smux)) = 0f6b9aaecaaf354357adc7def9239011ad276776
Provides:       bundled(golang(golang.org/x/crypto/bcrypt)) = c78caca803c95773f48a844d3dcab04b9bc4d6dd
Provides:       bundled(golang(golang.org/x/crypto/blowfish)) = c78caca803c95773f48a844d3dcab04b9bc4d6dd
Provides:       bundled(golang(golang.org/x/crypto/cast5)) = c78caca803c95773f48a844d3dcab04b9bc4d6dd
Provides:       bundled(golang(golang.org/x/crypto/pbkdf2)) = c78caca803c95773f48a844d3dcab04b9bc4d6dd
Provides:       bundled(golang(golang.org/x/crypto/salsa20)) = c78caca803c95773f48a844d3dcab04b9bc4d6dd
Provides:       bundled(golang(golang.org/x/crypto/tea)) = c78caca803c95773f48a844d3dcab04b9bc4d6dd
Provides:       bundled(golang(golang.org/x/crypto/twofish)) = c78caca803c95773f48a844d3dcab04b9bc4d6dd
Provides:       bundled(golang(golang.org/x/crypto/xtea)) = c78caca803c95773f48a844d3dcab04b9bc4d6dd
Provides:       bundled(golang(golang.org/x/net/bpf)) = ffcf1bedda3b04ebb15a168a59800a73d6dc0f4d
Provides:       bundled(golang(golang.org/x/net/context)) = ffcf1bedda3b04ebb15a168a59800a73d6dc0f4d
Provides:       bundled(golang(golang.org/x/net/internal/iana)) = ffcf1bedda3b04ebb15a168a59800a73d6dc0f4d
Provides:       bundled(golang(golang.org/x/net/internal/netreflect)) = ffcf1bedda3b04ebb15a168a59800a73d6dc0f4d
Provides:       bundled(golang(golang.org/x/net/ipv4)) = ffcf1bedda3b04ebb15a168a59800a73d6dc0f4d
Provides:       bundled(golang(golang.org/x/net/ipv6)) = ffcf1bedda3b04ebb15a168a59800a73d6dc0f4d
Provides:       bundled(golang(golang.org/x/net/proxy)) = ffcf1bedda3b04ebb15a168a59800a73d6dc0f4d
Provides:       bundled(golang(golang.org/x/sys/unix)) = f3918c30c5c2cb527c0b071a27c35120a6c0719a
Provides:       bundled(golang(golang.org/x/sys/windows)) = 493114f68206f85e7e333beccfabc11e98cba8dd
Provides:       bundled(golang(golang.org/x/text/internal/gen)) = f4b4367115ec2de254587813edaa901bc1c723a8
Provides:       bundled(golang(golang.org/x/text/internal/triegen)) = f4b4367115ec2de254587813edaa901bc1c723a8
Provides:       bundled(golang(golang.org/x/text/internal/ucd)) = f4b4367115ec2de254587813edaa901bc1c723a8
Provides:       bundled(golang(golang.org/x/text/transform)) = f4b4367115ec2de254587813edaa901bc1c723a8
Provides:       bundled(golang(golang.org/x/text/unicode/cldr)) = f4b4367115ec2de254587813edaa901bc1c723a8
Provides:       bundled(golang(golang.org/x/text/unicode/norm)) = f4b4367115ec2de254587813edaa901bc1c723a8
Provides:       bundled(golang(golang.org/x/time/rate)) = f51c12702a4d776e4c1fa9b0fabab841babae631
Provides:       bundled(golang(gopkg.in/yaml.v2)) = a3f3340b5840cee44f372bddb5880fcbc419b46a
%endif

%description    devel
Syncthing replaces other file synchronization services with something
open, trustworthy and decentralized. Your data is your data alone and
you deserve to choose where it is stored, if it is shared with some
third party and how it's transmitted over the Internet.

Using syncthing, that control is returned to you.

This package contains the syncthing source files, which are needed as
dependency for building packages using syncthing.
%endif


%if 0%{?with_unit_test} && 0%{?with_devel}
%package        unit-test-devel
Summary:        Continuous File Synchronization (unit tests)
Provides:       %{long_name}-unit-test-devel = %{version}-%{release}

# test subpackage tests code from devel subpackage
Requires:       %{name}-devel = %{version}-%{release}

%if 0%{?with_check} && ! 0%{?with_bundled}
BuildRequires:  golang(github.com/d4l3k/messagediff)
%endif

Requires:       golang(github.com/d4l3k/messagediff)

%description    unit-test-devel
Syncthing replaces other file synchronization services with something
open, trustworthy and decentralized. Your data is your data alone and
you deserve to choose where it is stored, if it is shared with some
third party and how it's transmitted over the Internet.

Using syncthing, that control is returned to you.

This package contains the unit tests for syncthing.
%endif


%if 0%{?with_tools}
%package        tools
Summary:        Continuous File Synchronization (server tools)

%if ! 0%{?with_bundled}
BuildRequires:  golang(github.com/AudriusButkevicius/cli)
BuildRequires:  golang(github.com/cznic/ql)
BuildRequires:  golang(github.com/golang/groupcache/lru)
BuildRequires:  golang(github.com/lib/pq)
BuildRequires:  golang(github.com/oschwald/geoip2-golang)
%endif

%description    tools
Syncthing replaces other file synchronization services with something
open, trustworthy and decentralized. Your data is your data alone and
you deserve to choose where it is stored, if it is shared with some
third party and how it's transmitted over the Internet.

Using syncthing, that control is returned to you.

This package contains the syncthing server tools.
%endif


%prep
%setup -q -n syncthing
%patch0 -p1


%build
%if ! 0%{?with_bundled}
# remove bundled libraries
rm -r vendor
%endif

# Replace usage of "context" package (go 1.7+ only) with the old
# "golang.org/x/net/context" package if only an old compiler is available
%if 0%{?fedora} == 24 || 0%{?rhel}
sed -i 's/"context"/"golang.org\/x\/net\/context"/' cmd/syncthing/*.go lib/*/*.go
%endif

# prepare build environment
mkdir -p ./_build/src/%{provider}.%{provider_tld}/%{project}

TOP=$(pwd)
pushd _build/src/%{provider}.%{provider_tld}/%{project}
ln -s $TOP ./syncthing
popd

export GOPATH=$(pwd)/_build:%{gopath}
export BUILDDIR=$(pwd)/_build/src/%{import_path}

# set BUILD_HOST variable so syncthing knows where it was built
export BUILD_HOST=fedora-koji

# run builds in appropriate directory
pushd $BUILDDIR

head -c20 /dev/urandom | od -An -tx1 | tr -d ' \n' > build_id
go run build.go -no-upgrade build syncthing

%if 0%{?with_tools}
head -c20 /dev/urandom | od -An -tx1 | tr -d ' \n' > build_id
go run build.go -no-upgrade build stdiscosrv

head -c20 /dev/urandom | od -An -tx1 | tr -d ' \n' > build_id
go run build.go -no-upgrade build strelaysrv

head -c20 /dev/urandom | od -An -tx1 | tr -d ' \n' > build_id
go run build.go -no-upgrade build strelaypoolsrv
%endif

popd

# remove build script so it doesn't get picked up later
%if 0%{?with_devel}
rm build.go
%endif


%install
# install binaries
mkdir -p %{buildroot}/%{_bindir}

cp -pav ./syncthing %{buildroot}/%{_bindir}/

%if 0%{?with_tools}
cp -pav ./stdiscosrv %{buildroot}/%{_bindir}/
cp -pav ./strelaysrv %{buildroot}/%{_bindir}/
cp -pav ./strelaypoolsrv %{buildroot}/%{_bindir}/
%endif

# install man pages
mkdir -p %{buildroot}/%{_mandir}/man1
mkdir -p %{buildroot}/%{_mandir}/man5
mkdir -p %{buildroot}/%{_mandir}/man7

cp -pav ./man/syncthing.1 %{buildroot}/%{_mandir}/man1/
cp -pav ./man/*.5 %{buildroot}/%{_mandir}/man5/
cp -pav ./man/*.7 %{buildroot}/%{_mandir}/man7/

%if 0%{?with_tools}
cp -pav ./man/stdiscosrv.1 %{buildroot}/%{_mandir}/man1/
cp -pav ./man/strelaysrv.1 %{buildroot}/%{_mandir}/man1/
%endif

# install systemd units
mkdir -p %{buildroot}/%{_unitdir}
mkdir -p %{buildroot}/%{_userunitdir}

cp -pav etc/linux-systemd/system/syncthing@.service %{buildroot}/%{_unitdir}/
cp -pav etc/linux-systemd/system/syncthing-resume.service %{buildroot}/%{_unitdir}/
cp -pav etc/linux-systemd/user/syncthing.service %{buildroot}/%{_userunitdir}/

# install systemd preset disabling the service per default
mkdir -p %{buildroot}/%{_prefix}/lib/systemd/user-preset
echo "disable syncthing*" > %{buildroot}/%{_prefix}/lib/systemd/user-preset/90-syncthing.preset


# Unmark source files as executable
for i in $(find -name "*.go" -executable -print); do chmod a-x $i; done


# source codes for building projects
%if 0%{?with_devel}
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
echo "%%dir %%{gopath}/src/%%{import_path}/." >> devel.file-list

# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . \( -iname "*.go" -or -iname "*.s" \) \! -iname "*_test.go" | grep -v "vendor") ; do
    dirprefix=$(dirname $file)
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$dirprefix
    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    echo "%%{gopath}/src/%%{import_path}/$file" >> devel.file-list

    while [ "$dirprefix" != "." ]; do
        echo "%%dir %%{gopath}/src/%%{import_path}/$dirprefix" >> devel.file-list
        dirprefix=$(dirname $dirprefix)
    done
done
%endif

# testing files for this project
%if 0%{?with_unit_test} && 0%{?with_devel}
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/

# find all *_test.go files and generate unit-test-devel.file-list
for file in $(find . -iname "*_test.go" | grep -v "vendor") ; do
    dirprefix=$(dirname $file)
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$dirprefix
    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    echo "%%{gopath}/src/%%{import_path}/$file" >> unit-test-devel.file-list

    while [ "$dirprefix" != "." ]; do
        echo "%%dir %%{gopath}/src/%%{import_path}/$dirprefix" >> devel.file-list
        dirprefix=$(dirname $dirprefix)
    done
done

# add test data for unit test subpackage
cp -pavr cmd/syncthing/testdata %{buildroot}/%{gopath}/src/%{import_path}/cmd/syncthing/
echo "%%{gopath}/src/%%{import_path}/cmd/syncthing/testdata" >> unit-test-devel.file-list

cp -pavr test/h* %{buildroot}/%{gopath}/src/%{import_path}/test/

cp -pavr lib/config/testdata %{buildroot}/%{gopath}/src/%{import_path}/lib/config/
echo "%%{gopath}/src/%%{import_path}/lib/config/testdata" >> unit-test-devel.file-list

cp -pavr lib/db/testdata %{buildroot}/%{gopath}/src/%{import_path}/lib/db/
echo "%%{gopath}/src/%%{import_path}/lib/db/testdata" >> unit-test-devel.file-list

cp -pavr lib/ignore/testdata %{buildroot}/%{gopath}/src/%{import_path}/lib/ignore/
echo "%%{gopath}/src/%%{import_path}/lib/ignore/testdata" >> unit-test-devel.file-list

cp -pavr lib/model/testdata %{buildroot}/%{gopath}/src/%{import_path}/lib/model/
echo "%%{gopath}/src/%%{import_path}/lib/model/testdata" >> unit-test-devel.file-list

cp -pavr lib/scanner/testdata %{buildroot}/%{gopath}/src/%{import_path}/lib/scanner/
echo "%%{gopath}/src/%%{import_path}/lib/scanner/testdata" >> unit-test-devel.file-list

cp -pavr lib/versioner/_external_test %{buildroot}/%{gopath}/src/%{import_path}/lib/versioner/
echo "%%{gopath}/src/%%{import_path}/lib/versioner/_external_test" >> unit-test-devel.file-list
%endif

%if 0%{?with_devel}
sort -u -o devel.file-list devel.file-list
%endif

%if 0%{?with_unit_test}
sort -u -o unit-test-devel.file-list unit-test-devel.file-list
%endif


%check
%if 0%{?with_check} && 0%{?with_unit_test} && 0%{?with_devel}
%if ! 0%{?with_bundled}
export GOPATH=%{buildroot}/%{gopath}:%{gopath}
%else
# Since we aren't packaging up the vendor directory we need to link
# back to it somehow. Hack it up so that we can add the vendor
# directory from BUILD dir as a gopath to be searched when executing
# tests from the BUILDROOT dir.
ln -s ./ ./vendor/src # ./vendor/src -> ./vendor
export GOPATH=%{buildroot}/%{gopath}:$(pwd)/vendor:%{gopath}
%endif

%if ! 0%{?gotest:1}
%global gotest go test
%endif

%gotest %{import_path}/cmd/syncthing
%gotest %{import_path}/lib/auto
%gotest %{import_path}/lib/beacon
%gotest %{import_path}/lib/config
%gotest %{import_path}/lib/connections
%gotest %{import_path}/lib/db
%gotest %{import_path}/lib/dialer
%gotest %{import_path}/lib/discover
%gotest %{import_path}/lib/events
%gotest %{import_path}/lib/fs
%gotest %{import_path}/lib/ignore
%gotest %{import_path}/lib/logger
%gotest %{import_path}/lib/model
%gotest %{import_path}/lib/nat
%gotest %{import_path}/lib/osutil
%gotest %{import_path}/lib/pmp
%gotest %{import_path}/lib/protocol
%gotest %{import_path}/lib/rand
%gotest %{import_path}/lib/relay/client
%gotest %{import_path}/lib/relay/protocol
%gotest %{import_path}/lib/scanner
%gotest %{import_path}/lib/signature
%gotest %{import_path}/lib/stats
%gotest %{import_path}/lib/sync
%gotest %{import_path}/lib/tlsutil
%gotest %{import_path}/lib/upgrade
%gotest %{import_path}/lib/upnp
%gotest %{import_path}/lib/util
%gotest %{import_path}/lib/versioner
%gotest %{import_path}/lib/weakhash

# Clean up after the tests
rm %{buildroot}/%{gopath}/src/%{import_path}/lib/model/testdata/empty
rm -r %{buildroot}/%{gopath}/src/%{import_path}/test/h*/

find %{buildroot}/%{gopath}/src/%{import_path}/ -name ".gitignore" -print -delete
find %{buildroot}/%{gopath}/src/%{import_path}/ -name ".stignore" -print -delete
find %{buildroot}/%{gopath}/src/%{import_path}/ -name ".stfolder" -print -delete
%endif


%post
%systemd_post 'syncthing@*.service'
%systemd_user_post syncthing.service

%preun
%systemd_preun 'syncthing@*.service'
%systemd_user_preun syncthing.service

%postun
%systemd_postun_with_restart 'syncthing@*.service'
%systemd_user_postun_with_restart syncthing.service


#define license tag if not already defined
%{!?_licensedir:%global license %doc}


%files
%license LICENSE
%doc README.md AUTHORS

%{_bindir}/syncthing

%{_mandir}/*/syncthing*

%{_unitdir}/syncthing@.service
%{_unitdir}/syncthing-resume.service
%{_userunitdir}/syncthing.service

%{_prefix}/lib/systemd/user-preset/90-syncthing.preset


%if 0%{?with_tools}
%files tools
%license LICENSE
%doc README.md AUTHORS

%{_bindir}/stdiscosrv
%{_bindir}/strelaysrv
%{_bindir}/strelaypoolsrv

%{_mandir}/man1/stdiscosrv*
%{_mandir}/man1/strelaysrv*
%endif


%if 0%{?with_devel}
%files devel -f devel.file-list
%license LICENSE
%doc README.md AUTHORS
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%endif


%if 0%{?with_unit_test} && 0%{?with_devel}
%files unit-test-devel -f unit-test-devel.file-list
%license LICENSE
%doc README.md AUTHORS
%endif


%changelog
* Wed Aug 09 2017 Fabio Valentini <decathorpe@gmail.com> - 0.14.35-2
- Add Provides for bundled JS libraries and adapt License tag.

* Tue Aug 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.14.35-1
- Update to version 0.14.35.

* Tue Aug 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.14.34-1
- Update to version 0.14.34.

* Sat Aug 05 2017 Fabio Valentini <decathorpe@gmail.com> - 0.14.33-3
- Add another missing ldflags argument.

* Tue Aug 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.14.33-2
- Adapt patched build script to use the correct LDFLAGS.

* Tue Jul 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.14.33-1
- Update to version 0.14.33.

* Tue Jul 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.14.32-1
- Update to version 0.14.32.

* Tue Jun 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.14.31-1
- Update to version 0.14.31.

* Tue Jun 13 2017 Fabio Valentini <decathorpe@gmail.com> - 0.14.30-1
- Update to version 0.14.30.

* Tue May 30 2017 Fabio Valentini <decathorpe@gmail.com> - 0.14.29-1
- Update to version 0.14.29.

* Tue May 16 2017 Fabio Valentini <decathorpe@gmail.com> - 0.14.28-1
- Update to version 0.14.28.

* Tue Apr 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.14.27-1
- Update to version 0.14.27.

* Fri Apr 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.14.26-1
- Update to version 0.14.26.

* Tue Mar 21 2017 Fabio Valentini <decathorpe@gmail.com> - 0.14.25-1
- Update to version 0.14.25.

* Tue Mar 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.14.24-1
- Update to version 0.14.24.

* Tue Feb 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.14.23-2
- Clean up spec file, remove bundled libs on fedora, add man pages.

* Tue Feb 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.14.23-1
- First package for fedora.

