%define pkgname borges
Summary:	Continuation-based web application framework
Summary(pl.UTF-8):	Szkielet aplikacji WWW oparty na kontynuacji
Name:		ruby-%{pkgname}
Version:	1.1.0
Release:	3
License:	GPL
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/574/%{pkgname}-%{version}.tar.gz
# Source0-md5:	16b448d727a2647cf1dadfed22b5a02f
URL:		http://borges.rubyforge.org/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel
%{?ruby_mod_ver_requires_eq}
Obsoletes:	ruby-Borges
Provides:	ruby-Borges
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

%description -l pl.UTF-8
Borges to szkielet aplikacji WWW oparty na kontynuacji, oryginalnie
sportowany z Seaside 2, pozwalający na liniowy styl programowania
aplikacji WWW. Komponenty stron Borges mogą wywoływać się nawzajem i
powracać w naturalny sposób, pozwalając na złożoną interakcję między
komponentami z prostych metod. Wsteczne śledzenie jest obsługiwane w
sposób przezroczysty, co pozwala na proste podejście przy tworzeniu
aplikacji WWW bez wchodzenia programistom w drogę.

%prep
%setup -q -n borges-%{version}

find lib/ -name 'Test*' -type f -print0 | xargs -0 rm -v
find lib/ -name 'Test*' -type d -print0 | xargs -0 rm -v -r
mv data/doc/ruby/Borges/{RDoc,rdoc}

%build
ruby setup.rb config \
	--rb-dir=%{ruby_rubylibdir} \
	--so-dir=%{ruby_archdir}

ruby setup.rb setup

rdoc --ri --op ri lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{ruby_ridir}}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}
mv -f $RPM_BUILD_ROOT/usr/share/examples/* $RPM_BUILD_ROOT%{_examplesdir}

rm -r $RPM_BUILD_ROOT%{_docdir}/ruby/Borges

cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
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
%{_examplesdir}/*
