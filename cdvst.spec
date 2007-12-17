%define	name	cdvst
%define	version	0.18
%define	release	%mkrel 7
%define Summary	Certain Death via Space Things

Summary:	%{Summary}
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://kokido.sourceforge.net/%{name}-.18.tar.bz2
Source1:	%{name}-icons.tar.bz2
Patch0:		%{name}-optflags.patch.bz2
Patch1:		%{name}-shared.patch.bz2
License:	GPL
Url:		http://kokido.sourceforge.net/cdvst.html
Group:		Games/Arcade
BuildRequires:	libSDL_mixer-devel libSDL_image-devel
BuildRequires:  desktop-file-utils

%description
The space things will certainly kill you :)
A top down scrolling putting you in the pilot seat of a space fighter.
Reminiscent of many old arcade games. 
 
%prep
%setup -q -n %{name}-.18

%patch0 -p0
%patch1 -p0

%build
%make OPTFLAGS="$RPM_OPT_FLAGS" DATA_PREFIX=%{_gamesdatadir}/%{name}/

%install
rm -rf $RPM_BUILD_ROOT
install -m755 cdvst -D $RPM_BUILD_ROOT%{_gamesbindir}/%{name}
chmod 644 readme.txt data/*
install -d $RPM_BUILD_ROOT%{_gamesdatadir}/%{name}
cp -a data $RPM_BUILD_ROOT%{_gamesdatadir}/%{name}

install -d %{buildroot}%{_menudir}
cat <<EOF > %{buildroot}%{_menudir}/%{name}
?package(%{name}):command="%{_gamesbindir}/%{name}" \
		  icon=%{name}.png \
		  needs="x11" \
		  section="More Applications/Games/Arcade" \
		  title="CDvST"\
		  longtitle="%{Summary}" \
                  xdg="true"
EOF

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=CDvST
Comment=%{Summary}
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=X-MandrivaLinux-MoreApplications-Games-Arcade;Game;ArcadeGame;
EOF

install -d ${RPM_BUILD_ROOT}{%{_miconsdir},%{_liconsdir}}
tar -xOjf %{SOURCE1} icons/16x16.png > ${RPM_BUILD_ROOT}%{_miconsdir}/%{name}.png
tar -xOjf %{SOURCE1} icons/32x32.png > ${RPM_BUILD_ROOT}%{_iconsdir}/%{name}.png
tar -xOjf %{SOURCE1} icons/48x48.png > ${RPM_BUILD_ROOT}%{_liconsdir}/%{name}.png

%post
%update_menus

%postun
%clean_menus

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc readme.txt
%{_gamesbindir}/%{name}
%dir %{_gamesdatadir}/%{name}
%{_gamesdatadir}/%{name}
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_menudir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop

