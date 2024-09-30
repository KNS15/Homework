from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, CallbackQuery
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Key_TBot import api_bot
from Crud_functionsM14dz4 import *


api = api_bot
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


def kb_menu():
    kb_list = [
        [
            KeyboardButton(text='Посчитать калории'),
            KeyboardButton(text='Хелп по боту'),
            KeyboardButton(text='Купить')
        ]
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
    kb = InlineKeyboardMarkup(inline_keyboard=kb_list, resize_keyboard=True)
    return kb

def buying_menu():
    kb_list = [
        [
            InlineKeyboardButton(text='product 1', callback_data='product_buying'),
            InlineKeyboardButton(text='product 2', callback_data='product_buying'),
            InlineKeyboardButton(text='product 3', callback_data='product_buying'),
            InlineKeyboardButton(text='product 4', callback_data='product_buying'),
            InlineKeyboardButton(text='product 5', callback_data='product_buying')
        ]
    ]
    kb_list = InlineKeyboardMarkup(inline_keyboard=kb_list, resize_keyboard=True)
    return kb_list


@dp.message_handler(text = 'Купить')
async def get_buying_list(message):
    all_products = get_all_products()
    for product in all_products:
        with open(f'{product[0]}.jpg', 'rb') as jpg:
            await message.answer_photo(jpg)
            await message.answer(f'{product[1]} | {product[2]} | {product[3]}')
    await message.answer('Выберите продукт для покупки:', reply_markup=buying_menu())

@dp.callback_query_handler(text = 'product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели этот продукт!')
    await call.answer()


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
    await state.update_data(age=int(message.text))
    await state.get_data()
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state = UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=int(message.text))
    await state.get_data()
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state = UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight = int(message.text))
    data = await state.get_data()
    clrs = int(data['weight']) * 10 + int(data['growth']) * 6.25 + int(data['age']) * 5 + 5
    await message.answer(f'Ваша норма калорий: {clrs}')
    await state.finish()

@dp.message_handler(text='Хелп по боту')
async def info(message: types.Message):
    await message.answer('Информация о боте!')

@dp.message_handler()
async def start_speak(message):
    await message.answer('Введите команду "/start" для начала общения')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)