import re

def validate_pin(pin):  # week 1
    match = re.search("^[0-9]{4}\Z|^[0-9]{6}\Z", pin)  # \Z ensures that there is no new line at the end of the pin
    if match:
        return True
    else:
        return False

print(validate_pin("457923"))  # print true if pin is 4 or 6 characters long