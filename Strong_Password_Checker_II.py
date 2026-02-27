def isStrongPassword(password: str) -> bool:
    # condition 1: length
    if len(password) < 8:
        return False

    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False
    special_chars = "!@#$%^&*()-+"

    # loop through characters
    for i in range(len(password)):
        ch = password[i]

        if ch.islower():
            has_lower = True
        if ch.isupper():
            has_upper = True
        if ch.isdigit():
            has_digit = True
        if ch in special_chars:
            has_special = True

        if i > 0 and password[i] == password[i-1]:
            return False

    return has_lower and has_upper and has_digit and has_special

print(isStrongPassword("IloveLe3tcode!"))  
print(isStrongPassword("Me+You--IsMyDream"))
print(isStrongPassword("1aB!"))          

