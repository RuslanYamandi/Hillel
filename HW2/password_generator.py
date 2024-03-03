import string
import random


def generate_password():
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    password_length = random.randint(10, 16)

    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation),
    ] + random.choices(chars, k=password_length)

    random.shuffle(password)
    return ''.join(password)




