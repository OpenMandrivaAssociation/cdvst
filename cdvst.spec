%define	name	cdvst
%define	version	0.18
%define release	12
%define Summary	Certain Death via Space Things

Summary:	%{Summary}
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://kokido.sourceforge.net/%{name}-.18.tar.bz2
Source1:	%{name}-icons.tar.bz2
Patch0:		%{name}-optflags.patch.bz2
Patch1:		%{name}-shared.patch.bz2
License:	GPLv2
Url:		https://kokido.sourceforge.net/cdvst.html
Group:		Games/Arcade
BuildRequires:	pkgconfig(SDL_mixer)
BuildRequires:	pkgconfig(SDL_image)
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
%make OPTFLAGS="$RPM_OPT_FLAGS -lm" DATA_PREFIX=%{_gamesdatadir}/%{name}/

%install
install -m755 cdvst -D $RPM_BUILD_ROOT%{_gamesbindir}/%{name}
chmod 644 readme.txt data/*
install -d $RPM_BUILD_ROOT%{_gamesdatadir}/%{name}
cp -a data $RPM_BUILD_ROOT%{_gamesdatadir}/%{name}


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


%files
%doc readme.txt
%{_gamesbindir}/%{name}
%{_gamesdatadir}/%{name}
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_datadir}/applications/mandriva-%{name}.desktop



