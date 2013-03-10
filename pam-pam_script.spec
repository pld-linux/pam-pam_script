#
%define		modulename	pam_script
#
Summary:	PAM module for executing scripts
Summary(pl.UTF-8):	Moduł PAM do wywoływania skryptów
Name:		pam-%{modulename}
Version:	0.1.12
Release:	0.1
License:	GPL
Group:		Applications/System
Source0:	 http://www.upfrontsystems.co.za/Members/izak/libpam-script_%{version}.tar.gz
# Source0-md5:	6607c1093612269ecf539c404b89cf73
Patch0:		%{name}-Makefile.patch
URL:	    http://www.upfrontsystems.co.za/Members/izak
BuildRequires:	pam-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pam_script is a module which allows to execute scripts after opening
and/or closing a session using PAM.

%description -l pl.UTF-8
pam_script to moduł umożliwiający wywoływanie skryptów po otwarciu
i/lub zamknięciu sesji przy użyciu PAM.

%prep
%setup -q -n libpam-script-%{version}
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -include syslog.h"

%install
rm -rf $RPM_BUILD_ROOT

install -D pam_script.so $RPM_BUILD_ROOT/%{_lib}/security/pam_script.so
install -D pam_script.5 $RPM_BUILD_ROOT%{_mandir}/man5/pam_script.5

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README examples/kde
%attr(755,root,root) /%{_lib}/security/*
%{_mandir}/man?/*
