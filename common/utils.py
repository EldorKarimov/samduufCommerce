import re

def phone_validator(value):
    regex = re.compile('^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$')
    value = str(value)
    if re.fullmatch(regex, value):
        return "valid"
    else:
        return "invalid"