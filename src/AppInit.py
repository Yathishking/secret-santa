import os
from datetime import datetime
from models.Employee import Employee
from src.SecretSantaApp import SecretSantaApp
from core.file_handler import FileHandler
from utils.clear_bom import clean_bom_keys


class AppInit:
    def __init__(self, input_path: str, previous_assignment: str = None, ouptut_path: str = None):
        """
        Initialize the AppInit class with input and output paths.

        :param input_path: Path to the input CSV file
        :param ouptut_path: Path to the output CSV file
        :param previous_assignment: Path to the previous year's secret santa CSV file
        """
        self.input_path = input_path
        self.output_path = ouptut_path
        self.previous_assignment = previous_assignment

    def run(self):
        """
        Run the Secret Santa assignment process.
        This method reads the input file, creates Employee objects, and generates
        secret santa assignments. It also handles file reading and writing.
        """
        
        # check if the input file and previous assignment csv file exist
        if not os.path.exists(self.input_path):
            raise FileNotFoundError(f"Input file '{self.input_path}' not found.")
    
        if not os.path.exists(self.previous_assignment):
            raise FileNotFoundError(f"Previous assignment file '{self.previous_assignment}' not found.")

        # read the input file and create Employee objects
        data = FileHandler.read_csv(self.input_path)
        data = clean_bom_keys(data) # Clean BOM keys if necessary
        data = [Employee.create_employee(name=i['Employee_Name'],
            email=i['Employee_EmailID']) for i in data] # Create Employee objects from the data
    
        # read previous year secret santa data from csv
        previous_assignments =  FileHandler.read_csv(self.previous_assignment)
        previous_assignments = clean_bom_keys(previous_assignments) # Clean BOM keys if necessary

        secret_santa = SecretSantaApp(data, previous_assignments)
        assignments = secret_santa.get_assigned_list()
        print("Secret Santa assignments have been successfully generated.")
        print("Please check the output for details.")
    
        # Write the output to the csv
        output_file_path = self.output_path or f"./secret_santa_child_{datetime.now().year}.csv"
        FileHandler.write_csv(output_file_path, assignments)
        print(f"Output csv: {output_file_path}")
        
    