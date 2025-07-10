import string

def strong_password(password):
    if len(password)<8:
        return False
    elif not any(ch.isupper() for ch in password):
        return False
    elif not any(ch.islower() for ch in password):
        return False
    elif not any(ch.isdigit() for ch in password):
        return False
    elif not any(ch in string.punctuation for ch in password):
        return False
    else:
        return True
    
while True:
    password=input('Enter Password\n')
    if strong_password(password):
        print('Password is strong')
        break
    else:
        print('Weak Password!!')