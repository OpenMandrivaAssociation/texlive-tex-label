%global tl_name tex-label
%global tl_revision 16372

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Place a classification on each page of a document
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tex-label
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tex-label.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tex-label.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tex-label.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Enables the user to place a 'classification' label on each page, at the
bottom to the right of the page number

