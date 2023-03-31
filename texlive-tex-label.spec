Name:		texlive-tex-label
Version:	16372
Release:	2
Summary:	Place a classification on each page of a document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tex-label
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tex-label.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tex-label.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tex-label.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Enables the user to place a 'classification' label on each
page, at the bottom to the right of the page number.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tex-label/tex-label.sty
%doc %{_texmfdistdir}/doc/latex/tex-label/README
%doc %{_texmfdistdir}/doc/latex/tex-label/tex-label-demo.pdf
%doc %{_texmfdistdir}/doc/latex/tex-label/tex-label-demo.tex
%doc %{_texmfdistdir}/doc/latex/tex-label/tex-label-doc.pdf
%doc %{_texmfdistdir}/doc/latex/tex-label/tex-label-doc.tex
#- source
%doc %{_texmfdistdir}/source/latex/tex-label/Makefile

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
