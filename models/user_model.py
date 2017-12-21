from models.app_model import AppModel


class User(AppModel):

    COLLECTION = 'users'

    def __init__(self, id, username, password_digest, **kwargs):
        self.id = id
        self.username = username
        self.password_digest = password_digest
