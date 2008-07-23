%define name	divider-applet
%define version 1.99.1
%define release  %mkrel 3

Summary:	Applet that adds a divider to your panel
Name:		%{name}
Version:    	%{version}
Release:	%{release}
License:	GPL
URL:            http://gqapplets.sourceforge.net
Group:		Graphical desktop/GNOME
Source0:	%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
Requires:	libgnomeui2
Requires:	libpanel-applet >= 2.0.0
BuildRequires:	libgnomeui2-devel
BuildRequires:  libpanel-applet-devel >= 2.0.0

%description
A GNOME panel applet that adds dividers to the panel similar to toolbar
dividers.

%prep
%setup -q

%build
%configure
%make

%install
rm -fr $RPM_BUILD_ROOT
%makeinstall_std GCONF_SCHEMA_CONFIG_SOURCE=

%post
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
gconftool-2 --makefile-install-rule /etc/gconf/schemas/divider-applet.schemas > /dev/null

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc README COPYING TODO ChangeLog
%{_libexecdir}/divider_applet2
%{_libdir}/bonobo/servers/GNOME_DividerApplet.server
%{_sysconfdir}/gconf/schemas/divider-applet.schemas
%{_datadir}/gnome-2.0/ui/GNOME_DividerApplet.xml
%{_datadir}/pixmaps/divider-applet.png
%{_datadir}/divider-applet

