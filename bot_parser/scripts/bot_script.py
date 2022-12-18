from aiogram import executor
from bot_parser import bot
from bot_parser.handlers.main_handler import register_main_handlers


def main():
    register_main_handlers(bot.dp)
    executor.start_polling(bot.dp, skip_updates=True)


if __name__ == '__main__':
    main()
