%define  upstream_name YAML

Summary:	A PHP library that speaks YAML
Name:		php-symfony-%{upstream_name}
Version:	1.0.6
Release:	%mkrel 2
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
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
rm -rf %{buildroot}

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}

%post
%if %mdkversion < 201000
pear install --nodeps --soft --force --register-only \
    %{_datadir}/pear/packages/%{upstream_name}.xml >/dev/null || :
%endif

%preun
%if %mdkversion < 201000
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only \
        %{pear_name} >/dev/null || :
fi
%endif

%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/LICENSE
%doc %{upstream_name}-%{version}/README.markdown
%{_datadir}/pear/SymfonyComponents/YAML
%{_datadir}/pear/packages/YAML.xml

