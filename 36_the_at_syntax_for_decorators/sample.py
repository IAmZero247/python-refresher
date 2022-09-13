
import functools

def make_secure_admin(func):
    @functools.wraps(func)
    def secure_admin():
        if user["access_level"] == 'admin':
            return func(user["password"])
        else:
            raise Exception("Invalid Privilage")

    return secure_admin

@make_secure_admin
def get_admin_password(x):
    return x

user = {"username": "jose", "access_level": "admin" , "password": "iamsamplepassword"}

print(get_admin_password.__name__)
print(get_admin_password())