count = 1
cont = True
employees = []

while cont:
    id = input("Please enter your employee ID: ")
    id_ok = False

    while not id_ok:
        if not id: # no user entry
            id_ok = False
        else:
            if id.isdigit(): # make sure input is a valid number
                if len(id) <= 7: # make sure it's 7 or less digits
                    id = int(id) # must be a number (integer)
                    id_ok = True
                else:
                    id_ok = False
            else:
                id_ok = False

        if not id_ok:
            id = input("The ID you entered is invalid, please enter a seven digit ID: ")

    name = input("Please enter your employee name: ")
    name_ok = False

    while not name_ok:
        # setup custom char filter - add numbers since a name cannot contain numbers because using isalpha would return false if the user has a period in their name, which isn't on the special characters list
        bad_name_chars = ['!', '"', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '=', '+', ',', '<', '>', '/', '?', ';', ':', '[', ']', '{' '}', '\\',
                          '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

        if name:
            for char in name:
                if char in bad_name_chars:
                    name_ok = False
                    break # stop if a bad char is found or else it could be set to true from the next char
                else:
                    name_ok = True
        else: # no user entry
            name_ok = False

        if not name_ok:
            name = input("The name you entered is not valid, please enter a name with alphabet characters only: ")


    email = input("Please enter your email: ")
    email_ok = False

    while not email_ok:
        # setup custom char filter
        bad_email_chars = ['!', '"', '\'', '#', '$', '%', '^', '&', '*', '(', ')', '=', '+', ',', '<', '>', '/', '?', ';', ':', '[', ']', '{', '}', '\\']

        if email:
            for char in email:
                if char in bad_email_chars:
                    email_ok = False
                    break # stop if a bad char is found or else it could be set to true from the next char
                else:
                    email_ok = True
        else: # no user entry
            email_ok = False

        if not email_ok:
            email = input("The email you entered is not valid, please enter an email only using alphanumeric characters and the special characters \"@\" and \".\": ")


    address = input("Please enter your address (optional): ")
    address_ok = False

    while not address_ok:
        if not address: # to skip address
            address_ok = True
        else:
            # setup custom char filter
            bad_address_chars = ['!', '"', '\'', '@', '$', '%', '^', '&', '*', '_', '=', '+', '<', '>', '?', ';', ':', '[', ']', '{', '}']

            for char in address:
                if char in bad_address_chars:
                    address_ok = False
                    break
                else:
                    address_ok = True

        if not address_ok:
            address = input("The address you entered is not valid, please enter an address only using special characters in addresses: ")

    # make sure to only include addresses if the user entered one
    if address:
        employees.append({ 'id': id, 'name': name, 'email': email, 'address': address})
    else:
        employees.append({ 'id': id, 'name': name, 'email': email})

    # increment so the loop is finite
    count = count + 1

    # check to make sure the max amount of employees hasn't been reached
    if count <= 5:
        response = input("Add another employee? (Y/N): ")
        if response.lower() == "n":
            cont = False # we only need to set cont to false since it's already true
    else:
        cont = False # to make sure it doesn't ask more than five times

print(employees)