%define		efl_ver		1.7.0

Summary:	ConnMan User Interface in EFL
Summary(pl.UTF-8):	Interfejs użytkownika do ConnMana wykorzystujący EFL
Name:		econnman
Version:	1.1
Release:	1
License:	BSD
Group:		Applications/Network
Source0:	http://download.enlightenment.org/rel/apps/econnman/%{name}-%{version}.tar.gz
# Source0-md5:	64ccd94e8f2d92a91447566ee2af67e6
URL:		http://enlightenment.org/
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake >= 1.6
BuildRequires:	edje
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.6
BuildRequires:	sed >= 4.0
Requires:	python-dbus
Requires:	python-edbus >= 1.7.0
Requires:	python-elementary >= 1.7.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ConnMan User Interface in EFL.

%description -l pl.UTF-8
Interfejs użytkownika do ConnMana wykorzystujący EFL.

%prep
%setup -q

%build
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
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
