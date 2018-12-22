# https://stackoverflow.com/questions/1732438/how-do-i-run-all-python-unit-tests-in-a-directory
# Unit test files must start with test_ to be run automagically.
import unittest
loader = unittest.TestLoader()
start_dir = '.'
suite = loader.discover(start_dir)

runner = unittest.TextTestRunner()
runner.run(suite)