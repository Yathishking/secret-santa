import random
from models.Employee import Employee


class SecretSantaApp:
    def __init__(self, participants: list[Employee],
                previous_assignments: list[dict[str, str]]=None,
                constraints=None):
        """
        Initialize the SecretSanta class with a list of participants.

        :param participants: List of participants (e.g. Employee objects)
        :param previous_assignments: Optional previous assignments to avoid repeated pairings
        :param constraints: Optional list of constraints to apply during assignment
        :raises ValueError: If participants list is empty or contains less than 2 participants
        """ 

        if len(participants) < 2:
            raise ValueError("At least two participants are required for Secret Santa.")

        self.participants = participants
        self.previous_assignments = previous_assignments if previous_assignments else None
        self.constraints = constraints or [self.no_self_assignment, self.no_repeated_assignment]
        self.assigned_pairs = []

        self.start_assigning_child()


    def start_assigning_child(self):
        """
        Start the process of assigning secret children to participants.
        """

        shuffled_participants = self.participants[:]
        random.shuffle(shuffled_participants)
        participant_index = 0
        max_attempts = 1000
        attempts = 0

        while participant_index < len(self.participants):
            giver = self.participants[participant_index]
            receiver = shuffled_participants[participant_index]

            if self.is_valid_pair(giver, receiver):
                self.assign_secret_child(giver, receiver)
                participant_index += 1
            else:
                random.shuffle(shuffled_participants)
            
            attempts += 1
            if attempts > max_attempts:
                raise Exception("Unable to find a valid pairs after multiple attempts.")
                break

    def is_valid_pair(self, giver: Employee, receiver: Employee):
        """
        Check if the pair of giver and receiver is valid based on the constraints.

        :param giver: Employee object representing the santa
        :param receiver: Employee object representing the child
        
        :return: True if the pair is valid, False otherwise
        """

        return all(constraint(giver, receiver) for constraint in self.constraints)

    def no_self_assignment(self, giver: Employee, receiver: Employee):
        """
        Check if the giver and receiver are not the same person.

        :param giver: Employee object representing the santa
        :param receiver: Employee object representing the child

        :return: True if they are not the same, False otherwise
        """
        if giver.email == receiver.email:
            return False
        return True

    def no_repeated_assignment(self, giver: Employee, receiver: Employee):
        """
        Check if the giver and receiver have been assigned in previous years.

        :param giver: Employee object representing the santa
        :param receiver: Employee object representing the child

        :return: True if they have not been assigned same again, False otherwise
        """
        for assignment in self.previous_assignments:
            if (giver.email == assignment["Employee_EmailID"] and
                receiver.email == assignment["Secret_Child_EmailID"]):
                return False
        return True
    
    def assign_secret_child(self, giver: Employee, receiver: Employee):
        """
        Assign the valid secret child to the giver and store the assignment.

        :param giver: Employee object representing the giver
        :param receiver: Employee object representing the receiver
        """
        self.assigned_pairs.append({
            "Employee_Name": giver.name,
            "Employee_EmailID": giver.email,
            "Secret_Child_Name": receiver.name,
            "Secret_Child_EmailID": receiver.email
        })

    def get_assigned_list(self):
        return self.assigned_pairs