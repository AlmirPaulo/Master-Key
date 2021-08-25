import random

def step1_letters():
    abcs = 'qwertyuiopasdfghjklzxcvbnmäåéþüúíóöáßðœøæñµ'
    a = random.choice(abcs)
    b = random.choice(abcs)
    c = random.choice(abcs)
    abc = a+b+c
    return abc
    

def step2_uppercase():
    return step1_letters().upper()

def step3_numbers():
    numbers = random.randint(100,999)
    return numbers

def step4_symbols():
    symbols = '!`~",;(){[]}<>.?/\|^@#$&%*-_+=×:¨'
    s1 = random.choice(symbols)
    s2 = random.choice(symbols)
    s3 = random.choice(symbols)
    passwd_symbols = s1+s2+s3

    return passwd_symbols 

def generate_password():
    letters = step1_letters()
    uppercase = step2_uppercase()
    numbers = str(step3_numbers())
    symbols = step4_symbols()

    final_password = letters+uppercase+numbers+symbols
    return ''.join(random.sample(final_password, len(final_password)))
    

