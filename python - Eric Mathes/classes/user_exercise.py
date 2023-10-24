class User:
    """A simple user class"""

    def __init__(self, first_name, last_name, *miscellaneous):
        """Initializing attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.miscellaneous = miscellaneous
        self.login_attempts = 0
    
    def describe_user(self):
        print(f"User Profile info: {self.first_name} , {self.last_name}, {self.miscellaneous}")

    def greet_user(self):
        print(f"Hello, {self.first_name}")

    def increment_login(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts  = 0

user1 = User("Nat","Cob","Software Engineer", "Machine Learning/AI Engineer", "Copywriter", "Full Stack Developer", "Backend Engineer")
user1.describe_user()
user1.greet_user()
user1.increment_login()
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)