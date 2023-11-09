import random
import string
def generate_password(length,use_uppercase,use_lowercase,use_digits,use_special_char):
    char=''
    if use_uppercase:
        char+=string.ascii_uppercase
    if use_lowercase:
        char+=string.ascii_lowercase
    if use_special_char:
        char+=string.punctuation
    if use_digits:
        char+=string.digits

    password=''.join(random.choice(char)for _ in range (length))
    return password

def main():
    print("password generator")
    length=int(input("Enter the password length:"))

    use_uppercase=input("include uppercaseletters(y/n):").lower()=='y'
    use_lowercase=input("include lowercaseletters(y/n):").lower()=='y'
    use_digits=input("include digits(y/n):").lower()=='y'
    use_spacial_char=input("include spacial_char(y/n):").lower()=='y'

    password=generate_password(length,use_uppercase,use_lowercase,use_digits,use_spacial_char)

    print("password generates:",password)

if __name__=='__main__':
    main()
    