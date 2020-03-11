import unittest
import shortuuid


from native_shortuuid import NativeShortUUIDField


class ClassShortUUIDTest(unittest.TestCase):
    def test_to_python(self):
        val = NativeShortUUIDField().to_python('CXc85b4rqinB7s5J52TRYb')
        self.assertEqual(val, shortuuid.decode('CXc85b4rqinB7s5J52TRYb'))

    def test_from_db_value(self):
        val = NativeShortUUIDField().from_db_value(shortuuid.decode('CXc85b4rqinB7s5J52TRYb'), None , None)
        self.assertEqual(val, shortuuid.encode(shortuuid.decode('CXc85b4rqinB7s5J52TRYb')))