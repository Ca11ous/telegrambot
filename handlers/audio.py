from aiogram import types
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from pytube import exceptions
import os


from config import dp, bot
from states.dowload import Dowload
from functions.audio import dowload_video



@dp.message_handler(commands=['audio'])
async def audio(message : types.Message):
    await message.answer("Введите ссылку на видео с YouTube")
    await Dowload.dowload.set()

@dp.message_handler(state=Dowload.dowload)
async def dowload(message: types.Message, state: FSMContext):
    try:
        title = dowload_video(message.text)
        audio = open(f'audio/{title}', 'rb')
        await bot.send_audio(message.chat.id, audio)
        await message.answer(text="Вот твое аудио, наслаждайся")
        os.remove(f'audio/{title}')
        await state.finish()
    except exceptions.LiveStreamError:
        await message.answer(text="Я еще не умею извлекать аудио с трансляции")
    except exceptions.RegexMatchError:
        await message.answer(text="Я умею извлекать аудио только из видео на YouTube")
    except:
        await message.answer(text="Я еще не умею извлекать аудио из таких долгих видео")
    await state.finish()