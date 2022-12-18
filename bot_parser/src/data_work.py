def get_category(user_request: dict) -> str:
    return user_request.get('category', None)


def get_brand(user_request: dict) -> str:
    return user_request.get('brand', None)


def get_model(user_request: dict) -> str:
    return user_request.get('model', None)


def check_input_data(user_request: dict) -> str:
    if get_category(user_request) is None:
        return 'Please enter correct category.'
    elif get_brand(user_request) is None:
        return 'Please enter correct brand.'
    elif get_model(user_request) is None:
        return 'Please enter correct model.'
    else:
        return 'Please waiting...'
