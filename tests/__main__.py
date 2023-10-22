import os
import sys
import unittest

testdir = os.path.dirname(__file__)
srcdir = '../'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

loader = unittest.TestLoader()
testSuite = loader.discover('tests')
testRunner = unittest.TextTestRunner(verbosity=2)
testRunner.run(testSuite)