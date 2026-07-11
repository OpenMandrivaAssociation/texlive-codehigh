%global tl_name codehigh
%global tl_revision 78632

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2025C
Release:	%{tl_revision}.1
Summary:	Highlight code and demos with l3regex and LPeg
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/codehigh
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/codehigh.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/codehigh.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package uses the l3regex package from the LaTeX3 Programming Layer
to parse and highlight source code and demos. It is more powerful than
the listings package, and more easy to use than minted. But it is slower
than both of them. Therefore in LuaTeX the package provides another way
to highlight code: using LPeg (Parsing Expression Grammars for Lua).
LPeg is much more powerful and faster than l3regex.

