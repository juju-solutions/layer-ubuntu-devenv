from charmhelpers.core.hookenv import status_set
from charms.reactive import set_state, when_not

# No states are emitted from this charm. This is simply Ubuntu with a few
# VCS tools installed. The usefulness of this charm comes by way of the
# relations it supports (java, xlc, xlf).


@when_not('ubuntu-devenv.installed')
def install():
    '''
    This charm doesn't need to do anything (vcs packages are installed
    with layer options). Notify the user that we're ready.
    '''
    status_set('active', 'Ubuntu Dev Env ready!')
    set_state('ubuntu-devenv.installed')
