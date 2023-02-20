def password_required(func):
    def wrapper(password):
        if password == '1234':
            return bank_credentials()
        elif password == 'cia':
            return instagram_credentials()
        else:
            print('Введен неправильный пароль!!')
    return wrapper


def bank_credentials():
    print("Bank card: 0000-1111-2222-3333-4444")
    print("Bank password: 1234")
    print("amount: 100 000 000$")

def instagram_credentials():
    print("username: snowden")
    print("password: cia")

decor = password_required(instagram_credentials)
print(decor("1234"))