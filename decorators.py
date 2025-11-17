
def require_login(func):
    def wrapper(user):
        if(user.get("isLoggedIn") == False):
            return "Access Denied"
        return func(user)
    return wrapper           


@require_login
def access_dashboard(user):
    return f"Welcome {user.get("name")}. Access to the dashboard."

user1 = {"name":"Dheeraj","isLoggedIn":True}
user2 = {"name":"Guest","isLoggedIn":False}


print(access_dashboard(user1))
print(access_dashboard(user2))