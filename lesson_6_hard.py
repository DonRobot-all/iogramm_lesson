keyboard: list[list[KeyboardButton]] = [[KeyboardButton(
    text=f'Кнопка {j * 3 + i}') for i in range(1, 4)] for j in range(3)]

# Создаем объект клавиатуры, добавляя в него кнопки
my_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
    keyboard=keyboard,
    resize_keyboard=True)