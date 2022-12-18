from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_category_button() -> ReplyKeyboardMarkup:
    tv = KeyboardButton('TV')
    smartphones = KeyboardButton('Smartphones')
    laptops = KeyboardButton('Laptops')
    client = ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=True,
    )
    client.add(tv).add(smartphones).add(laptops)
    return client
