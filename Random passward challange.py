import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4 for better security.")
        return ""

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits

    password_chars = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
    ]


    all_chars = lower + upper + digits
    password_chars += random.choices(all_chars, k=length - 3)

    random.shuffle(password_chars)

    password = ''.join(password_chars)
    return password

password_length = 10
password = generate_password(password_length)
print("Random Password:", password)
