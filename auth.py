def validate_signup(email, password):
    return "@" in email and len(password) >= 8
