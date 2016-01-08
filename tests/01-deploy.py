#!/usr/bin/env python3

import unittest
import amulet


class TestDeploy(unittest.TestCase):
    """
    Deployment test for the Ubuntu Dev Env charm.

    This charm doesn't do much by itself, so we expect functional
    tests to happen in the subordinate charms that relate to this
    (for example, openjdk).
    """

    @classmethod
    def setUpClass(cls):
        cls.d = amulet.Deployment(series='trusty')
        cls.d.add('ubuntu-devenv', 'cs:~kwmonroe/trusty/ubuntu-devenv-1')
        cls.d.add('openjdk', 'cs:~kwmonroe/trusty/openjdk-1')
        cls.d.relate('ubuntu-devenv:java', 'openjdk:java')
        cls.d.setup(timeout=900)
        cls.d.sentry.wait(timeout=1800)
        cls.unit = cls.d.sentry['ubuntu-devenv'][0]

    def test_vcs(self):
        output, rc = self.unit.run("bzr version")
        assert rc == 0, "Unexpected output from bzr: %s" % output

        output, rc = self.unit.run("cvs version")
        assert rc == 0, "Unexpected output from cvs: %s" % output

        output, rc = self.unit.run("git version")
        assert rc == 0, "Unexpected output from git: %s" % output

        output, rc = self.unit.run("svn --version --quiet")
        assert rc == 0, "Unexpected output from svn: %s" % output

    def test_java(self):
        output, rc = self.unit.run("java -version")
        assert 'OpenJDK' in output, "OpenJDK should be in %s" % output

if __name__ == '__main__':
    unittest.main()
