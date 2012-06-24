#
# Conditional build:
%bcond_without	dist_kernel	# without distribution kernel
%bcond_without	smp		# without smp packages
%bcond_without	kernel		# without kernel packages
%bcond_with	verbose		# verbose build (V=1)
#
%define		_nv_ver		1.0
%define		_nv_rel		7184
%define		_min_x11	6.7.0
%define		_rel		1
%define		_patchname	X11-driver-nvidia-legacy
#
Summary:	Linux Drivers for nVidia TNT/TNT2/GeForce/Quadro Chips
Summary(pl):	Sterowniki do kart graficznych nVidia TNT/TNT2/GeForce/Quadro
Name:		xorg-driver-video-nvidia-legacy
Version:	%{_nv_ver}.%{_nv_rel}
Release:	%{_rel}
License:	nVidia Binary
Vendor:		nVidia Corp.
Group:		X11/XFree86
# why not pkg0!?
Source0:	http://download.nvidia.com/XFree86/Linux-x86/%{_nv_ver}-%{_nv_rel}/NVIDIA-Linux-x86-%{_nv_ver}-%{_nv_rel}-pkg1.run
# Source0-md5:	68cf7f155786daf6946b9daeb64c7a35
Source1:	http://download.nvidia.com/XFree86/Linux-x86_64/%{_nv_ver}-%{_nv_rel}/NVIDIA-Linux-x86_64-%{_nv_ver}-%{_nv_rel}-pkg2.run
# Source1-md5:	332850387c4e7a4619753b856e3199e5
Patch0:		%{_patchname}-gcc34.patch
Patch1:		%{_patchname}-GL.patch
Patch2:		%{_patchname}-verbose.patch
# http://www.minion.de/files/1.0-6629/
URL:		http://www.nvidia.com/object/linux.html
BuildConflicts:	XFree86-nvidia
BuildRequires:	grep
%{?with_dist_kernel:BuildRequires:	kernel%{_alt_kernel}-module-build >= 2.6.7}
BuildRequires:	%{kgcc_package}
BuildRequires:	rpmbuild(macros) >= 1.326
BuildRequires:	sed >= 4.0
BuildRequires:	textutils
#BuildRequires:	X11-devel >= %{_min_x11}	# disabled for now
Requires:	X11-Xserver
Requires:	X11-libs >= %{_min_x11}
Requires:	X11-modules >= %{_min_x11}
Provides:	X11-OpenGL-core
Provides:	X11-OpenGL-libGL
Provides:	XFree86-OpenGL-core
Provides:	XFree86-OpenGL-libGL
Obsoletes:	Mesa
Obsoletes:	X11-OpenGL-core
Obsoletes:	X11-OpenGL-libGL
Obsoletes:	XFree86-OpenGL-core
Obsoletes:	XFree86-OpenGL-libGL
Obsoletes:	XFree86-driver-nvidia
Obsoletes:	XFree86-nvidia
Conflicts:	XFree86-OpenGL-devel <= 4.2.0-3
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLcore.so.1
%define		_prefix		/usr/X11R6
%ifarch %{x8664}
%define		_libdir32	%{_prefix}/lib
%endif

%description
This driver set adds improved 2D functionality to the XFree86 4.0 X
server as well as high performance OpenGL acceleration, AGP support,
support for most flat panels, and 2D multiple monitor support.

Hardware: nVidia TNT, TNT2, GeForce, or Quadro based graphics
accelerator. The nVidia NV1 and RIVA 128/128ZX chips are supported in
the base XFree86 4.0 install and are not supported by this driver set.

Software: Linux kernel >= 2.2.12, XFree86 >= 4.0.

%description -l pl
Usprawnione sterowniki dla kart graficznych nVidia do serwera XFree86
4.0, daj�ce wysokowydajn� akceleracj� OpenGL, obs�ug� AGP i wielu
monitor�w 2D.

Obs�uguj� karty nVidia TNT/TNT2/GeForce/Quadro do serwera XFree86 4.0;
Karty nVidia NV1 i Riva 128/128ZX s� obs�ugiwane przez sterownik nv z
pakiet�w XFree86 - NIE s� obs�ugiwane przez ten pakiet.

%package devel
Summary:	OpenGL for X11R6 development (only gl?.h)
Summary(pl):	Pliki nag��wkowe OpenGL dla systemu X11R6 (tylko gl?.h)
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	OpenGL-devel-base
Obsoletes:	OpenGL-devel-base
Obsoletes:	XFree86-driver-nvidia-devel
Conflicts:	XFree86-OpenGL-devel < 4.3.99.902-0.3

%description devel
Base headers (only gl?.h) for OpenGL for X11R6 for nvidia drivers.

%description devel -l pl
Podstawowe pliki nag��wkowe (tylko gl?.h) OpenGL dla systemu X11R6 dla
sterownik�w nvidii.

%package progs
Summary:	Tools for advanced control of nVidia graphic cards
Summary(pl):	Narz�dzia do zarz�dzania kartami graficznymi nVidia
Group:		Applications/System
Obsoletes:	XFree86-driver-nvidia-progs
Requires:	%{name} = %{version}-%{release}

%description progs
Tools for advanced control of nVidia graphic cards.

%description progs -l pl
Narz�dzia do zarz�dzania kartami graficznymi nVidia.

%package -n kernel%{_alt_kernel}-video-nvidia
Summary:	nVidia kernel module for nVidia Architecture support
Summary(de):	Das nVidia-Kern-Modul f�r die nVidia-Architektur-Unterst�tzung
Summary(pl):	Modu� j�dra dla obs�ugi kart graficznych nVidia
Version:	%{_nv_ver}.%{_nv_rel}
Release:	%{_rel}@%{_kernel_ver_str}
Group:		Base/Kernel
Requires(post,postun):	/sbin/depmod
Requires:	dev >= 2.7.7-10
%{?with_dist_kernel:%requires_releq_kernel_up}
Provides:	X11-driver-nvidia(kernel)
Obsoletes:	XFree86-nvidia-kernel

%description -n kernel%{_alt_kernel}-video-nvidia
nVidia Architecture support for Linux kernel.

%description -n kernel%{_alt_kernel}-video-nvidia -l de
Die nVidia-Architektur-Unterst�tzung f�r den Linux-Kern.

%description -n kernel%{_alt_kernel}-video-nvidia -l pl
Obs�uga architektury nVidia dla j�dra Linuksa. Pakiet wymagany przez
sterownik nVidii dla XFree86 4.

%package -n kernel%{_alt_kernel}-smp-video-nvidia
Summary:	nVidia kernel module for nVidia Architecture support
Summary(de):	Das nVidia-Kern-Modul f�r die nVidia-Architektur-Unterst�tzung
Summary(pl):	Modu� j�dra dla obs�ugi kart graficznych nVidia
Release:	%{_rel}@%{_kernel_ver_str}
Group:		Base/Kernel
Requires(post,postun):	/sbin/depmod
Requires:	dev >= 2.7.7-10
%{?with_dist_kernel:%requires_releq_kernel_smp}
Provides:	X11-driver-nvidia(kernel)
Obsoletes:	XFree86-nvidia-kernel

%description -n kernel%{_alt_kernel}-smp-video-nvidia
nVidia Architecture support for Linux kernel SMP.

%description -n kernel%{_alt_kernel}-smp-video-nvidia -l de
Die nVidia-Architektur-Unterst�tzung f�r den Linux-Kern SMP.

%description -n kernel%{_alt_kernel}-smp-video-nvidia -l pl
Obs�uga architektury nVidia dla j�dra Linuksa SMP. Pakiet wymagany
przez sterownik nVidii dla XFree86 4.

%prep
cd %{_builddir}
rm -rf NVIDIA-Linux-x86*-%{_nv_ver}-%{_nv_rel}-pkg*
%ifarch %{ix86}
/bin/sh %{SOURCE0} --extract-only
%setup -qDT -n NVIDIA-Linux-x86-%{_nv_ver}-%{_nv_rel}-pkg1
%else
/bin/sh %{SOURCE1} --extract-only
%setup -qDT -n NVIDIA-Linux-x86_64-%{_nv_ver}-%{_nv_rel}-pkg2
%endif
%patch0 -p1
%patch1 -p1
%if %{with verbose}
%patch2 -p0
%endif
sed -i 's:-Wpointer-arith::' usr/src/nv/Makefile.kbuild

%build
%if %{with kernel}
cd usr/src/nv/
ln -sf Makefile.kbuild Makefile
%build_kernel_modules -m nvidia
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/modules/{drivers,extensions} \
	$RPM_BUILD_ROOT{/usr/include/GL,/usr/%{_lib}/tls,%{_bindir}}

ln -sf $RPM_BUILD_ROOT%{_libdir} $RPM_BUILD_ROOT%{_prefix}/../lib

install usr/bin/nvidia-settings $RPM_BUILD_ROOT%{_bindir}
install usr/lib/libnvidia-tls.so.%{version} $RPM_BUILD_ROOT/usr/%{_lib}
install usr/lib/tls/libnvidia-tls.so.%{version} $RPM_BUILD_ROOT/usr/%{_lib}/tls
install usr/lib/libGL{,core}.so.%{version} $RPM_BUILD_ROOT%{_libdir}
install usr/X11R6/lib/modules/extensions/libglx.so.%{version} \
	$RPM_BUILD_ROOT%{_libdir}/modules/extensions
%ifarch %{x8664}
# support for running 32-bit OpenGL applications on 64-bit AMD64 Linux installations
#install -d $RPM_BUILD_ROOT%{_libdir32}
#install usr/lib32%{?with_tls:/tls}/libnvidia-tls.so.%{version} $RPM_BUILD_ROOT%{_libdir32}
#install usr/lib32/libGL{,core}.so.%{version} $RPM_BUILD_ROOT%{_libdir32}
%endif

install usr/X11R6/lib/modules/drivers/nvidia_drv.o $RPM_BUILD_ROOT%{_libdir}/modules/drivers
install usr/X11R6/lib/libXvMCNVIDIA.so.%{version} $RPM_BUILD_ROOT%{_libdir}
install usr/X11R6/lib/libXvMCNVIDIA.a $RPM_BUILD_ROOT%{_libdir}
install usr/include/GL/*.h	$RPM_BUILD_ROOT/usr/include/GL
#install usr/bin/nvidia-settings $RPM_BUILD_ROOT%{_bindir}

ln -sf libGL.so.1 $RPM_BUILD_ROOT%{_libdir}/libGL.so
ln -sf libglx.so.%{version} $RPM_BUILD_ROOT%{_libdir}/modules/extensions/libglx.so
ln -sf libXvMCNVIDIA.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libXvMCNVIDIA.so

# OpenGL ABI for Linux compatibility
ln -sf %{_libdir}/libGL.so.1 $RPM_BUILD_ROOT/usr/%{_lib}/libGL.so.1
ln -sf %{_libdir}/libGL.so $RPM_BUILD_ROOT/usr/%{_lib}/libGL.so

%if %{with kernel}
%install_kernel_modules -m usr/src/nv/nvidia -d misc
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
cat << EOF

 *******************************************************
 *                                                     *
 *  NOTE:                                              *
 *  You must install:                                  *
 *  kernel(24)(-smp)-video-nvidia-%{version}             *
 *  for this driver to work                            *
 *                                                     *
 *******************************************************

EOF

%postun	-p /sbin/ldconfig

%post	-n kernel%{_alt_kernel}-video-nvidia
%depmod %{_kernel_ver}

%postun	-n kernel%{_alt_kernel}-video-nvidia
%depmod %{_kernel_ver}

%post	-n kernel%{_alt_kernel}-smp-video-nvidia
%depmod %{_kernel_ver}smp

%postun	-n kernel%{_alt_kernel}-smp-video-nvidia
%depmod %{_kernel_ver}smp

%files
%defattr(644,root,root,755)
%doc LICENSE
%doc usr/share/doc/{README,NVIDIA_Changelog,XF86Config.sample}
#%%lang(de) %doc usr/share/doc/README.DE
%attr(755,root,root) %{_libdir}/libGL.so.*.*
%attr(755,root,root) %{_libdir}/libGL.so
%attr(755,root,root) %{_libdir}/libGLcore.so.*.*
%attr(755,root,root) %{_libdir}/libXvMCNVIDIA.so.*.*
%dir /usr/%{_lib}/tls
%attr(755,root,root) /usr/%{_lib}/libnvidia-tls.so.*.*.*
%attr(755,root,root) /usr/%{_lib}/tls/libnvidia-tls.so.*.*.*
%ifarch %{x8664}
# support for running 32-bit OpenGL applications on 64-bit AMD64 Linux installations
#dir %{_libdir32}
#attr(755,root,root) %{_libdir32}/libGL.so.*.*
#attr(755,root,root) %{_libdir32}/libGLcore.so.*.*
#attr(755,root,root) %{_libdir32}/libXvMCNVIDIA.so.*.*
#attr(755,root,root) %{_libdir32}/libnvidia-tls.so.*.*.*
%endif
%attr(755,root,root) /usr/%{_lib}/libGL.so.1
%attr(755,root,root) /usr/%{_lib}/libGL.so
%attr(755,root,root) %{_libdir}/modules/extensions/libglx.so*
%attr(755,root,root) %{_libdir}/modules/drivers/nvidia_drv.o

%if %{with kernel}
%files -n kernel%{_alt_kernel}-video-nvidia
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}/misc/*.ko*

%if %{with smp} && %{with dist_kernel}
%files -n kernel%{_alt_kernel}-smp-video-nvidia
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}smp/misc/*.ko*
%endif
%endif

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXvMCNVIDIA.so
/usr/include/GL/*.h
# -static
%{_libdir}/libXvMCNVIDIA.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/nvidia-settings
