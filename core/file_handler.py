import csv

class FileHandler:

    @staticmethod
    def read_csv(file_path):
        """
        Reads a CSV file and returns its content as a list of dictionaries.
        
        :param file_path: Path to the CSV file
        :return: List of dictionaries representing the CSV content
        """
        
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
        
    @staticmethod    
    def write_csv(file_path, data):
        """
        Writes a list of dictionaries to a CSV file.
        
        :param file_path: Path to the CSV file
        :param data: List of dictionaries to write
        """
        
        if not data:
            return
        
        with open(file_path, mode='w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)

