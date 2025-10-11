
class User():
    
    def __init__(self, email: str) -> None:
        self._email = email
    
    @property
    def email(self) -> str:
        return self._email
    
    @email.setter
    def email(self, value: str) -> None:
        if "@" in value:
            self._email = value
        else:
            print("Invalid email address")

    @property
    def username(self) -> str:
        return self._email.split("@")[0]



user = User("test@gmail.com")

print(user.username)

user.email = "new.user@domain.com"

print(user.username)


user.email = "invalid-email"

print(user.username)

# user.username = "ARARAT"