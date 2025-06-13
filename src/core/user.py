from uuid import UUID


def auth_user(username: str, pswd: str) -> UUID | None:
    """authenticate user and get its id"""
    raise NotImplementedError()


def user_role(user: UUID) -> str:
    """get user role by user id"""
    raise NotImplementedError()
