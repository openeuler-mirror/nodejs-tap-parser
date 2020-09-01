%{?nodejs_find_provides_and_requires}
%global packagename tap-parser
%global enable_tests 1
Name:		nodejs-tap-parser
Version:	1.2.2
Release:	1
Summary:	Parse the test anything protocol
License:	MIT
URL:		https://github.com/substack/tap-parser.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
#wget https://github.com/substack/tap-parser.git
#cd tap-parser
#git archive --prefix='test/' --format=tar v1.2.2:test/  | bzip2 >  tests-1.2.2.tar.bz2
Source1:	tests-%{version}.tar.bz2
ExclusiveArch:	%{nodejs_arches} noarch
BuildArch:	noarch
BuildRequires:       	nodejs-packaging
%if 0%{?enable_tests}
BuildRequires:       	npm(events-to-array) 	npm(glob) 	npm(js-yaml) 	npm(tap) 	npm(tape)
%endif
%description
Parse the test anything protocol.

%prep
%setup -q -n package
%setup -q -T -D -a 1 -n package
%nodejs_fixdep -r inherits

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json *.js \
	%{buildroot}%{nodejs_sitelib}/%{packagename}
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}/bin/
cp -pr package.json bin/*.js \
	%{buildroot}%{nodejs_sitelib}/%{packagename}/bin/
mkdir -p %{buildroot}%{_bindir}
ln -sf %{nodejs_sitelib}/%{packagename}/bin/cmd.js \
	%{buildroot}%{_bindir}/tap-parser
%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
%{_bindir}/tap test/*.js
%endif

%files
%{!?_licensedir:%global license %doc}
%doc *.markdown
%license LICENSE
%{nodejs_sitelib}/%{packagename}
%{_bindir}/tap-parser

%changelog
* Fri Aug 21 2020 wangyue <wangyue92@huawei.com> - 1.2.2-1
- package init
