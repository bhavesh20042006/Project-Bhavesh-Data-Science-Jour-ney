class User:
    pass
user_1 = User()   #its the basic step of adding attributes
user_1.id = "001"
user_1.username = "bhavesh"
print(user_1.id)


user_2 = User()
user_2.id = "002"
user_2.username = "john"
print(user_2.id)


class User:   #class first letter should be capital(pascal case)
    def __init__(self, id, username):  #constructor ,self is the instance
        self.id = id
        self.username = username
        self.followers = 0  #default attribute

user_1 = User("001", "bhavesh")
print(user_1.id)
print(user_1.username)
print(user_1.followers)


user_2 = User("002", "john")
print(user_2.id)
print(user_2.username)


