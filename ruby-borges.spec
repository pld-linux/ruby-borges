%define	ruby_archdir	%(ruby -r rbconfig -e 'print Config::CONFIG["archdir"]')
%define ruby_rubylibdir %(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
Summary:	Continuation-based web application framework
Name:	ruby-Borges
Version:	1.1.0
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/574/borges-%{version}.tar.gz
# Source0-md5:	16b448d727a2647cf1dadfed22b5a02f
URL:		http://borges.rubyforge.org/
BuildArch:	noarch
BuildRequires:	ruby
BuildRequires:	ruby-devel
Requires:	ruby
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Borges is a continuation-based web application framework originally ported from
on Seaside 2 that allows a linear style of programming of web applications.
Components of a Borges web page can call and return from each other in a
natural way, allowing complex interaction between components from simple
methods. Backtracking is supported seamlessly, allowing a simple approach to
building web applications that does not get in the developer's way.

%prep
%setup -q -n borges-%{version}

%build
ruby setup.rb config \
	--rb-dir=%{ruby_rubylibdir} \
	--so-dir=%{ruby_archdir}

ruby setup.rb setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_archdir}
ruby setup.rb install --prefix=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_examplesdir}
mv $RPM_BUILD_ROOT/usr/share/examples/* $RPM_BUILD_ROOT/%{_examplesdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README*
%{ruby_rubylibdir}/Borges.rb
%{ruby_rubylibdir}/Borges
%{_docdir}/ruby/Borges
%{_examplesdir}/*
