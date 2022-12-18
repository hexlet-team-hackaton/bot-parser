def get_category(user_request: dict) -> str:
    return user_request.get('category', None)


def get_brand(user_request: dict) -> str:
    return user_request.get('brand', None)


def get_model(user_request: dict) -> str:
    return user_request.get('model', None)


def check_input_data(user_request: dict):
    pass
