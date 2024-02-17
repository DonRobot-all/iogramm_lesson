from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота, полученный у @BotFather
API_TOKEN: str = ''

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()


@dp.message(Command(commands=["example"]))
async def process_example_command(message: Message):
    await message.answer('Я сработаю при запросе /example')


@dp.message(Command(commands=['two_example']))
async def process_two_example_command(message: Message):
    await message.answer('Я сработаю при запросе /two_example')


@dp.message(Command(commands=['opa']))
async def process_opa_command(message: Message):
    await message.answer('opa работает')


# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" и "/help"
@dp.message()
async def send_echo(message: Message):
    print(message)
    await message.reply(text='сообщение пришло!')


if __name__ == '__main__':
    dp.run_polling(bot)