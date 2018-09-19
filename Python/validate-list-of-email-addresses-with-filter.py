import re

email = re.compile(r"^[\w\-]+?@[a-z0-9]+?\.[a-z]{1,3}$", re.IGNORECASE)

def fun(s):
    return email.match(s)
