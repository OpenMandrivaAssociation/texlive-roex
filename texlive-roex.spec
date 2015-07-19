# revision 15878
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-roex
Version:	20111104
Release:	10
Summary:	TeXLive roex package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/roex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/roex.source.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar metafont source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20111104-2
+ Revision: 755720
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111104-1
+ Revision: 719459
- texlive-roex
- texlive-roex
- texlive-roex
- texlive-roex

