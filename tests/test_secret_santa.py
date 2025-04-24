from datetime import datetime
import os
import unittest

from core.file_handler import FileHandler
from src.AppInit import AppInit

class TestSecretSantaApp(unittest.TestCase):
    def setUp(self):
        self.input_file = "input.csv"
        self.prev_file = "prev.csv"

        # Create a sample input file
        FileHandler.write_csv(self.input_file, [
            {"Employee_Name": "Ninja", "Employee_EmailID": "ninja@game.com"},
            {"Employee_Name": "Coult", "Employee_EmailID": "coult@more.com"}
        ])

    def tearDown(self):
        # Remove the input file after tests
        if os.path.exists(self.input_file):
            os.remove(self.input_file)
        if os.path.exists(self.prev_file):
            os.remove(self.prev_file)
        output_file = f"./secret_santa_child_{datetime.now().year}.csv"
        if os.path.exists(output_file):
            os.remove(output_file)

    def test_file_creation(self):
        
        self.assertTrue(os.path.exists(self.input_file))

        # Fake previous assignment file
        FileHandler.write_csv(self.prev_file, [
            {"Employee_Name": "Ninja", "Employee_EmailID": "ninja@game.com",
              "Secret_Child_Name": "Max", "Secret_Child_EmailID": "Max@more.com"},
        ])
        self.assertTrue(os.path.exists(self.prev_file))
        
        # Instantiate the AppInit class and run the method
        app_init = AppInit(self.input_file, previous_assignment=self.prev_file)
        app_init.run()
        # check if the output file is created with the new generated data
        self.assertTrue(os.path.exists(f"./secret_santa_child_{datetime.now().year}.csv"))
        
        output_file = f"./secret_santa_child_{datetime.now().year}.csv"
        # check if the file is not empty
        self.assertTrue(os.path.getsize(output_file) > 0)
        
        with open(output_file, 'r') as file:
            header = file.readline().strip().split(',')
            self.assertEqual(header, ["Employee_Name", "Employee_EmailID", "Secret_Child_Name", "Secret_Child_EmailID"])
        
        with open(output_file, 'r') as file:
            lines = file.readlines()[1:]
            for line in lines:
                data = line.strip().split(',')
                self.assertEqual(len(data), 4) # check if there are 4 columns


    def test_same_pair_raises_error(self):
        # Test if the same pair is not assigned again
        FileHandler.write_csv(self.prev_file, [
            {"Employee_Name": "Ninja", "Employee_EmailID": "ninja@game.com",
              "Secret_Child_Name": "Coult", "Secret_Child_EmailID": "coult@more.com"}
        ])

        app_init = AppInit(self.input_file, previous_assignment=self.prev_file)
        # raises exception if same pair is assigned
        # the new pair cannot be assigned since the previous pair is same
        # which results in a max try error
        self.assertRaises(Exception, app_init.run) 
        # Check if the output file is not created  
        output_file = f"./secret_santa_child_{datetime.now().year}.csv"
        self.assertFalse(os.path.exists(output_file))
     
    def test_no_previous_assignment_raises_error(self):
        # Test if the program raises error when no previous assignment file is provided
        with self.assertRaises(FileNotFoundError):
            app_init = AppInit(self.input_file)
            app_init.run()
        