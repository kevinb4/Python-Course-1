id = input("Please enter your employee ID: ")
id_ok = False # use a bool to keep track instead of nesting a bunch of if's

# id section
if not id:
    id_ok = False
else:
    if id.isdigit():
        if len(id) < 7:
            id_ok = True
        else:
            id_ok = False
    else:
        id_ok = False

# end id section

# name section
if id_ok: # move on to the next input if the previous one passed validation
    name = input("Please enter your employee name: ")
    name_ok = False

    if name:
        if name.isalpha():
            name_ok = True
        else:
            name_ok = False
    else:
        name_ok = False

# end name section

# email section
if name_ok:
    email = input("Please enter your email: ")
    email_ok = False

    # setup bad char list since we have not been introducted to a python function that will check for all special chars except @
    bad_email_chars = ['!', '"', '\'', '#', '$', '%', '^', '&', '*', '(', ')', '=', '+', ',', '<', '>', '/', '?', ';', ':', '[', ']', '{', '}', '\\']

    if email:
        for char in email:
            if char in bad_email_chars:
                email_ok = False
                break # stop if a bad char is found or else it could be set to true from the next char
            else:
                email_ok = True
    else:
        email_ok = False

# end email section

# address section
if email_ok:
    address = input("Please enter your address (optional): ")
    address_ok = False

    if not address: # to skip address
        address_ok = True
    else:
         # setup bad char list since we have not been introducted to a python function that will check for all special chars except a few
        bad_address_chars = ['!', '"', '\'', '$', '%', '^', '&', '*', '=', '+', '<', '>', '?', ';', ':', '[', ']', '{', '}']

        for char in address:
            if char in bad_address_chars:
                address_ok = False
                break
            else:
                address_ok = True

# end address section

# output message section
if address_ok:
    message = f"Hello, {name}. Your Employee ID is {id}, and your email address is {email}. "
    
    if address:
        message = message + f"Your address is {address}."
    else:
        message = message + "You did not provide an address."

    print(message)