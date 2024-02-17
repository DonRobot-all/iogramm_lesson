import random

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command

BOT_TOKEN: str = 'токен'

bot: Bot = Bot(BOT_TOKEN)
dp: Dispatcher = Dispatcher()

ATTEMPTS = 5

user = {'in_game': False,
        'secret_number': None,
        'attempts': None,
        'total_games': 0,
        'wins': 0}


@dp.message(Command(commands=['start']))
async def progress_command_start(message):
    await message.answer('Напиши да, если хочешь играть')


@dp.message(F.text.lower().in_(['да']))
async def progress_command_yes(message):
    if user['in_game'] == True:
        await message.answer('Мы уже играем!')
    else:
        await message.answer('Начинаем играть')
        user['in_game'] = True
        user['secret_number'] = random.randint(1, 100)


@dp.message(lambda x: x.text and x.text.isdigit() and 1 <= int(x.text) <= 100)
async def process_numbers_answer(message):
    ...


if __name__ == '__main__':
    dp.run_polling(bot)