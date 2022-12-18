from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class Condition(StatesGroup):
    category = State()
    brand = State()
    model = State()


async def get_category(message: types.Message):
    await message.reply('Select category')
    await Condition.category.set()




def register_handlers(dp: Dispatcher):
    pass