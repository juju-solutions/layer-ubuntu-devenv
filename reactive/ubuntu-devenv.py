from charmhelpers.core.hookenv import log, status_set
from charms.reactive import is_state, set_state, when, when_not
from charms.reactive.helpers import data_changed

# No states are emitted from this charm. This is simply Ubuntu with a few
# VCS tools installed. The usefulness of this charm comes by way of the
# relations it supports (java, xlc, xlf).


@when_not('ubuntu-devenv.installed')
def install():
    """Set the installed state.

    The install function doesn't need to do anything (vcs packages are
    installed with the base layer options). Set our installed state and an
    active status message.
    """
    set_state('ubuntu-devenv.installed')
    status_set('active', 'devenv ready')


@when('ubuntu-devenv.installed')
def update_status():
    """Update status based on related charm states."""
    ready_services = []
    if is_state('java.ready'):
        ready_services.append('java')
    if is_state('xlc.ready'):
        ready_services.append('xlc')
    if is_state('xlf.ready'):
        ready_services.append('xlf')

    if ready_services:
        status_suffix = ' with: %s' % (', '.join(ready_services))
    else:
        status_suffix = ''
    status_set('active', 'devenv ready%s' % (status_suffix))


@when('ubuntu-devenv.installed', 'java.ready')
def log_java_details(java):
    """Log pertinent Java-related details."""
    if (data_changed('java.version', java.java_version())
            or data_changed('java.home', java.java_home())):

        log("Java (%s) using JAVA_HOME: '%s'" %
            (java.java_version(), java.java_home()))
