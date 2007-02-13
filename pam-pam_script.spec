#
%define		modulename	pam_script
#
Summary:	PAM module for executing scripts
Summary(pl.UTF-8):	Moduł PAM do wywoływania skryptów
Name:		pam-%{modulename}
Version:	0.1.6
Release:	0.1
License:	GPL
Group:		Applications/System
Source0:	http://www.bofs.co.za/~iburger/pam_script/pam-script-%{version}.tar.gz
# Source0-md5:	b9041c84649e94373564e8edd14ffbec
Patch0:		%{name}-Makefile.patch
URL:		http://www.bofs.co.za/~iburger/pam_script/index.html
BuildRequires:	pam-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pam_script is a module which allows to execute scripts after opening
and/or closing a session using PAM.

%description -l pl.UTF-8
pam_script to moduł umożliwiający wywoływanie skryptów po otwarciu
i/lub zamknięciu sesji przy użyciu PAM.

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
install -D pam-script.5 $RPM_BUILD_ROOT%{_mandir}/man5/pam_script.5

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog README examples/kde
%attr(755,root,root) /%{_lib}/security/*
%{_mandir}/man?/*
