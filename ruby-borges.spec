%define	ruby_archdir	%(ruby -r rbconfig -e 'print Config::CONFIG["archdir"]')
%define ruby_rubylibdir %(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
Summary:	Continuation-based web application framework
Summary(pl):	Szkielet aplikacji WWW oparty na kontynuacji
Name:		ruby-Borges
Version:	1.1.0
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/574/borges-%{version}.tar.gz
# Source0-md5:	16b448d727a2647cf1dadfed22b5a02f
URL:		http://borges.rubyforge.org/
BuildRequires:	ruby
BuildRequires:	ruby-devel
Requires:	ruby
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Borges is a continuation-based web application framework originally
ported from on Seaside 2 that allows a linear style of programming of
web applications. Components of a Borges web page can call and return
from each other in a natural way, allowing complex interaction between
components from simple methods. Backtracking is supported seamlessly,
allowing a simple approach to building web applications that does not
get in the developer's way.

%description -l pl
Borges to szkielet aplikacji WWW oparty na kontynuacji, oryginalnie
sportowany z Seaside 2, pozwalaj±cy na liniowy styl programowania
aplikacji WWW. Komponenty stron Borges mog± wywo³ywaæ siê nawzajem i
powracaæ w naturalny sposób, pozwalaj±c na z³o¿on± interakcjê miêdzy
komponentami z prostych metod. Wsteczne ¶ledzenie jest obs³ugiwane w
sposób przezroczysty, co pozwala na proste podej¶cie przy tworzeniu
aplikacji WWW bez wchodzenia programistom w drogê.

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

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}
mv -f $RPM_BUILD_ROOT/usr/share/examples/* $RPM_BUILD_ROOT%{_examplesdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README*
%{ruby_rubylibdir}/Borges.rb
%{ruby_rubylibdir}/Borges
%{_docdir}/ruby/Borges
%{_examplesdir}/*
