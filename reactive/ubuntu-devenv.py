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
    if is_state('db2.ready'):
        ready_services.append('db2')
    if is_state('java.ready'):
        ready_services.append('java')
    if is_state('mysql.available'):
        ready_services.append('mysql')
    if is_state('pgsql.database.available'):
        ready_services.append('pgsql')
    if is_state('xlc.ready'):
        ready_services.append('xlc')
    if is_state('xlf.ready'):
        ready_services.append('xlf')

    if ready_services:
        status_suffix = ' with: %s' % (', '.join(ready_services))
    else:
        status_suffix = ''
    status_set('active', 'devenv ready%s' % (status_suffix))


@when('ubuntu-devenv.installed', 'db2.connected')
def send_db2_details(db2):
    """
    DB2 requires an ssh key to be sent from the client to the server before
    the relation will become ready. We don't actually need ssh access for this
    charm, so send an invalid string as our key.
    """
    db2.set_ssh_keys("Invalid")


@when('ubuntu-devenv.installed', 'db2.ready')
def log_db2_details(db2):
    """Log pertinent DB2-related details."""
    if (data_changed('db2.host', db2.get_db2_hostname())):
        log("DB2 host: '%s'" % db2.get_db2_hostname())
        log("DB2 port: '%s'" % db2.get_db2_port())
        log("DB2 user: '%s'" % db2.get_dbusername())
        log("DB2 pass: '%s'" % db2.get_dbuserpw())
        log("DB2 db: '%s'" % db2.get_db2_dbnames())


@when('ubuntu-devenv.installed', 'java.ready')
def log_java_details(java):
    """Log pertinent Java-related details."""
    if (data_changed('java.version', java.java_version())
            or data_changed('java.home', java.java_home())):

        log("Java (%s) using JAVA_HOME: '%s'" %
            (java.java_version(), java.java_home()))


@when('ubuntu-devenv.installed', 'mysql.available')
def log_mysql_details(mysql):
    """Log pertinent Mysql-related details."""
    if (data_changed('mysql.host', mysql.host())):
        log("Mysql connection string: '%s'" % mysql.connection_string())


@when('ubuntu-devenv.installed', 'pgsql.database.available')
def log_pgsql_details(pgsql):
    """Log pertinent Postgres-related details."""
    if (data_changed('pgsql.host', pgsql.host())):
        log("Postgres connection string: '%s'" % pgsql.connection_string())
