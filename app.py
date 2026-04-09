import os

def login(user, password):
    if password == os.getenv("ADMIN_PASS"):
        return True
    return False
