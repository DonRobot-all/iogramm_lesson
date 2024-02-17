from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
API_TOKEN: str = ''

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()

# Создаем объекты кнопок
button_1: KeyboardButton = KeyboardButton(text='Положительный')
button_2: KeyboardButton = KeyboardButton(text='Крайне положительный')


# Создаем объект клавиатуры, добавляя в него кнопки
keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                    keyboard=[[button_1, button_2]])


# Этот хэндлер будет срабатывать на команду "/start"
# и отправлять в чат клавиатуру
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Какой отзыв Вы оставите о лагере?',
                         reply_markup=keyboard,)


# Этот хэндлер будет срабатывать на ответ "Положительный" и удалять клавиатуру
@dp.message(F.text.lower().in_(['положительный']))
async def process_dog_answer(message: Message):
    await message.answer(text='Спасибо!',
                         reply_markup=ReplyKeyboardRemove())


# Этот хэндлер будет срабатывать на ответ "крайне положительный" и удалять клавиатуру
@dp.message(F.text.lower().in_(['крайне положительный']))
async def process_cucumber_answer(message: Message):
    await message.answer(text='Большое спасибо!',
                         reply_markup=ReplyKeyboardRemove())


if __name__ == '__main__':
    dp.run_polling(bot)
