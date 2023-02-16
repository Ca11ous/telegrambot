from aiogram import types
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext


from config import dp, bot
from states.translate import Translate
from functions.translate import translate_text

@dp.message_handler(commands=['translate'])
async def translat(message : types.Message):
    await message.answer("Введите текст для перевода на русский язык")
    await Translate.translate.set()

@dp.message_handler(state=Translate.translate)
async def tran(message : types.Message, state: FSMContext):
    result = translate_text(message.text)
    await message.answer(result)    
    await state.finish()    