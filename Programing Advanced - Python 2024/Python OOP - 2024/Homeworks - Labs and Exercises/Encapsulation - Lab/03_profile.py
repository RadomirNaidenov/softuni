class Profile:

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        if not 5 <= len(username) <= 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = username

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        is_valid_length = True if len(password) == 8 else False
        is_upper_case = [char for char in password if char.isupper()]
        is_have_digit = [char for char in password if char.isdigit()]

        if not is_valid_length or not is_upper_case or not is_have_digit:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        self.__password = password

    def __str__(self) -> str:
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.username)}'



