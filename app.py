# app.py
def login(user, password):
    if password == "admin123":  # insecure
        return True
    return False