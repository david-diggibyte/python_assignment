import re
def validating_emails(emails):
    pattern = r'^[a-zA-Z0-9_.-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'
    valid_emails = sorted(filter(lambda x: re.match(pattern, x), emails))
    return valid_emails
