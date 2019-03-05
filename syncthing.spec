Name:           syncthing
Summary:        Continuous File Synchronization
Version:        1.1.0
Release:        1%{?dist}

%global goipath github.com/syncthing/syncthing
%global tag     v%{version}

%gometa

# syncthing (MPLv2.0) bundles
# - angular (MIT),
# - bootstrap (MIT),
# - ForkAwesome (MIT/OFL/CC-BY 3.0), and
# - moment (MIT)
# - a number of go packages (see below)
License:        MPLv2.0 and MIT and OFL and CC-BY

URL:            https://syncthing.net
Source0:        %{gourl}/releases/download/%{tag}/%{name}-source-%{tag}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  systemd

%{?systemd_requires}

# assets in gui/default/vendor/*
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

# vendored dependencies: automatically generated from go.mod
Provides:       bundled(golang(github.com/AudriusButkevicius/go-nat-pmp)) = 452c97607362
Provides:       bundled(golang(github.com/AudriusButkevicius/recli)) = 0.0.5
Provides:       bundled(golang(github.com/bkaradzic/go-lz4)) = 7224d8d8f27e
Provides:       bundled(golang(github.com/calmh/du)) = 1.0.1
Provides:       bundled(golang(github.com/calmh/xdr)) = 1.1.0
Provides:       bundled(golang(github.com/chmduquesne/rollinghash)) = a60f8e7142b5
Provides:       bundled(golang(github.com/d4l3k/messagediff)) = 1.2.1
Provides:       bundled(golang(github.com/davecgh/go-spew)) = 1.1.1
Provides:       bundled(golang(github.com/flynn-archive/go-shlex)) = 3f9db97f8568
Provides:       bundled(golang(github.com/gobwas/glob)) = 51eb1ee00b6d
Provides:       bundled(golang(github.com/gogo/protobuf)) = 1.2.0
Provides:       bundled(golang(github.com/golang/groupcache)) = 84a468cf14b4
Provides:       bundled(golang(github.com/golang/snappy)) = 553a64147049
Provides:       bundled(golang(github.com/jackpal/gateway)) = 5795ac81146e
Provides:       bundled(golang(github.com/kballard/go-shellquote)) = cd60e84ee657
Provides:       bundled(golang(github.com/kr/pretty)) = 0.1.0
Provides:       bundled(golang(github.com/lib/pq)) = 1.0.0
Provides:       bundled(golang(github.com/mattn/go-isatty)) = 0.0.4
Provides:       bundled(golang(github.com/minio/sha256-simd)) = cc1980cb0338
Provides:       bundled(golang(github.com/onsi/ginkgo)) = 6c46eb8334b3
Provides:       bundled(golang(github.com/onsi/gomega)) = ba3724c94e4d
Provides:       bundled(golang(github.com/oschwald/geoip2-golang)) = 1.1.0
Provides:       bundled(golang(github.com/oschwald/maxminddb-golang)) = 26fe5ace1c70
Provides:       bundled(golang(github.com/petermattis/goid)) = 3db12ebb2a59
Provides:       bundled(golang(github.com/pkg/errors)) = 0.8.1
Provides:       bundled(golang(github.com/pmezard/go-difflib)) = 1.0.0
Provides:       bundled(golang(github.com/prometheus/client_golang)) = 0.9.2
Provides:       bundled(golang(github.com/rcrowley/go-metrics)) = e181e095bae9
Provides:       bundled(golang(github.com/sasha-s/go-deadlock)) = 0.2.0
Provides:       bundled(golang(github.com/stretchr/testify)) = 1.2.2
Provides:       bundled(golang(github.com/syncthing/notify)) = 4e389ea6c0d8
Provides:       bundled(golang(github.com/syndtr/goleveldb)) = 34011bf325bc
Provides:       bundled(golang(github.com/thejerf/suture)) = 3.0.2+incompatible
Provides:       bundled(golang(github.com/urfave/cli)) = 1.20.0
Provides:       bundled(golang(github.com/vitrun/qart)) = bf64b92db6b0
Provides:       bundled(golang(golang.org/x/crypto)) = 0fcca4842a8d
Provides:       bundled(golang(golang.org/x/net)) = 351d144fa1fc
Provides:       bundled(golang(golang.org/x/sys)) = 4d1cda033e06
Provides:       bundled(golang(golang.org/x/text)) = e19ae1496984
Provides:       bundled(golang(golang.org/x/time)) = 6dc17368e09b
Provides:       bundled(golang(gopkg.in/asn1-ber.v1)) = 379148ca0225
Provides:       bundled(golang(gopkg.in/check.v1)) = 788fd7840127
Provides:       bundled(golang(gopkg.in/ldap.v2)) = 2.5.1
Provides:       bundled(golang(gopkg.in/yaml.v2)) = 287cf08546ab

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
export GO111MODULE=off

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
export GO111MODULE=off

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
export GO111MODULE=off

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
* Tue Mar 05 2019 Fabio Valentini <decathorpe@gmail.com> - 1.1.0-1
- Update to version 1.1.0.

* Tue Feb 05 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.1-1
- Update to version 1.0.1.

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 07 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.0-1
- Update to version 1.0.0.

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

