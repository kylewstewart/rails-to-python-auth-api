serailizer = {
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
        ),
        'update': (
            'id',
            'username'
        )
    },
    'auth': {
        'index': (
            'id',
            'username',
        ),
        'create': (
            'id',
            'username',
            'jwt'
        )
    }
}
