# signup.py - Placeholder for signup functionality

import string
def is_password_secure(password):
    
    uppercase=0
    lowercase=0
    digit=0
    special=0

    if len(password)<8:
        return False
    
    for i in password:
        if i.isupper():
            uppercase += 1
    if uppercase==0:
        return False
        
    for i in password:
        if i.islower():
            lowercase += 1
    if lowercase==0:
        return False
        
    for i in password:
        if i.isdigit():
            digit+=1
    if digit==0:
        return False
    
    # for i in password:
    #     if i in string.punctuation:
    #         special+=1
    # if special==0:
    #     return False
    return True  




def signup(username, password, email):
    if username=='' or password=='' or email=='':
        raise ValueError
    if is_password_secure(password)==False:
        raise ValueError
    else:
        return True
    """
    Handles the user signup process by validating the provided username, password, and email.

    Instructions for Implementation:
    1. **Input Validation**:
        - Ensure that all fields (`username`, `password`, `email`) are non-empty strings.
        - If any field is empty, raise a `ValueError`.
        - Validate that the `email` follows the correct format (e.g., using a regular expression for email validation).
        - Ensure the `password` meets minimum security criteria (e.g., at least 8 characters long, contains a mix of uppercase, lowercase, and digits).
        - If the `password` is weak (e.g., a simple password like "123"), raise a `ValueError`.

    2. **Username Uniqueness Check**:
        - Check if the `username` already exists in the user database.
        - If the `username` is already taken, raise a `ValueError`.

    3. **Create New User**:
        - If all validations pass and the username is unique, create a new user with the provided `username`, `password`, and `email`.
        - The `password` should be securely hashed before storing it (if using password hashing).
        - Add the new user to the user database.

    4. **Edge Cases**:
        - Handle cases where any of the input fields are empty.
        - Handle invalid email formats using proper regular expression checks.
        - Handle cases where the `username` is already taken.
        - Ensure that weak passwords (e.g., less than 8 characters or easily guessable) are rejected.

    Parameters:
    - `username` (str): The desired username for the new user.
    - `password` (str): The password chosen by the user.
    - `email` (str): The email address provided by the user.

    Returns:
    - bool: `True` if the signup is successful, otherwise raises a `ValueError` for invalid input.
    """
