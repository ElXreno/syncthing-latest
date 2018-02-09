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
%global commit          a9f0659f2f4bf910f82b652fd27a864074ec7ab8
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

# commit a9f0659f2f4bf910f82b652fd27a864074ec7ab8 == version 0.14.43


Name:           syncthing
Summary:        Continuous File Synchronization
Version:        0.14.43
Release:        2%{?dist}

# syncthing (MPLv2.0) bundles angular (MIT), bootstrap (MIT), and font-awesome (MIT/OFL)
License:        MPLv2.0 and MIT and OFL

URL:            https://syncthing.net
Source0:        https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-source-v%{version}.tar.gz

# Patch build.go script so go build doesn't install deps
# and produces debug-enabled binaries for rpm
Patch0:         00-go-build-flags.patch
Patch1:         00-go-build-flags-ppc64.patch

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 aarch64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}

BuildRequires:  systemd
%{?systemd_requires}

%if 0%{?with_check} && ! 0%{?with_bundled}
BuildRequires:  golang(github.com/AudriusButkevicius/go-nat-pmp)
BuildRequires:  golang(github.com/AudriusButkevicius/pfilter)
BuildRequires:  golang(github.com/bkaradzic/go-lz4)
BuildRequires:  golang(github.com/calmh/du)
BuildRequires:  golang(github.com/calmh/xdr)
BuildRequires:  golang(github.com/ccding/go-stun/stun)
BuildRequires:  golang(github.com/chmduquesne/rollinghash/adler32)
BuildRequires:  golang(github.com/gobwas/glob)
BuildRequires:  golang(github.com/gogo/protobuf/gogoproto)
BuildRequires:  golang(github.com/gogo/protobuf/proto)
BuildRequires:  golang(github.com/jackpal/gateway)
BuildRequires:  golang(github.com/kardianos/osext)
BuildRequires:  golang(github.com/kballard/go-shellquote)
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
BuildRequires:  golang(github.com/zillode/notify)
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
Provides:       bundled(bootstrap) = 3.3.6
Provides:       bundled(font-awesome) = 4.5.0
Provides:       bundled(jquery) = 2.2.2

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
Requires:       golang(github.com/AudriusButkevicius/pfilter)
Requires:       golang(github.com/bkaradzic/go-lz4)
Requires:       golang(github.com/calmh/du)
Requires:       golang(github.com/calmh/xdr)
Requires:       golang(github.com/ccding/go-stun/stun)
Requires:       golang(github.com/chmduquesne/rollinghash/adler32)
Requires:       golang(github.com/gobwas/glob)
Requires:       golang(github.com/gogo/protobuf/gogoproto)
Requires:       golang(github.com/gogo/protobuf/proto)
Requires:       golang(github.com/jackpal/gateway)
Requires:       golang(github.com/kardianos/osext)
Requires:       golang(github.com/kballard/go-shellquote)
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
Requires:       golang(github.com/zillode/notify)
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
third party and how it's transmitted over the Internet. Using syncthing,
that control is returned to you.

This package contains the syncthing unit tests.
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
%setup -q -n syncthing

# PIE build mode isn't supported on ppc64
%ifarch ppc64
%patch1 -p1
%else
%patch0 -p1
%endif


%build
# remove bundled libraries
rm -r vendor

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

%if 0%{?with_cli}
%gobuild -o stcli %{import_path}/cmd/stcli
%endif

# remove build script so it doesn't get picked up later
rm build.go


%install
# install binaries
mkdir -p %{buildroot}/%{_bindir}

cp -pav ./syncthing %{buildroot}/%{_bindir}/

%if 0%{?with_tools}
cp -pav ./stdiscosrv %{buildroot}/%{_bindir}/
cp -pav ./strelaysrv %{buildroot}/%{_bindir}/
cp -pav ./strelaypoolsrv %{buildroot}/%{_bindir}/
%endif

%if 0%{?with_cli}
cp -pav ./stcli %{buildroot}/%{_bindir}/
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
export GOPATH=%{buildroot}/%{gopath}:%{gopath}

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

# This test is a bit flaky on some architectures, issue is tracked at:
# https://github.com/syncthing/syncthing/issues/4370
%gotest %{import_path}/lib/model || :

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

# This test is failing randomly right now. Issue is tracked upstream at:
# https://github.com/syncthing/syncthing/issues/4351
%gotest %{import_path}/lib/versioner || :

%gotest %{import_path}/lib/watchaggregator
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


%if 0%{?with_unit_test} && 0%{?with_devel}
%files unit-test-devel -f unit-test-devel.file-list
%license LICENSE
%doc README.md AUTHORS
%endif


%changelog
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

