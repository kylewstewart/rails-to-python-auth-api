from models.app_model import AppModel
from IPython import embed


class User(AppModel):

    COLLECTION = 'users'

    def __init__(self, id, **kwargs):
        self.id = id
        self.username = kwargs.pop('username', None)
        self.password = kwargs.pop('password', None)
