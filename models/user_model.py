import datetime
from IPython import embed
from models.app_model import AppModel


class User(AppModel):

    def __init__(self, **kwargs):
        self.username = kwargs['username']


embed()

# structure = {
#     'username': basestring,
#     'password': basestring,
#     'date_creation': datetime.datetime
# }
# required_fields = [
#     'username',
#     'password'
# ]
# default_values = {
#     'date_creation': datetime.datetime.utcnow
# }
# use_dot_notation = True
