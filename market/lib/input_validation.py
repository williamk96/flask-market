import re

email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'


def email_is_valid(email):
    validity = False
	
    if(re.fullmatch(email_regex, email)):
        validity = True
    
    return validity