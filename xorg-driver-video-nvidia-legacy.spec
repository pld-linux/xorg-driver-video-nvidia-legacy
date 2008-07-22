#
# Conditional build:
%bcond_without	dist_kernel	# without distribution kernel
%bcond_without	kernel		# without kernel packages
%bcond_without	userspace	# don't build userspace programs
%bcond_with	verbose		# verbose build (V=1)

%if "%{_alt_kernel}" != "%{nil}"
%undefine	with_userspace
%endif

%define		pname		xorg-driver-video-nvidia-legacy
%define		rel		1

Summary:	Linux Drivers for old nVidia TNT/TNT2/GeForce/Quadro Chips
Summary(pl.UTF-8):	Sterowniki do starych kart graficznych nVidia TNT/TNT2/GeForce/Quadro
Name:		%{pname}%{_alt_kernel}
Version:	71.86.06
Release:	%{rel}
License:	nVidia Binary
Group:		X11
Source0:	http://us.download.nvidia.com/XFree86/Linux-x86/%{version}/NVIDIA-Linux-x86-%{version}-pkg1.run
# Source0-md5:	dc9635a78dfb02cb533e2061866b70ce
Source1:	http://us.download.nvidia.com/XFree86/Linux-x86_64/%{version}/NVIDIA-Linux-x86_64-%{version}-pkg2.run
# Source1-md5:	6d91b113d56e05ab16584ccb221aa48f
Patch0:		X11-driver-nvidia-legacy-gcc34.patch
Patch1:		X11-driver-nvidia-legacy-GL.patch
Patch2:		%{pname}-desktop.patch
URL:		http://www.nvidia.com/object/unix.html
BuildRequires:	%{kgcc_package}
%if %{with kernel} && %{with dist_kernel}
BuildRequires:	kernel%{_alt_kernel}-module-build >= 3:2.6.20.2
%endif
BuildRequires:	rpmbuild(macros) >= 1.379
BuildConflicts:	XFree86-nvidia
Requires:	xorg-xserver-server
Requires:	xorg-xserver-server(videodrv-abi) = 2.0
Provides:	OpenGL = 1.5
Provides:	OpenGL-GLX = 1.3
Provides:	xorg-xserver-libglx
Obsoletes:	Mesa
Obsoletes:	X11-OpenGL-core < 1:7.0.0
Obsoletes:	X11-OpenGL-libGL < 1:7.0.0
Obsoletes:	XFree86-OpenGL-core < 1:7.0.0
Obsoletes:	XFree86-OpenGL-libGL < 1:7.0.0
Obsoletes:	XFree86-driver-nvidia
Obsoletes:	XFree86-nvidia
Conflicts:	Mesa-libGL
Conflicts:	XFree86-OpenGL-devel <= 4.2.0-3
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLcore.so.1

%description
This driver set adds improved 2D functionality to the Xorg X server as
well as high performance OpenGL acceleration, AGP support, support for
most flat panels, and multiple monitor support.

Hardware: nVidia TNT, TNT2, GeForce, old GeForce2 or Quadro based
graphics accelerator. New GeForce2, GeForce3 and GeForce4 adapters are
supported by xorg-driver-video-nvidia package. The nVidia NV1 and RIVA
128/128ZX chips are supported by Open-Source nv driver from Xorg suite
and are no longer supported by vendor proprietary drivers.

%description -l pl.UTF-8
Usprawnione sterowniki dla kart graficznych nVidia do serwera Xorg X,
dające wysokowydajną akcelerację OpenGL, obsługę AGP i wielu
monitorów.

Obsługują karty nVidia TNT/TNT2/GeForce/starsze GeForce2/Quadro.
Nowsze karty GeForce2, GeForce3 i GeForce4 są obsługiwane przez pakiet
xorg-driver-video-nvidia. Karty nVidia NV1 i Riva 128/128ZX są
obsługiwane przez otwarty sterownik nv z instalacji Xorg i nie są już
obsługiwane przez własnościowe sterowniki producenta.

%package devel
Summary:	OpenGL (GL and GLX) header files
Summary(pl.UTF-8):	Pliki nagłówkowe OpenGL (GL i GLX)
Group:		X11/Development/Libraries
Requires:	%{pname} = %{version}-%{release}
Provides:	OpenGL-GLX-devel = 1.3
Provides:	OpenGL-devel = 1.5
Obsoletes:	X11-OpenGL-devel-base
Obsoletes:	XFree86-OpenGL-devel-base
Obsoletes:	XFree86-driver-nvidia-devel
Conflicts:	XFree86-OpenGL-devel < 4.3.99.902-0.3

%description devel
OpenGL header files (GL and GLX only) for NVIDIA OpenGL
implementation.

%description devel -l pl.UTF-8
Pliki nagłówkowe OpenGL (tylko GL i GLX) dla implementacji OpenGL
firmy NVIDIA.

%package static
Summary:	Static XvMCNVIDIA library
Summary(pl.UTF-8):	Statyczna biblioteka XvMCNVIDIA
Group:		X11/Development/Libraries
Requires:	%{pname}-devel = %{version}-%{release}

%description static
Static XvMCNVIDIA library.

%description static -l pl.UTF-8
Statyczna biblioteka XvMCNVIDIA.

%package progs
Summary:	Tools for advanced control of nVidia graphic cards
Summary(pl.UTF-8):	Narzędzia do zarządzania kartami graficznymi nVidia
Group:		Applications/System
Requires:	%{pname} = %{version}-%{release}
Obsoletes:	XFree86-driver-nvidia-progs

%description progs
Tools for advanced control of nVidia graphic cards.

%description progs -l pl.UTF-8
Narzędzia do zarządzania kartami graficznymi nVidia.

%package -n kernel%{_alt_kernel}-video-nvidia-legacy
Summary:	nVidia kernel module for nVidia Architecture support
Summary(de.UTF-8):	Das nVidia-Kern-Modul für die nVidia-Architektur-Unterstützung
Summary(pl.UTF-8):	Moduł jądra dla obsługi kart graficznych nVidia
Release:	%{rel}@%{_kernel_ver_str}
Group:		Base/Kernel
Requires(post,postun):	/sbin/depmod
Requires:	dev >= 2.7.7-10
%{?with_dist_kernel:%requires_releq_kernel}
Provides:	X11-driver-nvidia(kernel)
Obsoletes:	XFree86-nvidia-kernel

%description -n kernel%{_alt_kernel}-video-nvidia-legacy
nVidia Architecture support for Linux kernel.

%description -n kernel%{_alt_kernel}-video-nvidia-legacy -l de.UTF-8
Die nVidia-Architektur-Unterstützung für den Linux-Kern.

%description -n kernel%{_alt_kernel}-video-nvidia-legacy -l pl.UTF-8
Obsługa architektury nVidia dla jądra Linuksa. Pakiet wymagany przez
sterownik nVidii dla XFree86 4.

%prep
cd %{_builddir}
rm -rf NVIDIA-Linux-x86*%{version}-pkg*
%ifarch %{ix86}
/bin/sh %{SOURCE0} --extract-only
%setup -qDT -n NVIDIA-Linux-x86-%{version}-pkg1
%else
/bin/sh %{SOURCE1} --extract-only
%setup -qDT -n NVIDIA-Linux-x86_64-%{version}-pkg2
%endif
%patch0 -p1
%patch1 -p1
%patch2 -p1
echo 'EXTRA_CFLAGS += -Wno-pointer-arith -Wno-sign-compare -Wno-unused' >> usr/src/nv/Makefile.kbuild

%build
%if %{with kernel}
cd usr/src/nv/
ln -sf Makefile.kbuild Makefile
cat >> Makefile <<'EOF'

$(obj)/nv-kernel.o: $(src)/nv-kernel.o.bin
	cp $< $@
EOF
mv nv-kernel.o{,.bin}
%build_kernel_modules -m nvidia
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{with userspace}
install -d $RPM_BUILD_ROOT%{_includedir}/GL

install -D {usr/bin,$RPM_BUILD_ROOT%{_bindir}}/nvidia-settings
install -D {usr/lib/tls,$RPM_BUILD_ROOT%{_libdir}}/libnvidia-tls.so.%{version}
install -D {usr/X11R6/lib,$RPM_BUILD_ROOT%{_libdir}/xorg}/modules/extensions/libglx.so.%{version}
install -D {usr/lib,$RPM_BUILD_ROOT%{_libdir}}/libGL.so.%{version}
install -D {usr/lib,$RPM_BUILD_ROOT%{_libdir}}/libGLcore.so.%{version}
install -D {usr/X11R6/lib,$RPM_BUILD_ROOT%{_libdir}}/libXvMCNVIDIA.so.%{version}
install -D {usr/X11R6/lib,$RPM_BUILD_ROOT%{_libdir}}/libXvMCNVIDIA.a

install -D {usr/X11R6/lib,$RPM_BUILD_ROOT%{_libdir}/xorg}/modules/drivers/nvidia_drv.so
install usr/include/GL/*.h $RPM_BUILD_ROOT%{_includedir}/GL

ln -sf libglx.so.%{version} $RPM_BUILD_ROOT%{_libdir}/xorg/modules/extensions/libglx.so
ln -sf libXvMCNVIDIA.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libXvMCNVIDIA.so
ln -sf libXvMCNVIDIA.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libXvMCNVIDIA_dynamic.so.1

# OpenGL ABI for Linux compatibility
ln -sf libGL.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libGL.so.1
ln -sf libGL.so.1 $RPM_BUILD_ROOT%{_libdir}/libGL.so

install -D {usr/share/applications,$RPM_BUILD_ROOT%{_desktopdir}}/nvidia-settings.desktop
install -D {usr/share/pixmaps,$RPM_BUILD_ROOT%{_pixmapsdir}}/nvidia-settings.png
%endif

%if %{with kernel}
%install_kernel_modules -m usr/src/nv/nvidia -d misc
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
cat << EOF
NOTE: You must install:
kernel-video-nvidia-legacy-%{version}
for this driver to work
EOF

%postun	-p /sbin/ldconfig

%post	-n kernel%{_alt_kernel}-video-nvidia-legacy
%depmod %{_kernel_ver}

%postun	-n kernel%{_alt_kernel}-video-nvidia-legacy
%depmod %{_kernel_ver}

%if %{with userspace}
%files
%defattr(644,root,root,755)
%doc LICENSE usr/share/doc/{README,NVIDIA_Changelog,XF86Config.sample}
%attr(755,root,root) %{_libdir}/libGL.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libGL.so.1
# symlink for binary apps which fail to conform Linux OpenGL ABI
# (and dlopen libGL.so instead of libGL.so.1)
%attr(755,root,root) %{_libdir}/libGL.so
%attr(755,root,root) %{_libdir}/libGLcore.so.*.*
%attr(755,root,root) %{_libdir}/libXvMCNVIDIA.so.*.*
%attr(755,root,root) %{_libdir}/libXvMCNVIDIA_dynamic.so.1
%attr(755,root,root) %{_libdir}/libnvidia-tls.so.*.*.*
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/nvidia_drv.so
%attr(755,root,root) %{_libdir}/xorg/modules/extensions/libglx.so*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXvMCNVIDIA.so
%dir %{_includedir}/GL
%{_includedir}/GL/gl.h
%{_includedir}/GL/glext.h
%{_includedir}/GL/glx.h
%{_includedir}/GL/glxtokens.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libXvMCNVIDIA.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/nvidia-settings
%{_desktopdir}/nvidia-settings.desktop
%{_pixmapsdir}/nvidia-settings.png
%endif

%if %{with kernel}
%files -n kernel%{_alt_kernel}-video-nvidia-legacy
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}/misc/*.ko*
%endif
