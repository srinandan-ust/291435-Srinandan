#import json
import unittest
import os
from storage import Storage
from employee import Employee

class TestStorage(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_employees.pkl"
        self.storage = Storage(self.test_file)
        self.test_data = [Employee("Sunil", "Supply Cahain", "Manager", 3200, 6, 50)]

    def test_save_data(self):
        self.storage.save(self.test_data)
        self.assertTrue(os.path.exists(self.test_file))

    def test_load_data(self):
        self.storage.save(self.test_data)
        loaded = self.storage.load()
        self.assertEqual(len(loaded), 1)
        self.assertEqual(loaded[0].name, "Sunil")

    def test_load_empty_when_file_not_exists(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        loaded = self.storage.load()
        self.assertEqual(loaded, [])

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

if __name__ == '__main__':
    unittest.main()