UNAUTHORIZED_RESPONSE = {
    'message': 'You should be authorised',
    'success': False
}


def get_success_user_response(name):
    return {
        'success': True,
        'user': {
            'email': 'oleqrezni4enko@yandex.ru',
            'name': name
        }
    }
