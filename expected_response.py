UNAUTHORIZED_RESPONSE = {
    'message': 'You should be authorised',
    'success': False
}

CREATE_NEW_USER_RESPONSE = {
    'success': False,
    'message': 'User already exists'
}

FAIL_CREATE_NEW_USER_RESPONSE = {
    'message': 'Email, password and name are required fields',
    'success': False
}

FAIL_CREATE_ORDER_NON_INGREDIENTS = {
    'success': False,
    'message': "Ingredient ids must be provided"
}


def get_success_user_response(name):
    return {
        'success': True,
        'user': {
            'email': 'oleqrezni4enko@yandex.ru',
            'name': name
        }
    }
