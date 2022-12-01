id = input("Please enter your employee ID: ")
id_ok = False # use a bool to keep track instead of nesting a bunch of if's

# id section
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

# end id section

# name section
name_ok = False
if id_ok: # move on to the next input if the previous one passed validation
    name = input("Please enter your employee name: ")
    name_ok = False

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

# end name section

# email section
email_ok = False
if name_ok: # move on to the next input if the previous one passed validation
    email = input("Please enter your email: ")
    email_ok = False

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

# end email section

# address section
address_ok = False
if email_ok: # move on to the next input if the previous one passed validation
    address = input("Please enter your address (optional): ")
    address_ok = False

    if not address: # to skip address
        address_ok = True
    else:
        # setup custom char filter
        bad_address_chars = ['!', '"', '\'', '@', '$', '%', '^', '&', '*', '_', '=', '+', '<', '>', '?', ';', ':', '[', ']', '{', '}']

        for char in address:
            if char in bad_address_chars:
                address_ok = False
                break # stop if a bad char is found or else it could be set to true from the next char
            else:
                address_ok = True

# end address section

# output message section
if address_ok: # move on to the next input if the previous one passed validation
    message = f"Hello, {name}. Your Employee ID is {id}, and your email address is {email}. "
    
    if address: # check for address so we can change the message based off of if it's there or not
        message = message + f"Your address is {address}."
    else:
        message = message + "You did not provide an address."

    print(message)