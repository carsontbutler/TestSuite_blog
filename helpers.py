import random
import string

def generate_invalid_username():
    invalid_chars = ['#','$','%','^','*', '(', ')']
    invalid_char = random.choice(invalid_chars)
    length = random.randint(1,100)
    random_string = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=length))
    res = f'{random_string}{invalid_char}'
    return res

def generate_long_username():
    MAX_LENGTH = 150
    res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=MAX_LENGTH+1))
    return res