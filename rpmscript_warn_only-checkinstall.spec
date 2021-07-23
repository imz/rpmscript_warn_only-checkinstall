Name: rpmscript_warn_only-@scriptlet@-checkinstall
Version: 1
Release: alt1

Summary: A trivial test package whose %%@scriptlet@ scriptlet has non-zero exit status

License: MIT
Group: System/Configuration/Packaging
Url: http://git.altlinux.org/people/imz/packages/rpmscript_warn_only-checkinstall.git

#BuildArch: noarch

%description
A non-zero exit status of a scriptlet can be either a warning only or
a fatal error of rpm (depending on the version of rpm, the class of
the scriptlet, and the configuration of rpm).

It should be treated as a fatal error in the install check of Girar builder.

So, if this package passes the check (by causing a warning only), then
Girar builder works wrong. It is expected that this test (represented
by this package) fails in Girar (when it is installed at the install
check stage).

%@scriptlet@
exit 1

%files

%changelog
* Tue Jul 20 2021 Ivan Zakharyaschev <imz@altlinux.org> 1-alt1
- initial version
