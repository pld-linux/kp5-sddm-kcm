%define		kdeplasmaver	5.22.3
%define		qtver		5.9.0
%define		kpname		sddm-kcm

Summary:	KDE Config Module for SDDM
Name:		kp5-%{kpname}
Version:	5.22.3
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	b3c22bd4348d9b285773c3d4bb70b9dd
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-kauth-devel
BuildRequires:	kf5-kconfigwidgets-devel
BuildRequires:	kf5-kcoreaddons-devel
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-kio-devel
BuildRequires:	kf5-kxmlgui-devel
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
KDE Config Module for SDDM.

%prep
%setup -q -n %{kpname}-%{version}

%build
install -d build
cd build
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	../
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kpname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kpname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/kauth/kcmsddm_authhelper
%{_datadir}/dbus-1/system-services/org.kde.kcontrol.kcmsddm.service
%{_datadir}/kservices5/kcm_sddm.desktop
%{_datadir}/polkit-1/actions/org.kde.kcontrol.kcmsddm.policy
%attr(755,root,root) %{_bindir}/sddmthemeinstaller
%{_datadir}/dbus-1/system.d/org.kde.kcontrol.kcmsddm.conf
%{_datadir}/knsrcfiles/sddmtheme.knsrc
%attr(755,root,root) %{_libdir}/qt5/plugins/kcms/kcm_sddm.so
%dir %{_datadir}/kpackage/kcms/kcm_sddm
%dir %{_datadir}/kpackage/kcms/kcm_sddm/contents
%dir %{_datadir}/kpackage/kcms/kcm_sddm/contents/ui
%{_datadir}/kpackage/kcms/kcm_sddm/contents/ui/Advanced.qml
%{_datadir}/kpackage/kcms/kcm_sddm/contents/ui/DetailsDialog.qml
%{_datadir}/kpackage/kcms/kcm_sddm/contents/ui/main.qml
%{_datadir}/kpackage/kcms/kcm_sddm/metadata.desktop
%{_datadir}/kpackage/kcms/kcm_sddm/metadata.json
