%global goipath github.com/syncthing/syncthing
%global tag     v0.14.54

Name:           syncthing
Summary:        Continuous File Synchronization
Version:        0.14.54
Release:        1%{?dist}

%gometa

# syncthing (MPLv2.0) bundles
# - angular (MIT),
# - bootstrap (MIT),
# - ForkAwesome (MIT/OFL/CC-BY 3.0), and
# - moment (MIT)
License:        MPLv2.0 and MIT and OFL and CC-BY

URL:            https://syncthing.net
Source0:        %{gourl}/releases/download/%{tag}/%{name}-source-%{tag}.tar.gz

# goleveldb in fedora is too old to have the nosync option, so disable it
#Patch2:         02-leveldb-nonosync.patch

BuildRequires:  desktop-file-utils
BuildRequires:  systemd

#BuildRequires:  golang(github.com/AudriusButkevicius/cli)
#BuildRequires:  golang(github.com/AudriusButkevicius/go-nat-pmp)
#BuildRequires:  golang(github.com/bkaradzic/go-lz4)
#BuildRequires:  golang(github.com/calmh/du)
#BuildRequires:  golang(github.com/calmh/xdr)
#BuildRequires:  golang(github.com/chmduquesne/rollinghash/adler32)
#BuildRequires:  golang(github.com/d4l3k/messagediff)
#BuildRequires:  golang(github.com/gobwas/glob)
#BuildRequires:  golang(github.com/gogo/protobuf/gogoproto)
#BuildRequires:  golang(github.com/gogo/protobuf/proto)
#BuildRequires:  golang(github.com/golang/groupcache/lru)
#BuildRequires:  golang(github.com/jackpal/gateway)
#BuildRequires:  golang(github.com/kballard/go-shellquote)
#BuildRequires:  golang(github.com/minio/sha256-simd)
#BuildRequires:  golang(github.com/oschwald/geoip2-golang)
#BuildRequires:  golang(github.com/prometheus/client_golang/prometheus)
#BuildRequires:  golang(github.com/prometheus/client_golang/prometheus/promhttp)
#BuildRequires:  golang(github.com/pkg/errors)
#BuildRequires:  golang(github.com/rcrowley/go-metrics)
#BuildRequires:  golang(github.com/sasha-s/go-deadlock)
#BuildRequires:  golang(github.com/syncthing/notify)
#BuildRequires:  golang(github.com/syndtr/goleveldb/leveldb)
#BuildRequires:  golang(github.com/syndtr/goleveldb/leveldb/errors)
#BuildRequires:  golang(github.com/syndtr/goleveldb/leveldb/iterator)
#BuildRequires:  golang(github.com/syndtr/goleveldb/leveldb/opt)
#BuildRequires:  golang(github.com/syndtr/goleveldb/leveldb/storage)
#BuildRequires:  golang(github.com/syndtr/goleveldb/leveldb/util)
#BuildRequires:  golang(github.com/thejerf/suture)
#BuildRequires:  golang(github.com/vitrun/qart/qr)
#BuildRequires:  golang(golang.org/x/crypto/bcrypt)
#BuildRequires:  golang(golang.org/x/net/ipv4)
#BuildRequires:  golang(golang.org/x/net/ipv6)
#BuildRequires:  golang(golang.org/x/net/proxy)
#BuildRequires:  golang(golang.org/x/text/unicode/norm)
#BuildRequires:  golang(golang.org/x/time/rate)
#BuildRequires:  golang(gopkg.in/ldap.v2)

%{?systemd_requires}

Provides:       bundled(angular) = 1.3.20
Provides:       bundled(angular-dirPagination) = 759009c
Provides:       bundled(angular-sanitize) = 1.3.20
Provides:       bundled(angular-translate) = 2.9.0.1
Provides:       bundled(angular-translate-loader-static-files) = 2.11.0
Provides:       bundled(bootstrap) = 3.3.6
Provides:       bundled(daterangepicker) = 3.0.0
Provides:       bundled(ForkAwesome) = 1.1.2
Provides:       bundled(jquery) = 2.2.2
Provides:       bundled(jquery-fancytree) = 2.28.1
Provides:       bundled(jquery-ui) = 1.12.1
Provides:       bundled(moment) = 2.19.4

Provides:       bundled(golang(code.cloudfoundry.org/bytefmt)) = a052d587819f45f719a22e344a8ad7858deb3733
Provides:       bundled(golang(github.com/AudriusButkevicius/cli)) = 7f561c78b5a4aad858d9fd550c92b5da6d55efbb
Provides:       bundled(golang(github.com/AudriusButkevicius/go-nat-pmp)) = 452c97607362b2ab5a7839b8d1704f0396b640ca
Provides:       bundled(golang(github.com/AudriusButkevicius/pfilter)) = 9dca34a5b530bfc9843fa8aa2ff08ff9821032cb
Provides:       bundled(golang(github.com/BurntSushi/toml)) = a368813c5e648fee92e5f6c30e3944ff9d5e8895
Provides:       bundled(golang(github.com/a8m/mark)) = 44f2db6188458162890ca13980819247418d8e45
Provides:       bundled(golang(github.com/beorn7/perks/quantile)) = 4c0e84591b9aa9e6dcfdf3e020114cd81f89d5f9
Provides:       bundled(golang(github.com/bkaradzic/go-lz4)) = 7224d8d8f27ef618c0a95f1ae69dbb0488abc33a
Provides:       bundled(golang(github.com/calmh/du)) = dd9dc2043353249b2910b29dcfd6f6d4e64f39be
Provides:       bundled(golang(github.com/calmh/xdr)) = 08e072f9cb164f943a92eb59f90f3abc64ac6e8f
Provides:       bundled(golang(github.com/cheggaaa/pb)) = 18d384da9bdc1e5a08fc2a62a494c321d9ae74ea
Provides:       bundled(golang(github.com/chmduquesne/rollinghash)) = abb8cbaf9915e48ee20cae94bcd94221b61707a2
Provides:       bundled(golang(github.com/d4l3k/messagediff)) = 29f32d820d112dbd66e58492a6ffb7cc3106312b
Provides:       bundled(golang(github.com/dustin/go-humanize)) = bb3d318650d48840a39aa21a027c6630e198e626
Provides:       bundled(golang(github.com/gernest/wow)) = 7e0b2a2398989a5d220eebac5742d45422ba7de8
Provides:       bundled(golang(github.com/go-ini/ini)) = 32e4c1e6bc4e7d0d8451aa6b75200d19e37a536a
Provides:       bundled(golang(github.com/gobwas/glob)) = 51eb1ee00b6d931c66d229ceeb7c31b985563420
Provides:       bundled(golang(github.com/gogo/protobuf)) = 160de10b2537169b5ae3e7e221d28269ef40d311
Provides:       bundled(golang(github.com/golang/groupcache/lru)) = 84a468cf14b4376def5d68c722b139b881c450a4
Provides:       bundled(golang(github.com/golang/protobuf/proto)) = 1e59b77b52bf8e4b449a57e6f79f21226d571845
Provides:       bundled(golang(github.com/golang/protobuf/ptypes/any)) = 1e59b77b52bf8e4b449a57e6f79f21226d571845
Provides:       bundled(golang(github.com/golang/snappy)) = 553a641470496b2327abcac10b36396bd98e45c9
Provides:       bundled(golang(github.com/jackpal/gateway)) = 5795ac81146e01d3fab7bcf21c043c3d6a32b006
Provides:       bundled(golang(github.com/kballard/go-shellquote)) = cd60e84ee657ff3dc51de0b4f55dd299a3e136f2
Provides:       bundled(golang(github.com/klauspost/cpuid)) = eae9b3e628d72774e13bdf024e78c0802f85a5b9
Provides:       bundled(golang(github.com/lib/pq)) = 4ded0e9383f75c197b3a2aaa6d590ac52df6fd79
Provides:       bundled(golang(github.com/magefile/mage/mg)) = 63768081a3236a7c6c53ef72e402ae1fe1664b61
Provides:       bundled(golang(github.com/magefile/mage/sh)) = 63768081a3236a7c6c53ef72e402ae1fe1664b61
Provides:       bundled(golang(github.com/magefile/mage/types)) = 63768081a3236a7c6c53ef72e402ae1fe1664b61
Provides:       bundled(golang(github.com/mattn/go-runewidth)) = 97311d9f7767e3d6f422ea06661bc2c7a19e8a5d
Provides:       bundled(golang(github.com/matttproud/golang_protobuf_extensions/pbutil)) = c12348ce28de40eed0136aa2b644d0ee0650e56c
Provides:       bundled(golang(github.com/minio/cli)) = 45db1f8a055198ad8c12754026cb2c51c584c756
Provides:       bundled(golang(github.com/minio/sha256-simd)) = ad98a36ba0da87206e3378c556abbfeaeaa98668
Provides:       bundled(golang(github.com/mitchellh/go-homedir)) = b8bc1bf767474819792c23f32d8286a45736f1c6
Provides:       bundled(golang(github.com/onsi/ginkgo)) = 6c46eb8334b30dc55b42f1a1c725d5ce97375390
Provides:       bundled(golang(github.com/onsi/gomega)) = ba3724c94e4dd5d5690d37c190f1c54b2c1b4e64
Provides:       bundled(golang(github.com/oschwald/geoip2-golang)) = 5b1dc16861f81d05d9836bb21c2d0d65282fc0b8
Provides:       bundled(golang(github.com/oschwald/maxminddb-golang)) = 26fe5ace1c706491c2936119e1dc69c1a9c04d7f
Provides:       bundled(golang(github.com/petermattis/goid)) = 3db12ebb2a599ba4a96bea1c17b61c2f78a40e02
Provides:       bundled(golang(github.com/pkg/errors)) = e881fd58d78e04cf6d0de1217f8707c8cc2249bc
Provides:       bundled(golang(github.com/prometheus/client_golang/prometheus)) = 1cafe34db7fdec6022e17e00e1c1ea501022f3e4
Provides:       bundled(golang(github.com/prometheus/client_model/go)) = 99fa1f4be8e564e8a6b613da7fa6f46c9edafc6c
Provides:       bundled(golang(github.com/prometheus/common/expfmt)) = 2e54d0b93cba2fd133edc32211dcc32c06ef72ca
Provides:       bundled(golang(github.com/prometheus/common/internal/bitbucket.org/ww/goautoneg)) = 2e54d0b93cba2fd133edc32211dcc32c06ef72ca
Provides:       bundled(golang(github.com/prometheus/common/model)) = 2e54d0b93cba2fd133edc32211dcc32c06ef72ca
Provides:       bundled(golang(github.com/prometheus/procfs)) = b15cd069a83443be3154b719d0cc9fe8117f09fb
Provides:       bundled(golang(github.com/rcrowley/go-metrics)) = e181e095bae94582363434144c61a9653aff6e50
Provides:       bundled(golang(github.com/sasha-s/go-deadlock)) = 03d40e5dbd5488667a13b3c2600b2f7c2886f02f
Provides:       bundled(golang(github.com/sirupsen/logrus)) = d682213848ed68c0a260ca37d6dd5ace8423f5ba
Provides:       bundled(golang(github.com/stathat/go)) = 74669b9f388d9d788c97399a0824adbfee78400e
Provides:       bundled(golang(github.com/syncthing/notify)) = 116c45bb5ad48777321e4984d1320d56889b6097
Provides:       bundled(golang(github.com/syndtr/goleveldb/leveldb)) = 34011bf325bce385408353a30b101fe5e923eb6e
Provides:       bundled(golang(github.com/templexxx/cpufeat)) = 3794dfbfb04749f896b521032f69383f24c3687e
Provides:       bundled(golang(github.com/thejerf/suture)) = bf6ee6a0b047ebbe9ae07d847f750dd18c6a9276
Provides:       bundled(golang(github.com/tjfoc/gmsm/sm4)) = 98aa888b79d8de04afe0fccf45ed10594efc858b
Provides:       bundled(golang(github.com/vitrun/qart/coding)) = bf64b92db6b05651d6c25a3dabf2d543b360c0aa
Provides:       bundled(golang(github.com/vitrun/qart/gf256)) = bf64b92db6b05651d6c25a3dabf2d543b360c0aa
Provides:       bundled(golang(github.com/vitrun/qart/qr)) = bf64b92db6b05651d6c25a3dabf2d543b360c0aa
Provides:       bundled(golang(golang.org/x/crypto/bcrypt)) = 95a4943f35d008beabde8c11e5075a1b714e6419
Provides:       bundled(golang(golang.org/x/crypto/blowfish)) = 95a4943f35d008beabde8c11e5075a1b714e6419
Provides:       bundled(golang(golang.org/x/crypto/cast5)) = 95a4943f35d008beabde8c11e5075a1b714e6419
Provides:       bundled(golang(golang.org/x/crypto/pbkdf2)) = 95a4943f35d008beabde8c11e5075a1b714e6419
Provides:       bundled(golang(golang.org/x/crypto/salsa20)) = 95a4943f35d008beabde8c11e5075a1b714e6419
Provides:       bundled(golang(golang.org/x/crypto/ssh/terminal)) = 0fcca4842a8d74bfddc2c96a073bd2a4d2a7a2e8
Provides:       bundled(golang(golang.org/x/crypto/tea)) = 95a4943f35d008beabde8c11e5075a1b714e6419
Provides:       bundled(golang(golang.org/x/crypto/twofish)) = 95a4943f35d008beabde8c11e5075a1b714e6419
Provides:       bundled(golang(golang.org/x/crypto/xtea)) = 95a4943f35d008beabde8c11e5075a1b714e6419
Provides:       bundled(golang(golang.org/x/net/bpf)) = d866cfc389cec985d6fda2859936a575a55a3ab6
Provides:       bundled(golang(golang.org/x/net/html)) = d866cfc389cec985d6fda2859936a575a55a3ab6
Provides:       bundled(golang(golang.org/x/net/internal/iana)) = d866cfc389cec985d6fda2859936a575a55a3ab6
Provides:       bundled(golang(golang.org/x/net/internal/socket)) = d866cfc389cec985d6fda2859936a575a55a3ab6
Provides:       bundled(golang(golang.org/x/net/ipv4)) = d866cfc389cec985d6fda2859936a575a55a3ab6
Provides:       bundled(golang(golang.org/x/net/ipv6)) = d866cfc389cec985d6fda2859936a575a55a3ab6
Provides:       bundled(golang(golang.org/x/net/proxy)) = d866cfc389cec985d6fda2859936a575a55a3ab6
Provides:       bundled(golang(golang.org/x/sys/unix)) = 83801418e1b59fb1880e363299581ee543af32ca
Provides:       bundled(golang(golang.org/x/sys/windows)) = 83801418e1b59fb1880e363299581ee543af32ca
Provides:       bundled(golang(golang.org/x/text/encoding)) = e19ae1496984b1c655b8044a65c0300a3c878dd3
Provides:       bundled(golang(golang.org/x/text/internal/format)) = e19ae1496984b1c655b8044a65c0300a3c878dd3
Provides:       bundled(golang(golang.org/x/text/internal/gen)) = e19ae1496984b1c655b8044a65c0300a3c878dd3
Provides:       bundled(golang(golang.org/x/text/internal/tag)) = e19ae1496984b1c655b8044a65c0300a3c878dd3
Provides:       bundled(golang(golang.org/x/text/internal/triegen)) = e19ae1496984b1c655b8044a65c0300a3c878dd3
Provides:       bundled(golang(golang.org/x/text/internal/ucd)) = e19ae1496984b1c655b8044a65c0300a3c878dd3
Provides:       bundled(golang(golang.org/x/text/internal/utf8internal)) = e19ae1496984b1c655b8044a65c0300a3c878dd3
Provides:       bundled(golang(golang.org/x/text/language)) = e19ae1496984b1c655b8044a65c0300a3c878dd3
Provides:       bundled(golang(golang.org/x/text/runes)) = e19ae1496984b1c655b8044a65c0300a3c878dd3
Provides:       bundled(golang(golang.org/x/text/transform)) = e19ae1496984b1c655b8044a65c0300a3c878dd3
Provides:       bundled(golang(golang.org/x/text/unicode/cldr)) = e19ae1496984b1c655b8044a65c0300a3c878dd3
Provides:       bundled(golang(golang.org/x/text/unicode/norm)) = e19ae1496984b1c655b8044a65c0300a3c878dd3
Provides:       bundled(golang(golang.org/x/time/rate)) = 6dc17368e09b0e8634d71cac8168d853e869a0c7
Provides:       bundled(golang(gopkg.in/asn1-ber.v1)) = 379148ca0225df7a432012b8df0355c2a2063ac0
Provides:       bundled(golang(gopkg.in/ldap.v2)) = bb7a9ca6e4fbc2129e3db588a34bc970ffe811a9
Provides:       bundled(golang(gopkg.in/urfave/cli.v1)) = cfb38830724cc34fedffe9a2a29fb54fa9169cd1
Provides:       bundled(golang(gopkg.in/yaml.v2)) = 287cf08546ab5e7e37d55a84f7ed3fd1db036de5

# an inotify filesystem watcher is integrated with syncthing now
Provides:       syncthing-inotify = 0.8.7-5
Obsoletes:      syncthing-inotify < 0.8.7-5


%description
Syncthing replaces other file synchronization services with something
open, trustworthy and decentralized. Your data is your data alone and
you deserve to choose where it is stored, if it is shared with some
third party and how it's transmitted over the Internet. Using syncthing,
that control is returned to you.

This package contains the syncthing client binary and systemd services.


%package        devel
Summary:        Continuous File Synchronization (development files)
BuildArch:      noarch

%description    devel
Syncthing replaces other file synchronization services with something
open, trustworthy and decentralized. Your data is your data alone and
you deserve to choose where it is stored, if it is shared with some
third party and how it's transmitted over the Internet. Using syncthing,
that control is returned to you.

This package contains the syncthing sources, which are needed as
dependency for building packages using syncthing.


%package        tools
Summary:        Continuous File Synchronization (server tools)

%description    tools
Syncthing replaces other file synchronization services with something
open, trustworthy and decentralized. Your data is your data alone and
you deserve to choose where it is stored, if it is shared with some
third party and how it's transmitted over the Internet. Using syncthing,
that control is returned to you.

This package contains the main syncthing server tools:

* strelaysrv / strelaypoolsrv, the syncthing relay server for indirect
  file transfers between client nodes, and
* stdiscosrv, the syncthing discovery server for discovering nodes
  to connect to indirectly over the internet.


%package        cli
Summary:        Continuous File Synchronization (CLI)

%description    cli
Syncthing replaces other file synchronization services with something
open, trustworthy and decentralized. Your data is your data alone and
you deserve to choose where it is stored, if it is shared with some
third party and how it's transmitted over the Internet. Using syncthing,
that control is returned to you.

This package contains the CLI program.


%prep
%autosetup -n %{name} -p1


%build
# remove bundled libraries
#rm -r vendor

# prepare build environment
mkdir -p ./_build/src/github.com/syncthing

TOP=$(pwd)
pushd _build/src/github.com/syncthing
ln -s $TOP syncthing
popd

export GOPATH=$(pwd)/_build:%{gopath}
export BUILDDIR=$(pwd)/_build/src/%{goipath}

# compile assets used by the build process
pushd _build/src/%{goipath}
go run build.go assets
rm build.go
popd

# set variables expected by syncthing binaries as additional LDFLAGS
export BUILD_HOST=fedora-koji
export LDFLAGS="-X main.Version=v%{version} -X main.BuildStamp=$(date +%s) -X main.BuildUser=$USER -X main.BuildHost=$BUILD_HOST"
export BUILDTAGS="noupgrade"

%gobuild -o _bin/syncthing %{goipath}/cmd/syncthing
%gobuild -o _bin/stdiscosrv %{goipath}/cmd/stdiscosrv
%gobuild -o _bin/strelaysrv %{goipath}/cmd/strelaysrv
%gobuild -o _bin/strelaypoolsrv %{goipath}/cmd/strelaypoolsrv
%gobuild -o _bin/stcli %{goipath}/cmd/stcli


%install
# install binaries
mkdir -p %{buildroot}/%{_bindir}

cp -pav _bin/syncthing %{buildroot}/%{_bindir}/
cp -pav _bin/stdiscosrv %{buildroot}/%{_bindir}/
cp -pav _bin/strelaysrv %{buildroot}/%{_bindir}/
cp -pav _bin/strelaypoolsrv %{buildroot}/%{_bindir}/
cp -pav _bin/stcli %{buildroot}/%{_bindir}/

# install man pages
mkdir -p %{buildroot}/%{_mandir}/man1
mkdir -p %{buildroot}/%{_mandir}/man5
mkdir -p %{buildroot}/%{_mandir}/man7

cp -pav ./man/syncthing.1 %{buildroot}/%{_mandir}/man1/
cp -pav ./man/*.5 %{buildroot}/%{_mandir}/man5/
cp -pav ./man/*.7 %{buildroot}/%{_mandir}/man7/
cp -pav ./man/stdiscosrv.1 %{buildroot}/%{_mandir}/man1/
cp -pav ./man/strelaysrv.1 %{buildroot}/%{_mandir}/man1/

# install systemd units
mkdir -p %{buildroot}/%{_unitdir}
mkdir -p %{buildroot}/%{_userunitdir}

cp -pav etc/linux-systemd/system/syncthing@.service %{buildroot}/%{_unitdir}/
cp -pav etc/linux-systemd/system/syncthing-resume.service %{buildroot}/%{_unitdir}/
cp -pav etc/linux-systemd/user/syncthing.service %{buildroot}/%{_userunitdir}/

# install systemd preset disabling the service per default
mkdir -p %{buildroot}/%{_userpresetdir}
echo "disable syncthing*" > %{buildroot}/%{_userpresetdir}/90-syncthing.preset

# install .desktop files
mkdir -p %{buildroot}/%{_datadir}/applications

cp -pav etc/linux-desktop/*.desktop %{buildroot}/%{_datadir}/applications/


# Unmark source files as executable
for i in $(find -name "*.go" -executable -print); do
    chmod a-x $i;
done

%goinstall


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/syncthing*.desktop

export LANG=C.utf8
export GOPATH=$(pwd)/_build:%{gopath}

%gotest %{goipath}/cmd/stdiscosrv
%gotest %{goipath}/cmd/strelaypoolsrv
%gotest %{goipath}/cmd/syncthing
%gotest %{goipath}/lib/auto
%gotest %{goipath}/lib/beacon
%gotest %{goipath}/lib/config
%gotest %{goipath}/lib/connections
%gotest %{goipath}/lib/db
%gotest %{goipath}/lib/dialer
%gotest %{goipath}/lib/discover
%gotest %{goipath}/lib/events
%gotest %{goipath}/lib/fs
%gotest %{goipath}/lib/ignore
%gotest %{goipath}/lib/logger

# This test sometimes fails dependent on load on some architectures:
# https://github.com/syncthing/syncthing/issues/4370
%gotest %{goipath}/lib/model || :

%gotest %{goipath}/lib/nat
%gotest %{goipath}/lib/osutil
%gotest %{goipath}/lib/pmp
%gotest %{goipath}/lib/protocol
%gotest %{goipath}/lib/rand
%gotest %{goipath}/lib/relay/client
%gotest %{goipath}/lib/relay/protocol
%gotest %{goipath}/lib/scanner
%gotest %{goipath}/lib/signature
%gotest %{goipath}/lib/stats
%gotest %{goipath}/lib/sync
%gotest %{goipath}/lib/tlsutil
%gotest %{goipath}/lib/upgrade
%gotest %{goipath}/lib/upnp
%gotest %{goipath}/lib/util

# This test sometimes fails dependent on load on some architectures:
# https://github.com/syncthing/syncthing/issues/4351
%gotest %{goipath}/lib/versioner || :

%gotest %{goipath}/lib/watchaggregator
%gotest %{goipath}/lib/weakhash


%post
%systemd_post 'syncthing@*.service'
%systemd_user_post syncthing.service

%preun
%systemd_preun 'syncthing@*.service'
%systemd_user_preun syncthing.service

%postun
%systemd_postun_with_restart 'syncthing@*.service'
%systemd_user_postun_with_restart syncthing.service


%files
%license LICENSE
%doc README.md AUTHORS

%{_bindir}/syncthing

%{_mandir}/*/syncthing*

%{_unitdir}/syncthing@.service
%{_unitdir}/syncthing-resume.service
%{_userunitdir}/syncthing.service
%{_userpresetdir}/90-syncthing.preset

%{_datadir}/applications/syncthing*.desktop


%files tools
%license LICENSE
%doc README.md AUTHORS

%{_bindir}/stdiscosrv
%{_bindir}/strelaysrv
%{_bindir}/strelaypoolsrv

%{_mandir}/man1/stdiscosrv*
%{_mandir}/man1/strelaysrv*


%files cli
%license LICENSE
%doc README.md AUTHORS

%{_bindir}/stcli


%files devel -f devel.file-list
%license LICENSE
%doc README.md AUTHORS


%changelog
* Wed Dec 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.14.54-1
- Update to version 0.14.54.
- Switch back to using bundled dependencies.

* Tue Dec 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.14.53-1
- Update to version 0.14.53.

* Tue Nov 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.14.52-1
- Update to version 0.14.52.

* Tue Oct 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.14.51-1
- Update to version 0.14.51.

* Sun Sep 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.14.50-2
- Adapt to rollinghash v4.0.0 changes.

* Tue Sep 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.14.50-1
- Update to version 0.14.50.
- Clean up .spec file and use new macros.
- Drop upstreamed go1.11 patch.

* Wed Jul 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.14.49-1
- Update to version 0.14.49.
- Drop upstreamed osext patch.
- Add upstream patch to fix building tests with go 1.11.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.48-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.14.48-1
- Update to version 0.14.48.

* Tue May 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.14.47-1
- Update to version 0.14.47.

* Wed Apr 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.14.46-1
- Update to version 0.14.46.
- Simplify .spec file and build process, and drop build system patches.

* Tue Mar 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.14.45-1
- Update to version 0.14.45.

* Tue Feb 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.14.44-1
- Update to version 0.14.44.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.43-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.14.43-1
- Update to version 0.14.43.

* Tue Dec 26 2017 Fabio Valentini <decathorpe@gmail.com> - 0.14.42-1
- Update to version 0.14.42.

* Tue Dec 05 2017 Fabio Valentini <decathorpe@gmail.com> - 0.14.41-1
- Update to version 0.14.41.

* Tue Nov 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.14.40-1
- Update to version 0.14.40.

* Wed Oct 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.14.39-1
- Update to version 0.14.39.

* Wed Sep 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.14.38-1
- Update to version 0.14.38.
- Add patch to use internal luhn version again.

* Mon Sep 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.14.37-2
- Rebuild for updated dependencies, fixing crashes.

* Tue Sep 05 2017 Fabio Valentini <decathorpe@gmail.com> - 0.14.37-1
- Update to version 0.14.37.

* Tue Aug 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.14.36-2
- Adapt patch to work on ppc64, where PIE isn't supported.

* Sat Aug 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.14.36-1
- Update to version 0.14.36.

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

