# Generate devel rpm
%global with_devel 1
# Build project from bundled dependencies
%global with_bundled 0
# Build with debug info rpm
%global with_debug 1
# Run tests in check section
%global with_check 1
# Generate unit-test rpm
%global with_unit_test 1
# Build server tools
%global with_tools 1
# Build CLI program
%global with_cli 1

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
%global goipath         %{provider_prefix}
%global commit          92602485434d17b473b2034b4291d29d869c4076
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

# commit 92602485434d17b473b2034b4291d29d869c4076 == version 0.14.48


Name:           syncthing
Summary:        Continuous File Synchronization
Version:        0.14.48
Release:        1%{?dist}

# syncthing (MPLv2.0) bundles
# - angular (MIT),
# - bootstrap (MIT),
# - font-awesome (MIT/OFL), and
# - moment (MIT)
License:        MPLv2.0 and MIT and OFL

URL:            https://syncthing.net
Source0:        https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-source-v%{version}.tar.gz

# replace usage of deprecated "github.com/kardianos/osext" by stdlib's "os"
Patch1:         01-replace-deprecated-osext.patch

# goleveldb in fedora is too old to have the nosync option, so disable it
Patch2:         02-leveldb-nonosync.patch

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 aarch64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}

BuildRequires:  systemd

%if 0%{?with_check} && ! 0%{?with_bundled}
BuildRequires:  golang(github.com/AudriusButkevicius/go-nat-pmp)
BuildRequires:  golang(github.com/bkaradzic/go-lz4)
BuildRequires:  golang(github.com/calmh/du)
BuildRequires:  golang(github.com/calmh/xdr)
BuildRequires:  golang(github.com/chmduquesne/rollinghash/adler32)
BuildRequires:  golang(github.com/d4l3k/messagediff)
BuildRequires:  golang(github.com/gobwas/glob)
BuildRequires:  golang(github.com/gogo/protobuf/gogoproto)
BuildRequires:  golang(github.com/gogo/protobuf/proto)
BuildRequires:  golang(github.com/jackpal/gateway)
BuildRequires:  golang(github.com/kballard/go-shellquote)
BuildRequires:  golang(github.com/minio/sha256-simd)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(github.com/rcrowley/go-metrics)
BuildRequires:  golang(github.com/sasha-s/go-deadlock)
BuildRequires:  golang(github.com/syncthing/notify)
BuildRequires:  golang(github.com/syndtr/goleveldb/leveldb)
BuildRequires:  golang(github.com/syndtr/goleveldb/leveldb/errors)
BuildRequires:  golang(github.com/syndtr/goleveldb/leveldb/iterator)
BuildRequires:  golang(github.com/syndtr/goleveldb/leveldb/opt)
BuildRequires:  golang(github.com/syndtr/goleveldb/leveldb/storage)
BuildRequires:  golang(github.com/syndtr/goleveldb/leveldb/util)
BuildRequires:  golang(github.com/thejerf/suture)
BuildRequires:  golang(github.com/vitrun/qart/qr)
BuildRequires:  golang(golang.org/x/crypto/bcrypt)
BuildRequires:  golang(golang.org/x/net/ipv4)
BuildRequires:  golang(golang.org/x/net/ipv6)
BuildRequires:  golang(golang.org/x/net/proxy)
BuildRequires:  golang(golang.org/x/text/unicode/norm)
BuildRequires:  golang(golang.org/x/time/rate)
%endif

%{?systemd_requires}

Provides:       %{long_name} = %{version}-%{release}

Provides:       bundled(angular) = 1.3.20
Provides:       bundled(angular-dirPagination) = 759009c
Provides:       bundled(angular-translate) = 2.9.0.1
Provides:       bundled(angular-translate-loader-static-files) = 2.11.0
Provides:       bundled(bootstrap) = 3.3.6
Provides:       bundled(font-awesome) = 4.5.0
Provides:       bundled(jquery) = 2.2.2
Provides:       bundled(jquery-fancytree) = 2.26.0
Provides:       bundled(jquery-ui) = 1.12.1
Provides:       bundled(moment) = 2.19.4

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


%if 0%{?with_devel}
%package        devel
Summary:        Continuous File Synchronization (development files)
Provides:       %{long_name}-devel = %{version}-%{release}
BuildArch:      noarch

Requires:       golang(github.com/AudriusButkevicius/go-nat-pmp)
Requires:       golang(github.com/bkaradzic/go-lz4)
Requires:       golang(github.com/calmh/du)
Requires:       golang(github.com/calmh/xdr)
Requires:       golang(github.com/chmduquesne/rollinghash/adler32)
Requires:       golang(github.com/d4l3k/messagediff)
Requires:       golang(github.com/gobwas/glob)
Requires:       golang(github.com/gogo/protobuf/gogoproto)
Requires:       golang(github.com/gogo/protobuf/proto)
Requires:       golang(github.com/jackpal/gateway)
Requires:       golang(github.com/kballard/go-shellquote)
Requires:       golang(github.com/minio/sha256-simd)
Requires:       golang(github.com/pkg/errors)
Requires:       golang(github.com/rcrowley/go-metrics)
Requires:       golang(github.com/sasha-s/go-deadlock)
Requires:       golang(github.com/syncthing/notify)
Requires:       golang(github.com/syndtr/goleveldb/leveldb)
Requires:       golang(github.com/syndtr/goleveldb/leveldb/errors)
Requires:       golang(github.com/syndtr/goleveldb/leveldb/iterator)
Requires:       golang(github.com/syndtr/goleveldb/leveldb/opt)
Requires:       golang(github.com/syndtr/goleveldb/leveldb/storage)
Requires:       golang(github.com/syndtr/goleveldb/leveldb/util)
Requires:       golang(github.com/thejerf/suture)
Requires:       golang(github.com/vitrun/qart/qr)
Requires:       golang(golang.org/x/net/ipv4)
Requires:       golang(golang.org/x/net/ipv6)
Requires:       golang(golang.org/x/net/proxy)
Requires:       golang(golang.org/x/text/unicode/norm)
Requires:       golang(golang.org/x/time/rate)

%if %{with_tools}
Requires:       golang(github.com/golang/groupcache/lru)
Requires:       golang(github.com/oschwald/geoip2-golang)
Requires:       golang(github.com/prometheus/client_golang/prometheus)
Requires:       golang(github.com/prometheus/client_golang/prometheus/promhttp)
%endif

%if %{with_cli}
Requires:       golang(github.com/AudriusButkevicius/cli)
%endif

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
Provides:       golang(%{import_path}/lib/watchaggregator) = %{version}-%{release}
Provides:       golang(%{import_path}/lib/weakhash) = %{version}-%{release}

%description    devel
Syncthing replaces other file synchronization services with something
open, trustworthy and decentralized. Your data is your data alone and
you deserve to choose where it is stored, if it is shared with some
third party and how it's transmitted over the Internet. Using syncthing,
that control is returned to you.

This package contains the syncthing sources, which are needed as
dependency for building packages using syncthing.
%endif


%if 0%{?with_tools}
%package        tools
Summary:        Continuous File Synchronization (server tools)

%if ! 0%{?with_bundled}
BuildRequires:  golang(github.com/golang/groupcache/lru)
BuildRequires:  golang(github.com/oschwald/geoip2-golang)
BuildRequires:  golang(github.com/prometheus/client_golang/prometheus)
BuildRequires:  golang(github.com/prometheus/client_golang/prometheus/promhttp)
%endif

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
%endif


%if 0%{?with_cli}
%package        cli
Summary:        Continuous File Synchronization (CLI)
Requires:       %{name}%{?_isa} = %{version}-%{release}

%if ! 0%{?with_bundled}
BuildRequires:  golang(github.com/AudriusButkevicius/cli)
%endif

%description    cli
Syncthing replaces other file synchronization services with something
open, trustworthy and decentralized. Your data is your data alone and
you deserve to choose where it is stored, if it is shared with some
third party and how it's transmitted over the Internet. Using syncthing,
that control is returned to you.

This package contains the CLI program.
%endif


%prep
%autosetup -n %{name} -p1


%build
# remove bundled libraries
rm -r vendor

# prepare build environment
mkdir -p ./_build/src/github.com/syncthing

TOP=$(pwd)
pushd _build/src/github.com/syncthing
ln -s $TOP syncthing
popd

export GOPATH=$(pwd)/_build:%{gopath}
export BUILDDIR=$(pwd)/_build/src/%{import_path}

# compile assets used by the build process
pushd _build/src/%{import_path}
go run build.go assets
rm build.go
popd

# set variables expected by syncthing binaries as additional LDFLAGS
export BUILD_HOST=fedora-koji
export LDFLAGS="-X main.Version=v%{version} -X main.BuildStamp=$(date +%s) -X main.BuildUser=$USER -X main.BuildHost=$BUILD_HOST"
export BUILDTAGS="noupgrade"

%gobuild -o _bin/syncthing %{import_path}/cmd/syncthing

%if 0%{?with_tools}
%gobuild -o _bin/stdiscosrv %{import_path}/cmd/stdiscosrv
%gobuild -o _bin/strelaysrv %{import_path}/cmd/strelaysrv
%gobuild -o _bin/strelaypoolsrv %{import_path}/cmd/strelaypoolsrv
%endif

%if 0%{?with_cli}
%gobuild -o _bin/stcli %{import_path}/cmd/stcli
%endif


%install
# install binaries
mkdir -p %{buildroot}/%{_bindir}

cp -pav _bin/syncthing %{buildroot}/%{_bindir}/

%if 0%{?with_tools}
cp -pav _bin/stdiscosrv %{buildroot}/%{_bindir}/
cp -pav _bin/strelaysrv %{buildroot}/%{_bindir}/
cp -pav _bin/strelaypoolsrv %{buildroot}/%{_bindir}/
%endif

%if 0%{?with_cli}
cp -pav _bin/stcli %{buildroot}/%{_bindir}/
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
echo "disable syncthing*" > %{buildroot}/%{_userpresetdir}/90-syncthing.preset


# Unmark source files as executable
for i in $(find -name "*.go" -executable -print); do chmod a-x $i; done

%goinstall


%check
%if 0%{?with_check} && 0%{?with_unit_test} && 0%{?with_devel}
export GOPATH=$(pwd)/_build:%{gopath}

%if ! 0%{?gotest:1}
%global gotest go test
%endif

%gotest %{import_path}/cmd/stdiscosrv
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

# This test sometimes fails dependent on load on some architectures:
# https://github.com/syncthing/syncthing/issues/4370
%gotest %{import_path}/lib/model || :

%gotest %{import_path}/lib/nat
%gotest %{import_path}/lib/osutil
%gotest %{import_path}/lib/pmp

# This test seems to fail on 32 bit architectures only, ignore for now:
# https://github.com/syncthing/syncthing/issues/4990
%gotest %{import_path}/lib/protocol || :

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

# This test sometimes fails dependent on load on some architectures:
# https://github.com/syncthing/syncthing/issues/4351
%gotest %{import_path}/lib/versioner || :

%gotest %{import_path}/lib/watchaggregator
%gotest %{import_path}/lib/weakhash
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


%files
%license LICENSE
%doc README.md AUTHORS

%{_bindir}/syncthing

%{_mandir}/*/syncthing*

%{_unitdir}/syncthing@.service
%{_unitdir}/syncthing-resume.service
%{_userunitdir}/syncthing.service
%{_userpresetdir}/90-syncthing.preset


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


%if 0%{?with_cli}
%files cli
%{_bindir}/stcli
%endif


%if 0%{?with_devel}
%files devel -f devel.file-list
%license LICENSE
%doc README.md AUTHORS
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%endif


%changelog
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

