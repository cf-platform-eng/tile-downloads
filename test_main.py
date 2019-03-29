import unittest
import main
import datetime

class TestDataLoad(unittest.TestCase):

    def test_load_fixture(self):
        data = main.load_data('appdynamics')
        self.assertIsNotNone(data)

    def test_load_non_existent_fixture(self):
        with self.assertRaises(FileNotFoundError):
            main.load_data('nonsense')

    def test_load_datetime(self):
        date = datetime.datetime.strptime("2017-09-21 13:49:38 UTC", '%Y-%m-%d %H:%M:%S %Z')
        self.assertEqual(date.year, 2017)

if __name__ == '__main__':
    unittest.main()