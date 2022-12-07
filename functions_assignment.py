def bad_char_check(passed_input, type):
    passed = False

    if type == "name":
        # setup custom char filter - add numbers since a name cannot contain numbers because using isalpha would return false if the user has a period in their name, which isn't on the special characters list
        list = ['!', '"', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '=', '+', ',', '<', '>', '/', '?', ';', ':', '[', ']', '{' '}', '\\',
                          '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    elif type == "email":
        # setup custom char filter
        list = ['!', '"', '\'', '#', '$', '%', '^', '&', '*', '(', ')', '=', '+', ',', '<', '>', '/', '?', ';', ':', '[', ']', '{', '}', '\\']
    elif type == "address":
        # setup custom char filter
        list = ['!', '"', '\'', '@', '$', '%', '^', '&', '*', '_', '=', '+', '<', '>', '?', ';', ':', '[', ']', '{', '}']
    else: # this shouldn't happen but it's good to have a safety net
        print("Failed to get illegal character filters")
        return

    for char in passed_input:
        if char in list:
            passed = False
            break # stop if a bad char is found or else it could be set to true from the next char
        else:
            passed = True
            
    return passed

def get_id():
    id = input("Please enter your employee ID: ")
    id_ok = False

    while not id_ok:
        if not id: # no user entry
            id_ok = False
        else:
            if id.isdigit() and len(id) <= 7: # make sure input is a valid number and that it's 7 or less digits
                id_ok = True
            else:
                id_ok = False

        if not id_ok:
            id = input("The ID you entered is invalid, please enter a seven digit ID: ")

    return id

def get_name():
    name = input("Please enter your employee name: ")
    name_ok = False

    while not name_ok:
        if name:
            name_ok = bad_char_check(name, "name")
        else: # no user entry
            name_ok = False

        if not name_ok:
            name = input("The name you entered is not valid, please enter a name with alphabet characters only: ")

    return name

def get_email():
    email = input("Please enter your email: ")
    email_ok = False

    while not email_ok:
        if email:
            email_ok = bad_char_check(email, "email")
        else: # no user entry
            email_ok = False

        if not email_ok:
            email = input("The email you entered is not valid, please enter an email only using alphanumeric characters and the special characters \"@\" and \".\": ")

    return email

def get_address():
    address = input("Please enter your address (optional): ")
    address_ok = False

    while not address_ok:
        if not address: # to skip address
            address_ok = True
        else:
            address_ok = bad_char_check(address, "address")

        if not address_ok:
            address = input("The address you entered is not valid, please enter an address only using special characters in addresses: ")

    return address

cont = True
employees = []

while cont:
    id = get_id()
    name = get_name()
    email = get_email()
    address = get_address()

    # make sure to only include addresses if the user entered one
    if address:
        employees.append({ 'id': id, 'name': name, 'email': email, 'address': address})
    else:
        employees.append({ 'id': id, 'name': name, 'email': email})

    # check to make sure the max amount of employees hasn't been reached
    if len(employees) <= 5:
        response = input("Add another employee? (Y/N): ")
        if response.lower() == "n":
            cont = False # we only need to set continue to false since it's already true
    else:
        cont = False # to make sure it doesn't ask more than five times

print(employees)