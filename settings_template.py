TINYRSS = {
    # URL to TinyRSS instance
    'url': 'http://<host>/ttrss/api/',

    # USER registered in TinyRSS
    'user': 'admin',

    # PASSWORD for TinyRSS user
    'password': 'password',

    # FEEDS the bot should listen to
    'feeds': [
        {'name': 'Mixed Martial Arts', 'id': '-1234'},
        {'name': 'Football', 'id': '-1337'},
    ],
}

TELEGRAM = {
    # TOKEN for chat bot
    'token': '123456789:ABCDEFGHIJKLMNOPQRSTUVWYZ1234567890',
    'chat_id': '133707331',
}

CHAT = {
    # [optional] add users listening in chat for specific actions
    'users': [
        {'name': 'User1', 'id': '<user_id>', 'email': 'not@existing.com'},
    ],

    # [optional] add inline buttons
    'buttons': [
        {'name': 'Cool!', 'data': 'cool'},
        {'name': 'Lame!', 'data': 'lame'},
    ]
}