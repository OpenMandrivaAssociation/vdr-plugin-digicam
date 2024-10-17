
%define plugin	digicam
%define name	vdr-plugin-%plugin
%define version	1.0.2
%define rel	6

Summary:	VDR plugin: Plugin to access a digital camera
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		https://turku.wi-bw.tfh-wildau.de/~pjuszack/digicam/index_en.html
Source:		http://194.95.44.38/~pjuszack/digicam/download/vdr-%plugin-%version.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.4.1-6
BuildRequires:	gphoto2-devel
Requires:	libgphoto-hotplug
Requires:	vdr-abi = %vdr_abi

%description
The 'control' plugin brings the ability to VDR to control
the whole OSD over a telnet client.

%prep
%setup -q -n %plugin-%version
chmod -x MANUAL HISTORY README INSTALL

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

install -d -m755 %{buildroot}%{_vdr_plugin_cfgdir}
install -m644 examples/*.conf %{buildroot}%{_vdr_plugin_cfgdir}

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY MANUAL INSTALL
%config(noreplace) %{_vdr_plugin_cfgdir}/digicam*.conf


