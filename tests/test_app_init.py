from datetime import datetime
import os
import unittest
from src.AppInit import AppInit
from core.file_handler import FileHandler

class TestAppInit(unittest.TestCase):
    def setUp(self):
        self.input_file = "input.csv"
        self.prev_file = "prev.csv"

        FileHandler.write_csv(self.input_file, [
            {"Employee_Name": "Ninja", "Employee_EmailID": "ninja@me.com"},
            {"Employee_Name": "Coult", "Employee_EmailID": "coult@more.com"}
        ])

        FileHandler.write_csv(self.prev_file, [
            {"Employee_Name": "Ninja", "Employee_EmailID": "ninja@me.com",
              "Secret_Child_Name": "Coult", "Secret_Child_EmailID": "coult.jr@more.com"},
        ])

    def tearDown(self):
        os.remove(self.input_file)
        os.remove(self.prev_file)
        output_file = f"./secret_santa_child_{datetime.now().year}.csv"
        if os.path.exists(output_file):
            os.remove(output_file)

    def test_run(self):
        app_init = AppInit(self.input_file, previous_assignment=self.prev_file)
        app_init.run()
        self.assertTrue(os.path.exists(f"./secret_santa_child_{datetime.now().year}.csv"))

    def test_empty_input_file(self):
        empty_file = "empty.csv"
        FileHandler.write_csv(empty_file, [])
        app_init = AppInit(empty_file, previous_assignment=self.prev_file)
        with self.assertRaises(FileNotFoundError):
            app_init.run()
