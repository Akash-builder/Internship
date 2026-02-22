def validate_password(password):
    has_digit = False
    has_upper = False

    # Check each character
    for char in password:
        if char.isdigit():
            has_digit = True
        if char.isupper():
            has_upper = True

    # Final validation
    if len(password) >= 8 and has_digit and has_upper:
        return "Valid Password"
    else:
        return "Invalid Password"

password = input("Enter the Password : ")

result = validate_password(password)
print(result)
