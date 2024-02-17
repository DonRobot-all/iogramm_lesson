import requests
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command

# Замените 'YOUR_TELEGRAM_BOT_TOKEN' на ваш токен Telegram бота
bot = Bot(token="")
dp: Dispatcher = Dispatcher()


# Функция для обращения к API NASA и получения данных запрошенного типа
def get_nasa_data(api_key, data_type):
    url = f'https://api.nasa.gov/planetary/{data_type}?api_key={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

# Обработчик команды /start
@dp.message(Command(commands=['start']))
async def start_command_handler(message: Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton('/nasa'))
    await message.answer("Привет! Я бот, который поможет тебе получить данные с NASA. Введи команду /nasa, чтобы начать.", reply_markup=keyboard)

# Обработчик команды /nasa
@dp.message(Command(commands=['nasa']))
async def nasa_command_handler(message: Message):
    # Здесь укажите свой ключ API NASA
    your_api_key = ''
    await message.answer("Выбери тип данных, которые ты хочешь получить: APOD или EPIC.")

@dp.message()
async def nasa_data_type_handler(message: Message):
    data_type = message.text.lower()
    if data_type not in ['apod', 'epic']:
        await message.answer("Некорректный выбор типа данных. Введите /nasa, чтобы попробовать еще раз.")
        return

    # Здесь укажите свой ключ API NASA
    your_api_key = 'bivbVc3kBmu1HX6H4Csde0Qp2RDTHbjSuvGjibPN'
    nasa_data = get_nasa_data(your_api_key, data_type)
    if nasa_data:
        await message.answer(nasa_data)
    else:
        await message.answer("Не удалось получить данные от NASA API.")


# Запуск бота
if __name__ == '__main__':
    dp.run_polling(bot)