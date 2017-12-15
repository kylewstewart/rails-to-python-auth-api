import datetime


class User():
    structure = {
        'username': basestring,
        'password': basestring,
        'date_creation': datetime.datetime
    }
    required_fields = [
        'username',
        'password'
    ]
    default_values = {
        'date_creation': datetime.datetime.utcnow
    }
    use_dot_notation = True
