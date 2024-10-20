from aiogram.types import Message
from aiogram import Router
from lexicon.lexicon import LEXICON_RU

# Инициализируем роутер уровня модуля
router = Router()


# этот хендлер будет срабатывать на любые ваши сообщения,
# кроме команд "/start" и "/help"
@router.message()
async def send_echo(message: Message):
    await message.reply(text=LEXICON_RU['no_echo'])
