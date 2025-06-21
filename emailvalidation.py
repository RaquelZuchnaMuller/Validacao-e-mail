def validate_email(email):
    # Rule 1: Must contain exactly one "@"
    if email.count("@") != 1:
        return "Invalid email"

    # Rule 2: Cannot start or end with "@"
    if email.startswith("@") or email.endswith("@"):
        return "Invalid email"

    # Rule 3: Cannot contain spaces
    if " " in email:
        return "Invalid email"

    # Rule 4: Must contain a domain like gmail.com or outlook.com
    user, domain = email.split("@")
    if "." not in domain:
        return "Invalid email"

    return "Valid email"



