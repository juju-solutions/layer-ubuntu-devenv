from subprocess import check_call

from charmhelpers.core.hookenv import status_set
from charms.reactive import hook

# No states are emitted from this charm. This is simply Ubuntu with a few
# VCS tools installed. The usefulness of this charm comes by way of the
# relations it supports (java for now, other languages to follow).


@hook('install')
def install():
    ''' Install VCS tooling '''
    status_set('maintenance', 'Installing VCS tools')
    check_call(['apt-get', 'install', '-y', 'bzr', 'cvs', 'git', 'subversion'])
    status_set('active', 'Ubuntu Dev Env ready!')
