Summary:	Free UCS font for Egyptian hieroglyphs
Summary(pl.UTF-8):	Wolnodostępny font UCS dla hieroglifów egipskich
Name:		fonts-OTF-Aegyptus
Version:	3.11
%define	_ver	%(echo %{version} | tr -d .)
Release:	1
License:	Freeware
Group:		Fonts
Source0:	http://users.teilar.gr/~g1951d/Aegyptus%{_ver}.zip
# Source0-md5:	de9426b4fbed2ce23d6121effce36ba9
URL:		http://users.teilar.gr/~g1951d/
BuildRequires:	iconv
BuildRequires:	unzip
Requires(post,postun):	fontpostinst
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		otffontsdir	%{_fontsdir}/OTF

%description
The Aegyptus font encodes some 7100 Egyptian Hieroglyphs, all with a
graphical representation. The main sources of glyphs are Hieroglyphica
<http://www.ccer.nl/product8.html> and the work of Alan Gardiner
<http://std.dkuug.dk/JTC1/SC2/WG2/docs/n3182.pdf>. Egyptian
Hieroglyphs are allocated in the Supplementary Private Use Plane 15,
for the lack of a standard. The font also covers Basic Latin, Egyptian
Transliteration characters, Meroitic, some Punctuation and other
Symbols and the Gardiner set of Egyptian Hieroglyphs supported by The
Unicode Standard 5.2

%%description -l pl.UTF-8
#TODO

%prep
%setup -q -c

%build
for i in *.txt; do
	iconv -f utf16 -t utf8 < $i > $i.
	mv -f $i. $i
done

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{otffontsdir}

install *.otf $RPM_BUILD_ROOT%{otffontsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst OTF

%postun
fontpostinst OTF

%files
%defattr(644,root,root,755)
%doc *.txt
%{otffontsdir}/Aegyptus.otf
