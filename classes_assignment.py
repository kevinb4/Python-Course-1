class Individual():
    """Defines the base class for an individual"""

    def __init__(self, id, name, email):
        """Initializes the Individual class"""

        self.id = id
        self.name = name
        self.email = email

class Student(Individual):
    """Defines the student class that inherits from the Individual class"""

    def __init__(self, id, name, email, program):
        """Initializes the student class which inherits the individual class"""
        super().__init__(id, name, email)

        self.program = program

    def displayInformation(self):
        """Returns of all the data in the student class so it can be added to a list"""

        return { 'individual_type': 'Student', 'id': self.id, 'name': self.name, 'email': self.email, 'program_of_study': self.program }

class Instructor(Individual):
    """Defines the instructor class that inherits from the Individual class"""

    def __init__(self, id, name, email, institution_graduated, highest_degree_earned):
        """Initializes the instructor class that inherits the individual class"""

        super().__init__(id, name, email)

        self.institution_graduated = institution_graduated
        self.highest_degree_earned = highest_degree_earned

    def displayInformation(self):
        """Returns of all the data in the instructor class so it can be added to a list"""

        return { 'individual_type': 'Instructor', 'id': self.id, 'name': self.name, 'email': self.email, 'institution_graduated': self.institution_graduated, 'highest_degree_earned': self.highest_degree_earned }

class Validator():
    """Defines the validator class that will validate user input"""

    def __init__(self, data, individual_type):
        """Initializes the validator class"""

        self.data = data
        self.individual_type = individual_type

    def validate_input(self):
        """Ensures the user entered a value"""

        if self.data:
            return True
        else:
            return False

    def validate_individual(self):
        """Validates the type of individual"""

        if self.data.lower() == "student" or self.data.lower() == "instructor":
            return True
        else:
            return False

    def validate_id(self):
        """Validates the ID for students or instructors"""

        length = 0

        if self.individual_type == "student":
            length = 7
        elif self.individual_type == "instructor":
            length = 5
        else: # this should not happen, but just in case
            return False

        if self.data.isdigit() and len(self.data) <= length:
            return True
        else:
            return False

    def validate_char(self, data_type):
        """Validates name or email"""

        char_list = []

        if data_type == "name":
            # setup custom char filter - add numbers since a name cannot contain numbers because using isalpha would return false if the user has a period in their name, which isn't on the special characters list
            char_list = ['!', '"', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '=', '+', ',', '<', '>', '/', '?', ';', ':', '[', ']', '{', '}', '\\',
                         '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        elif data_type == "email":
            # setup custom char filter
            char_list = ['!', '"', '\'', '#', '$', '%', '^', '&', '*', '(', ')', '=', '+', ',', '<', '>', '/', '?', ';', ':', '[', ']', '{', '}', '\\']
        else: # this should not happen, but just in case
            return False

        passed = False

        for char in self.data:
            if char in char_list:
                passed = False
                break # stop if a bad char is found or else it could be set to true from the next char
            else:
                passed = True

        return passed

def get_data(data_type, individual = ""):
    message = "Please enter the "

    # modify the message depending on the data type
    if data_type == "individual":
        message += "type of individual (student or instructor): "
    else:
        message += f"{individual}'s {data_type}: "

    data = input(message)
    data_ok = False

    while not data_ok:
        check = Validator(data, individual) # initiate the validator class right away since it will be used regardless of the type

        # handle specific data types with the specific validator methods
        if data_type == "individual":
            data_ok = check.validate_individual()
        elif data_type == "id":
            data_ok = check.validate_id()
        elif data_type == "name" or data_type == "email": # name and email use the same method for good code reuse
            data_ok = check.validate_char(data_type)
        else: # handles the remaining info required for the individual
            data_ok = check.validate_input()

        if not data_ok:
            data = input(f"\"{data}\" is an invalid entry for a(n) {data_type}, please try again: ")

    return data

cont = True
college_records = []

while cont:
    individual = get_data("individual")
    id = get_data("id", individual)
    name = get_data("name", individual)
    email = get_data("email", individual)

    if individual == "student": # handle student's specific information
        program = get_data("program of study", individual)

        # create new student instance and add the collected data
        student = Student(id, name, email, program)

        # append the data to the list using the displayInformation method so the data is readable
        college_records.append(student.displayInformation())
    elif individual == "instructor": # handle instructor's specific information
        institution = get_data("institution graduated", individual)
        degree = get_data("highest degree earned", individual)

        # create new instructor instance and add the collected data
        instructor = Instructor(id, name, email, institution, degree)

        # append the data to the list using the displayInformation method so the data is readable
        college_records.append(instructor.displayInformation())

    response = input("Add another individual? (Y/N): ")
    if response.lower() == "n":
        cont = False # we only need to set continue to false since it's already true

# output all of the entries in the list
print(college_records)