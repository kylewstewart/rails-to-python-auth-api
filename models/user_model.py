from models.app_model import AppModel
from IPython import embed


class User(AppModel):

    COLLECTION = 'users'

    def __init__(self, id, username, password, **kwargs):
        self.id = id
        self.username = username
        self.password = password
