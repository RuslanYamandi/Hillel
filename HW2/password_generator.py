import string
import random


def generate_password():
    s1 = list(string.ascii_lowercase)
    s2 = list(string.ascii_uppercase)
    s3 = list(string.digits)
    s4 = list(string.punctuation)
    chars = s1 + s2 + s3 + s4

    password_length = random.randint(10, 20)
    password = ''
    for i in range(password_length):
        password += random.choice(chars)

    return password




