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

%install
# FIXME: A trivial %%install is needed to mkdir %%buildroot, which is required.
# It's a workaround for the following issue: to find autodeps of the scriptlet,
# rpm-build-4.0.4-alt170 wants to write its code to a file under
# %%buildroot in generateDepends() and saveInstScript() (in build/files.c):
#
# error: cannot write /usr/src/tmp/rpmscript_warn_only-pre-checkinstall-buildroot/.pre:rpmscript_warn_only-pre-checkinstall
#
# but fails to do so if %%buildroot has not been created; then it ignores
# this failure and doesn't generate additional deps from the scriptlet.
# The only deps added to the package are "Requires(interp,pre): /bin/sh" then
# (if it's a %%pre scriptlet) by parseScript() (from build/parseScript.c):
#
#    if (pkg->autoReq && *pkg->autoReq)
#    (void) addReqProv(spec, pkg->header, (tagflags | RPMSENSE_INTERP), progArgv[0], NULL, 0);
#
# which are then printed as:
#
# Requires(interp): /bin/sh
# Requires(pre): /bin/sh
#
# Probably, a fix would be not ignore the failure to write the script to a file
# (because in this case the expectations on how rpm-build works are broken)\
# and to automatically create the dir if needed (asin this case)--so that
# existing packages don't fail to build with the "fixed@ rpm-build.
mkdir %buildroot

%@scriptlet@
exit 1

%files

%changelog
* Tue Jul 20 2021 Ivan Zakharyaschev <imz@altlinux.org> 1-alt1
- initial version
