# Overview

This layered charm provides the same functionality as the 'ubuntu' charm with
revision control tools preinstalled, as well as relations to other
developer-oriented charms. It is useful as both a development environment and
an endpoint for testing charms like 'openjdk', 'ibm-xlc', and various
databases.

Source for this charm is available on
[github](https://github.com/juju-solutions/layer-ubuntu-devenv).


# Usage

## Use Case 1

An example use case for this charm is to test Java JRE or Java SDK
providers. This charm supports the `java` interface and serves as a
simple principal charm that can be used to relate to a `java`
subordinate. Deploy as follows:

    juju deploy ubuntu-devenv
    juju deploy openjdk
    juju add-relation ubuntu-devenv openjdk

## Use Case 2

Another use case is to test database charms. This charm supports the `db2`,
`mysql`, and `pgsql` interfaces. Once related, connection information will
be logged to the debug log. Deploy as follows:

    juju deploy ubuntu-devenv
    juju deploy mariadb
    juju add-relation ubuntu-devenv mariadb


# Verification

Verify you see relation data (java version, database connection information,
etc) in the debug log:

    juju debug-log -i unit-ubuntu-devenv-0 --replay


# Limitations

This charm does not currently have any config options, nor does it scale.
This may change if other relations are added that would benefit from such
functionality.


# Contact Information

- <kevin.monroe@canonical.com>
