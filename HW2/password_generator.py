import string
import random


def generate_password():
    s1 = list(string.ascii_lowercase)
    s2 = list(string.ascii_uppercase)
    s3 = list(string.digits)
    s4 = list(string.punctuation)
    chars = s1 + s2 + s3 + s4

    password_length = random.randint(10, 16)
    password = [
        random.choice(s1),
        random.choice(s2),
        random.choice(s3),
        random.choice(s4),
    ] + [random.choice(chars) for _ in range(password_length)]

    random.shuffle(password)
    return ''.join(password)




