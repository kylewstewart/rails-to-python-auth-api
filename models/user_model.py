from models.app_model import AppModel
from IPython import embed


class User(AppModel):

    COLLECTION = 'users'

    def __init__(
        self,
        username,
        password,
        id=None
    ):
        self.username = username
        self.password = password
        self.id = id
