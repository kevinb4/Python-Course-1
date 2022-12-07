def bad_char_check(passed_input, data_type):
    passed = False
    char_list = []

    if data_type == "name":
        # setup custom char filter - add numbers since a name cannot contain numbers because using isalpha would return false if the user has a period in their name, which isn't on the special characters list
        char_list = ['!', '"', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '=', '+', ',', '<', '>', '/', '?', ';', ':', '[', ']', '{' '}', '\\',
                          '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    elif data_type == "email":
        # setup custom char filter
        char_list = ['!', '"', '\'', '#', '$', '%', '^', '&', '*', '(', ')', '=', '+', ',', '<', '>', '/', '?', ';', ':', '[', ']', '{', '}', '\\']
    elif data_type == "address":
        # setup custom char filter
        char_list = ['!', '"', '\'', '@', '$', '%', '^', '&', '*', '_', '=', '+', '<', '>', '?', ';', ':', '[', ']', '{', '}']
    else: # this shouldn't happen but it's good to have a safety net
        print("Failed to get illegal character list")
        return False

    for char in passed_input:
        if char in char_list:
            passed = False
            break # stop if a bad char is found or else it could be set to true from the next char
        else:
            passed = True
            
    return passed

def get_data(data_type):
    msg = f"Please enter your employee {data_type}"

    # inform the user address is optional when prompted
    if data_type == "address":
        msg = f"{msg} (optional): "
    else:
        msg = f"{msg}: "

    data = input(msg) # get data
    data_ok = False

    while not data_ok:
        if not data and data_type != "address": # handle nothing entered as long as it's not the address
            data_ok = False
        elif not data and data_type == "address": # handle the optional address
            data_ok = True
        elif data_type == "id": # special handler for id since it doesn't use the char checker
            if data.isdigit() and len(data) <= 7: # make sure input is a valid number and that it's 7 or less digits
                data_ok = True
            else:
                data_ok = False
        else:
            data_ok = bad_char_check(data, data_type)

        if not data_ok:
            data = input(f"The {data_type} you entered is not valid, please enter characters only used in a {data_type}: ")

    return data

cont = True
employees = []

while cont:
    id = get_data("id")
    name = get_data("name")
    email = get_data("email")
    address = get_data("address")

    # make sure to only include addresses if the user entered one
    if address:
        employees.append({ 'id': id, 'name': name, 'email': email, 'address': address })
    else:
        employees.append({ 'id': id, 'name': name, 'email': email })

    # check to make sure the max amount of employees hasn't been reached
    if len(employees) < 5:
        response = input("Add another employee? (Y/N): ")
        if response.lower() == "n":
            cont = False # we only need to set continue to false since it's already true
    else:
        cont = False # to make sure it doesn't ask more than five times

print(employees)