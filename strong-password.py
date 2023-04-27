
import string
import secrets

def generate_password(length=12):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password

if __name__ == '__main__':
    password = generate_password()
    print(password)
