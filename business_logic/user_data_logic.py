from aiogram.types import Message
import re
import json


def add_new_user(datafile: dict, message: Message,):
    if str(message.from_user.id) not in datafile:
        datafile[str(message.from_user.id)] = [0, 0, 0]


def update_user_data(datafile: dict, message: Message, game_result: str):

    add_new_user(datafile, message)

    templates = [r'ПОБЕДИЛИ', r'ПРОИГРАЛИ', r'Ничья']

    result = 3

    for i in templates:
        match = re.search(i, game_result)
        if match:
            if match[0] == 'ПОБЕДИЛИ':
                result = 1
            elif match[0] == 'ПРОИГРАЛИ':
                result = 2
            elif match[0] == 'Ничья':
                pass

    if str(message.from_user.id) in datafile:
        if result == 1:
            datafile[str(message.from_user.id)][0] += 1
            datafile[str(message.from_user.id)][2] += 1
        elif result == 2:
            datafile[str(message.from_user.id)][1] += 1
            datafile[str(message.from_user.id)][2] += 1
        elif result == 3:
            datafile[str(message.from_user.id)][2] += 1

    f = open('E:/projects/echo_bot/database/user_data_txt', 'w')
    f.write(json.dumps(datafile))
    f.close()
