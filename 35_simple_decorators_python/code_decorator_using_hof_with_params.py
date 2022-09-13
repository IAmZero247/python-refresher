



def make_secure(func):
    def secure_function(panel):
        if user["access_level"] == "admin":
            return func(panel)
        else:
            return f"No admin permissions for {user['username']}."

    return secure_function

def get_password(panel):
    if panel == "admin":
        return "1234"
    elif panel == "billing":
        return "super_secure_password"


get_password_with_param = make_secure(get_password)


user = {"username": "jose", "access_level": "guest"}

print(get_password_with_param("admin"))
print(get_password_with_param("billing"))

user = {"username": "bob", "access_level": "admin"}

print(get_password_with_param("admin"))
print(get_password_with_param("billing"))

