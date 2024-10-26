from project.library import Library
from project.user import User


class Registration:

    @staticmethod
    def add_user(user: User, library: Library) -> str or None:
        if user not in library.user_records:
            library.user_records.append(user)
        else:
            return f"User with id = {user.user_id} already registered in the library!"

    @staticmethod
    def remove_user(user: User, library: Library) -> str or None:
        if user not in library.user_records:
            return "We could not find such user to remove!"
        library.user_records.remove(user)

    @staticmethod
    def change_username(user_id: int, new_username: str, library: Library) -> str:
        try:
            user = [x for x in library.user_records if x.user_id == user_id][0]
            if user.username != new_username:
                user.username = new_username
                return f"Username successfully changed to: {user.username} for user id: {user.user_id}"

            return f"Please check again the provided username - it should be different than the username used so far!"

        except IndexError:
            return f"There is no user with id = {user_id}!"


