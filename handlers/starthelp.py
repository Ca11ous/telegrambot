from aiogram import types
from config import dp


@dp.message_handler(commands=['start','help'])
async def starthelp(message : types.Message):
    await message.answer("Привет, меня зовут Саша, я буду помогать тебе\n\n<b>Список команд:</b>\n/start - начать общение с ботом\n/help - узнать список всех команд\n\n<b>Я могу:\n</b>/audio - извлечь аудио из видео YouTube\n/translate - перевести ваш текст")