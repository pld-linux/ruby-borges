%define	ruby_archdir	%(ruby -r rbconfig -e 'print Config::CONFIG["archdir"]')
%define	ruby_ridir	%(ruby -r rbconfig -e 'include Config; print File.join(CONFIG["datadir"], "ri", CONFIG["ruby_version"], "system")')
%define ruby_rubylibdir %(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
Summary:	Continuation-based web application framework
Summary(pl):	Szkielet aplikacji WWW oparty na kontynuacji
Name:		ruby-Borges
Version:	1.1.0
Release:	2
License:	GPL
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/574/borges-%{version}.tar.gz
# Source0-md5:	16b448d727a2647cf1dadfed22b5a02f
URL:		http://borges.rubyforge.org/
BuildRequires:	ruby
BuildRequires:	ruby-devel
Requires:	ruby
#BuildArch:	noarch
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

find lib/ -name 'Test*' -type f -print0 | xargs -0 rm -v
find lib/ -name 'Test*' -type d -print0 | xargs -0 rm -v -r

ruby setup.rb config \
	--rb-dir=%{ruby_rubylibdir} \
	--so-dir=%{ruby_archdir}

ruby setup.rb setup

mv data/doc/ruby/Borges/RDoc data/doc/ruby/Borges/rdoc

rdoc --ri --op ri lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{ruby_ridir}}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}
mv -f $RPM_BUILD_ROOT/usr/share/examples/* $RPM_BUILD_ROOT%{_examplesdir}

rm -r $RPM_BUILD_ROOT%{_docdir}/ruby/Borges

cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}
rm $RPM_BUILD_ROOT%{ruby_ridir}/Array/cdesc-Array.yaml
rm $RPM_BUILD_ROOT%{ruby_ridir}/Numeric/cdesc-Numeric.yaml
rm $RPM_BUILD_ROOT%{ruby_ridir}/Object/cdesc-Object.yaml
rm $RPM_BUILD_ROOT%{ruby_ridir}/Proc/cdesc-Proc.yaml
rm $RPM_BUILD_ROOT%{ruby_ridir}/String/cdesc-String.yaml

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc data/doc/ruby/Borges/*
%{ruby_rubylibdir}/Borges.rb
%{ruby_rubylibdir}/Borges
%{_examplesdir}/*
%{ruby_ridir}/Borges
%{ruby_ridir}/Array/render_on-i.yaml
%{ruby_ridir}/HtmlRendererProfiler
%{ruby_ridir}/Numeric/print_html_on-i.yaml
%{ruby_ridir}/Numeric/to_cents-i.yaml
%{ruby_ridir}/Object/render_on-i.yaml
%{ruby_ridir}/Proc/handle_request-i.yaml
%{ruby_ridir}/Proc/render_on-i.yaml
%{ruby_ridir}/Profiler/cdesc-Profiler.yaml
%{ruby_ridir}/Profiler/profile-c.yaml
%{ruby_ridir}/Profiler__/cdesc-Profiler__.yaml
%{ruby_ridir}/Profiler__/profile-c.yaml
%{ruby_ridir}/String/print_html_on-i.yaml
%{ruby_ridir}/String/render_on_indent-i.yaml
%{ruby_ridir}/Weak
