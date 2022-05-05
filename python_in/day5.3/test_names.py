from function_test import get_name
import unittest

class NamesTestCase(unittest.TestCase):
    def test_name(self):
        fullname = get_name('ava','diana')
        self.assertEqual(fullname,'Ava Diana')

unittest.main()