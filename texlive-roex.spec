%global tl_name roex
%global tl_revision 45818

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Metafont-PostScript conversions
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/MF-PS
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/roex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/roex.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A Metafont support package including: epstomf, a tiny AWK script for
converting EPS files into Metafont; mftoeps for generating
(encapsulated) PostScript files readable, e.g., by CorelDRAW, Adobe
Illustrator and Fontographer; a collection of routines (in folder progs)
for converting Metafont-coded graphics into encapsulated PostScript; and
roex.mf, which provides Metafont macros for removing overlaps and
expanding strokes. In mftoeps, Metafont writes PostScript code to a log-
file, from which it may be extracted by either TeX or AWK.

