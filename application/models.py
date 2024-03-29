# User class with UserMixin kwarg invoked.
class User(UserMixin):
    def __init__(self, user_id, usuario, password):
        self.id = user_id
        self.usuario = usuario
        self.password = password
        self.authenticated = False
    def is_active(self):
        return self.is_active()
    def is_anonymous(self):
        return False
    def is_authenticated(self):
        return self.authenticated
    def is_active(self):
        return True
    def get_id(self):
        return self.id
