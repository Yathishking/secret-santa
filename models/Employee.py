class Employee:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_details(self):
        return f"Name: {self.name}, Email: {self.email}"

    def __str__(self):
        return f"Employee(Name: {self.name}, Email: {self.email})"
    
    @classmethod
    def create_employee(cls, name, email):
        """
        Create an Employee object with the given name and email.
        :param name: Name of the employee
        :param email: Email of the employee
        :return: Employee object
        """
        return Employee(name, email)