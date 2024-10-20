from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from keyboards.keyboards import kb_builder, kb_builder2
from lexicon.lexicon import LEXICON_RU
from business_logic.game_logic import process_game
from business_logic.user_data_logic import add_new_user, update_user_data
import json
from database.user_data import info

# Инициализируем роутер уровня модуля
router = Router()


# этот хендлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):

    await message.answer(
        text=LEXICON_RU['/start'], reply_markup=kb_builder.as_markup(
                                                resize_keyboard=True))


# этот хендлер срабатывает на команду /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])


@router.message(F.text == 'Давай!')
async def reply_game_keyboard(message: Message):
    await message.answer(text=LEXICON_RU['Davai'],
                         reply_markup=kb_builder2.as_markup(
                                        resize_keyboard=True))


@router.message(F.text == "Не хочу")
async def process_disagreement_command(message: Message):
    await message.answer(text=LEXICON_RU['Ne hochu'])


@router.message(F.text == "Мой результат")
async def process_disagreement_command(message: Message):

    f = open('E:/projects/echo_bot/database/user_data_txt', 'r')
    readed_user_data = f.read()
    user_data_dict = json.loads(readed_user_data)
    f.close()

    if str(message.from_user.id) not in user_data_dict:
        await message.answer(text='Вы еще ни разу не сыграли ;(')
        return
    else:
        await message.answer(text=f'Победы: {user_data_dict[str(message.from_user.id)][0]}\n'
                    f'Поражения: {user_data_dict[str(message.from_user.id)][1]}\n'
                    f'Игр сыграно: {user_data_dict[str(message.from_user.id)][2]}\n')


@router.message(F.text.in_({'Камень', "Ножницы", "Бумага"}))
async def process_choice_command(message: Message):

    result = process_game(message)

    update_user_data(info, message, result)

    await message.answer(text=result + '\n\nЕще разок?',
                         reply_markup=kb_builder.as_markup(
                            resize_keyboard=True, one_time_keyboard=True))
