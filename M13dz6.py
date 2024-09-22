from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Key_TBot import api_bot

api = api_bot
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


def kb_menu():
    kb_list = [
        [KeyboardButton(text='Посчитать калории')],
        [KeyboardButton(text='Хелп по боту')]
    ]
    kb = ReplyKeyboardMarkup(keyboard=kb_list, resize_keyboard=True)
    return kb

def inline_menu():
    kb_list = [
        [
            InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='clrs'),
            InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
        ]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=kb_list)
    return kb





@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb_menu())



@dp.message_handler(text = 'Посчитать калории')
async def menu_main(message: types.Message):
    await message.answer('Выберите опцию:', reply_markup=inline_menu())


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5',
                              reply_markup=inline_menu())




@dp.callback_query_handler(text='clrs')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()

@dp.message_handler(state = UserState.age)
async def set_growth(message, state):
    await state.update_data(first=message.text)
    data = await state.get_data()
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state = UserState.growth)
async def set_weight(message, state):
    await state.update_data(second=message.text)
    await state.get_data()
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state = UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    await state.get_data()
    clrs = float(data['weight']) * 10 + float(data['growth']) * 6.25 + float(data['age']) * 5 + 5
    await message.answer(f'Ваша норма калорий: {clrs}')
    await state.finish()


    await message.answer(f'Ваша норма калорий: {clrs}')
    await state.finish()

@dp.message_handler(text='Хелп по боту')
async def info(message: types.Message):
    await message.answer('Информация о боте!')




if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
