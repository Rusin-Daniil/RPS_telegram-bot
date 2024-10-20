from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


kb_builder = ReplyKeyboardBuilder()

start_buttons: list[KeyboardButton] = [
    KeyboardButton(text='Давай!'),
    KeyboardButton(text='Не хочу'),
    KeyboardButton(text='Мой результат')
    ]

kb_builder.row(*start_buttons, width=2)


kb_builder2 = ReplyKeyboardBuilder()

game_buttons: list[KeyboardButton] = [
    KeyboardButton(text=f'{i}') for i in ('Камень', "Ножницы", "Бумага")
    ]

kb_builder2.row(*game_buttons)
