# Adding a route and verb will restrict access to users with authorized tokens.

authorize = {
    'auth': (
        'post'
    ),
    'user': (
        'get',
        'put',
        'patch',
        'delete'
    )
}
