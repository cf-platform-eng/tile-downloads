import unittest
import main

class TestDataLoad(unittest.TestCase):

    def test_load_fixture(self):
        data = main.load_data('appdynamics')
        self.assertIsNotNone(data)

    def test_load_non_existent_fixture(self):
        with self.assertRaises(FileNotFoundError):
            main.load_data('nonsense')

if __name__ == '__main__':
    unittest.main()