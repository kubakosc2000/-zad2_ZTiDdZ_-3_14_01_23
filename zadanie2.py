import random
import string

def generate_secure_password():
    password = ""
    characters = string.ascii_letters + string.digits + string.punctuation
    password += random.choice(string.ascii_lowercase)
    password += random.choice(string.ascii_uppercase)
    password += random.choice(string.digits)
    password += random.choice(string.punctuation)
    for i in range(4):
        password += random.choice(characters)
    password_list = list(password)
    random.shuffle(password_list)
    password = "".join(password_list)
    return password

print(generate_secure_password())