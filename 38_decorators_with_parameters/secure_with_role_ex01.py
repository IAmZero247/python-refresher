import functools


jack = {"username": "jack", "role": "admin" , "password": "iamadminpassword"}
rose = {"username": "rose", "role": "user" , "password": "iamuserpassword"}

def secure_with_role(role):

    def decorator(func):
        @functools.wraps(func)
        def secure(*args, **kwargs):
            #print("<--inside secure--")
            #print(args)
            #print(kwargs)
            #print("--inside secure-->")
            u = args[0]
            if u['role'] == role:
                return func(u['password'])
            else:
                #raise Exception("Invalid Role")
                return "Invalid"

        return secure
    return decorator

@secure_with_role('admin')
def get_admin_password(password):
    return password
print(get_admin_password(jack))
print(get_admin_password(rose))

@secure_with_role('user')
def get_user_password(password):
    return password

print(get_user_password(jack))
print(get_user_password(rose))