# Secret Santa

A Python-based application to assign secret santa to a given list of employees.

## Features

- Randomized pairings for participants.
- Ensures no one is paired with themselves.
- Option to exclude specific pairings.
- Easy-to-use and customizable.

## Folder Structure
```
└── 📁Secret_Santa
    └── 📁core
        └── __init__.py
        └── file_handler.py  -- Handle csv files reading and writing
    └── 📁data
        └── employee_list.csv
        └── santa_secret_child_2023.csv
    └── 📁models
        └── Employee.py  --  Empolyee model to store employee data
    └── 📁output
        └── secret_santa_assignments.csv
    └── 📁src
        └── __init__.py
        └── AppInit.py  --  AppInit class to initialize the app
        └── SecretSantaApp.py --  SecretSantaApp class to handle the secret santa logic
    └── 📁tests
        └── test_app_init.py
        └── test_employee.py
        └── test_secret_santa.py
    └── 📁utils
        └── __init__.py
        └── clear_bom.py
        └── cli.py
    └── .gitignore
    └── main.py  -- main python file where execution starts
    └── readme.md
    └── requirements.txt
    └── secret-santa.spec
    └── setup.py -- setup file to create executable which runs on linux and windows for now. (no macos since I don't have any macos system)
```

## Installation

1. Clone the repository:
    ```
    git clone https://github.com/Yathishking/secret-santa.git
    ```
2. Navigate to the project directory:
    ```
    cd secret-santa
    ```
3. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```

## Usage

### Code usage:

    All the dependencies need to installed before executing the `main.py` using the above installation commands or try executing the executable.

1. Input the CSV file path and previous assignment CSV using the below command.
2. Run the script:
    ```
    python main.py employee_list_csv_path previous_csv_path [optional] output_file_path
    ```
3. View the generated pairings in the output csv file.

### Executable (no installation required)

All the executables can be found in the `dist` folder.

1. Open a terminal in your system.
2. Select an executable for your operating system(windows and linux).
3. Run the executable with providing input csv file path and previous year assignment csv file path.
    
    For windows:
    ```
    main.exe employee_list_csv_path previous_csv_path [optional] output_file_path
    ```


    For linux:
    ``` 
    secret-santa employee_list_csv_path previous_csv_path [optional] output_file_path
    ```
4. View the generated pairings in the output csv file.

### Output

1. The output file will be generated in the folder of executable or in the folder where you run the script.
2. The output file will be named `secret_santa_child_2025.csv` by default, but you can specify a different name by providing the `output_file_path` argument.

### Test

1. Run the following command to run the tests in a terminal in the folder root.
2. For linux: 
    ```
    python3 -m unittest tests.test_name
    ```
    
    For windows:
    ```
    python -m unittest tests.test_name
    ```
    Here test_name is the test file name in the tests folder.


3. You can also run all the tests at once using the below command.
    ```
    python -m unittest discover tests
    ```
    All the tests can be found in the tests folder.
    
