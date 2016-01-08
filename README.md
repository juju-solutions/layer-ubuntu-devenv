# Overview

This is the 'ubuntu' charm with revision control tools preinstalled,
as well as relations to other developer-oriented charms. It is useful
as both a development environment and an endpoint for testing charms
like 'openjdk' and 'ibm-xlc'.


# Usage

An example use case for this charm is to test Java JRE or Java SDK
providers. This charm supports the `java` interface and serves as a
simple principal charm that can be used to relate to a `java`
subordinate. Deploy as follows:

    juju deploy ubuntu-devenv
    juju deploy openjdk
    juju add-relation ubuntu-devenv openjdk


# Contact Information

- <kevin.monroe@canonical.com>
