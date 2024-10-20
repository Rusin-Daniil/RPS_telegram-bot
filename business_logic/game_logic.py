from random import choice
from entities_classes.classes import Element
from entities_classes.classes import rock, paper, scissors
from aiogram.types import Message


def process_game(message: Message) -> str:

    user_choice: Element

    for i in (scissors, rock, paper):
        if message.text == i.name:
            user_choice = i

    bot_choice = choice(['Камень', "Ножницы", "Бумага"])

    if user_choice.name == bot_choice:
        return f'Ничья. Я выбрал {bot_choice}'
    else:
        if user_choice.beating == bot_choice:
            return f'Вы ПОБЕДИЛИ! Я выбрал {bot_choice}'
        elif not user_choice.beating == bot_choice:
            return f'Вы ПРОИГРАЛИ. Я выбрал {bot_choice}'
