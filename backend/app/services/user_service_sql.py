class SQLUserService(UserService):
    def __init__(self, session):
        self.session = session

    def create_user(self, user: User):
        raise NotImplementedError("SQL backend not implemented yet")
