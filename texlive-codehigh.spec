Name:		texlive-codehigh
Version:	63175
Release:	2
Summary:	Highlight code and demos with l3regex and lpeg
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/codehigh
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/codehigh.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/codehigh.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package uses the l3regex package from the LaTeX3
Programming Layer to parse and highlight source code and demos.
It is more powerful than the listings package, and more easy to
use than minted. But it is slower than both of them. Therefore
in LuaTeX the package provides another way to highlight code:
using LPeg (Parsing Expression Grammars for Lua). LPeg is much
more powerful and faster than l3regex.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/codehigh
%doc %{_texmfdistdir}/doc/latex/codehigh

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
