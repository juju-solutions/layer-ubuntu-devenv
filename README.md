# Overview

This layered charm provides the same functionality as the 'ubuntu' charm with
revision control tools preinstalled, as well as relations to other
developer-oriented charms. It is useful as both a development environment and
an endpoint for testing charms like 'openjdk' and 'ibm-xlc'.

Source for this charm is available on
[github](https://github.com/juju-solutions/layer-ubuntu-devenv).


# Usage

An example use case for this charm is to test Java JRE or Java SDK
providers. This charm supports the `java` interface and serves as a
simple principal charm that can be used to relate to a `java`
subordinate. Deploy as follows:

    juju deploy cs:~kwmonroe/trusty/ubuntu-devenv
    juju deploy cs:~kwmonroe/trusty/openjdk
    juju add-relation ubuntu-devenv openjdk


# Limitations

This charm does not currently have any config options, nor does it scale.
This may change if other relations are added that would benefit from such
functionality.


# Contact Information

- <kevin.monroe@canonical.com>
