from models.app_model import AppModel


class User(AppModel):

    collection = 'users'

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save(self):
        id = self.get_id_number()
        db = self.get_db
