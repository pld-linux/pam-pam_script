#
%define		modulename	pam_script	
#
Summary:	PAM module for executing scripts
Summary(pl):	Modu³ PAM do wywo³ywania skryptów
Name:		pam-%{modulename}
Version:	0.1.5
Release:	0.1
License:	GPL
Group:		Applications/System
Source0:	http://www.bofs.co.za/~iburger/pam_script/pam-script-%{version}.tar.gz
# Source0-md5:	7ba4ba54e71298a4238b2191823c2eb6
Patch0:		%{name}-Makefile.patch
URL:		http://www.bofs.co.za/~iburger/pam_script/index.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pam_script is a module which allows to execute scripts after opening
and/or closing a session using PAM.

%description -l pl
pam_script to modu³ umo¿liwiaj±cy wywo³ywanie skryptów po otwarciu
i/lub zamkniêciu sesji przy u¿yciu PAM.

%prep
%setup -q -n pam-script-%{version}
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -D pam_script.so $RPM_BUILD_ROOT/%{_lib}/security/pam_script.so
install -D pam-script.5 $RPM_BUILD_ROOT/%{_mandir}/man5/pam_script.5

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog README examples/kde
%attr(755,root,root) /%{_lib}/security/*
%{_mandir}/man?/*
