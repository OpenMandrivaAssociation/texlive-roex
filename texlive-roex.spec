Name:		texlive-roex
Version:	45818
Release:	2
Summary:	TeXLive roex package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/roex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/roex.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive roex package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/metafont/roex/roex.mf
#- source
%doc %{_texmfdistdir}/source/metafont/roex/0roex.doc
%doc %{_texmfdistdir}/source/metafont/roex/roexsamp/0roexsam.doc
%doc %{_texmfdistdir}/source/metafont/roex/roexsamp/es-01.mf
%doc %{_texmfdistdir}/source/metafont/roex/roexsamp/es-02.mf
%doc %{_texmfdistdir}/source/metafont/roex/roexsamp/es-03.mf
%doc %{_texmfdistdir}/source/metafont/roex/roexsamp/ro-01.mf
%doc %{_texmfdistdir}/source/metafont/roex/roexsamp/ro-02.mf
%doc %{_texmfdistdir}/source/metafont/roex/roexsamp/ro-03.mf
%doc %{_texmfdistdir}/source/metafont/roex/roexsamp/ro-04.mf
%doc %{_texmfdistdir}/source/metafont/roex/roexsamp/ro-05.mf
%doc %{_texmfdistdir}/source/metafont/roex/roexsamp/ro-06.mf
%doc %{_texmfdistdir}/source/metafont/roex/roexsamp/ro-07.mf
%doc %{_texmfdistdir}/source/metafont/roex/roexsamp/roes-01.mf
%doc %{_texmfdistdir}/source/metafont/roex/roexsamp/roes-02.mf
%doc %{_texmfdistdir}/source/metafont/roex/roexsamp/roes-03.mf
%doc %{_texmfdistdir}/source/metafont/roex/roexsamp/roes-04.mf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar metafont source %{buildroot}%{_texmfdistdir}
