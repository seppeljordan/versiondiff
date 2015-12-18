import unittest

from pkg_resources import parse_version
from distutils import version

class TestBetaVersion(unittest.TestCase):
    '''Test if beta versions are handled correctly'''

    def test_only_newer_setuptools(self):
        beta = '0.1b4'
        stable = '0.1'
        self.assertTrue(parse_version(beta) < parse_version(stable))

    def test_only_newer_distutils(self):
        beta = '0.1b4'
        stable = '0.1'
        self.assertTrue(version.LooseVersion(beta) < version.LooseVersion(stable))

suite = unittest.TestLoader().loadTestsFromTestCase(TestBetaVersion)
unittest.TextTestRunner(verbosity=2).run(suite)
