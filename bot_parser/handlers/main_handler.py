from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from bot_parser.handlers.keybords import get_category_button
from dotenv import load_dotenv

load_dotenv()


class Condition(StatesGroup):
    category = State()
    brand = State()
    model = State()


async def get_category(message: types.Message):
    kb_client = get_category_button()
    await message.reply('Select category', reply_markup=kb_client)
    await Condition.category.set()


async def get_brand(message: types.Message, state: FSMContext):
    await state.update_data(category=message.text)
    await message.reply('Select brand:')
    await Condition.next()


async def get_model(message: types.Message, state: FSMContext):
    await state.update_data(brand=message.text)
    await message.reply('Select model')
    await Condition.next()


async def get_user_request(message: types.Message, state: FSMContext):
    await state.update_data(model=message.text)
    data = await state.get_data()
    await message.reply(str(data))
    await state.finish()


def register_main_handlers(dp: Dispatcher):
    dp.register_message_handler(
        get_category,
        commands=['start'],
        state=None,
    )
    dp.register_message_handler(
        get_brand,
        state=Condition.category,
    )
    dp.register_message_handler(
        get_model,
        state=Condition.brand,
    )
    dp.register_message_handler(
        get_user_request,
        state=Condition.model,
    )
