import requests
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command

# Замените 'YOUR_TELEGRAM_BOT_TOKEN' на ваш токен Telegram бота
bot = Bot(token="")
dp: Dispatcher = Dispatcher()

# Функция для обращения к API NASA и получения данных об астрономическом изображении дня
def get_nasa_apod():
    api_key = 'bivbVc3kBmu1HX6H4Csde0Qp2RDTHbjSuvGjibPN'  # Замените YOUR_NASA_API_KEY на ваш ключ API NASA
    url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        title = data['title']
        explanation = data['explanation']
        image_url = data['url']
        return f'{title}\n\n{explanation}\n\n{image_url}'
    else:
        return 'Не удалось получить данные от NASA API.'

# Обработчик команды /start
@dp.message(Command(commands=['start']))
async def start_command_handler(message: Message):
    await message.answer("Привет! Я бот, который поможет тебе узнать о космосе. Введи команду /nasa, чтобы получить астрономическое изображение дня.")

# Обработчик команды /nasa
@dp.message(Command(commands=['nasa']))
async def nasa_command_handler(message: Message):
    nasa_info = get_nasa_apod()
    await message.answer(nasa_info)

# Обработчик неизвестных команд
@dp.message()
async def unknown_command_handler(message: Message):
    await message.answer("Извините, я не понимаю эту команду. Введите /nasa, чтобы получить астрономическое изображение дня.")

if __name__ == '__main__':
    dp.run_polling(bot)
