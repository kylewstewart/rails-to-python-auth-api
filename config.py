database = {
    'host': 'localhost',
    'port': 27017,
    'db_name': 'dtx-flask-exch-server',
}

serailize = {
    'users': {
        'index': (
            'id',
            'username'
        ),
        'create': (
            'id',
            'username'
        ),
        'show': (
            'id',
            'username'
        )
    }
}
