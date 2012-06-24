%define		_realname	pinball
%define		_snap		2007-01-20_sea1.1
Summary:	Great theme - it doesn't take much space
Summary(pl):	Przepi�kny motyw - idealny kompromis pomi�dzy rozmiarem i czytelno�ci�
Name:		seamonkey-theme-pinball
Version:	2007.01.20
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://mozilla-themes.schellen.net/%{_realname}_%{_snap}.jar
# Source0-md5:	9cfdaf385bd3c6a05d4d5404410f85e7
Source1:	gen-installed-chrome.sh
URL:		http://mozilla-themes.schellen.net/
Requires(post,postun):	seamonkey >= 1.1
Requires(post,postun):	textutils
Requires:	seamonkey >= 1.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_chromedir	%{_datadir}/seamonkey/chrome

%description
The great theme, very good in low resolutions (800x600) - it doesn't
take much space, but it's still nice.

%description -l pl
Przepi�kny motyw, kt�ry wy�mienicie nadaje si� do u�ywania w niskich
rozdzielczo�ciach (800x600), gdy� zajmuje niewielk� powierzchni�
ekranu nie trac�c przy tym na urodzie.

%prep
%setup -q -c -T
install %{SOURCE0} %{_realname}.jar
install %{SOURCE1} .
./gen-installed-chrome.sh skin %{_realname}.jar > %{_realname}-installed-chrome.txt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

install %{_realname}.jar $RPM_BUILD_ROOT%{_chromedir}
install %{_realname}-installed-chrome.txt $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/seamonkey-chrome+xpcom-generate

%postun
%{_sbindir}/seamonkey-chrome+xpcom-generate

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt
