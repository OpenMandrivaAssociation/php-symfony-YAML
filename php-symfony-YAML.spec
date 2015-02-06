%define  upstream_name YAML

Summary:	A PHP library that speaks YAML
Name:		php-symfony-%{upstream_name}
Version:	1.0.6
Release:	3
License:	MIT
Group:		Development/PHP
URL:		http://pear.symfony-project.com/
Source0:	http://pear.symfony-project.com/get/YAML-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-cli >= 3:5.2.1
Requires:	php-pear >= 1:1.9.4
Requires:	php-channel-symfony
BuildArch:	noarch
BuildRequires:	php-pear
BuildRequires:	php-channel-symfony

%description
Symfony YAML is a PHP library that parses YAML strings and converts them to
PHP arrays. It can also converts PHP arrays to YAML strings. Its official
website is at http://components.symfony-project.org/yaml/.

This package provides The Symfony YAML Component.

%prep

%setup -q -c 
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%build

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/LICENSE
%doc %{upstream_name}-%{version}/README.markdown
%{_datadir}/pear/SymfonyComponents/YAML
%{_datadir}/pear/packages/YAML.xml



%changelog
* Wed Nov 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.6-1mdv2012.0
+ Revision: 730909
- import php-symfony-YAML


* Wed Nov 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.6-1mdv2010.2
- initial Mandriva package
