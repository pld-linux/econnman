Summary:	ConnMan User Interface in EFL
Summary(pl.UTF-8):	Interfejs użytkownika do ConnMana wykorzystujący EFL
Name:		econnman
Version:	1.1
Release:	2
License:	BSD
Group:		Applications/Network
Source0:	https://download.enlightenment.org/rel/apps/econnman/%{name}-%{version}.tar.xz
# Source0-md5:	9cc318e26fcb11b66d8ac46ffe64af0a
URL:		http://enlightenment.org/
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake >= 1.6
BuildRequires:	efl-devel
BuildRequires:	pkgconfig
BuildRequires:	python3-devel >= 1:2.6
BuildRequires:	sed >= 4.0
Requires:	python3-dbus
Requires:	python3-efl >= 1.7.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ConnMan User Interface in EFL.

%description -l pl.UTF-8
Interfejs użytkownika do ConnMana wykorzystujący EFL.

%prep
%setup -q

%{__sed} -E -i -e '1s,#!\s*/usr/bin/python(\s|$),#!%{__python3}\1,' \
	econnman-bin.in

%build
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
PYTHON=%{__python3} \
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/econnman-bin
%{_datadir}/econnman
%{_desktopdir}/econnman.desktop
%{_desktopdir}/econnman-agent.desktop
