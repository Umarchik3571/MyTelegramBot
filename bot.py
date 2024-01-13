import logging

from aiogram import Bot,Dispatcher, executor, types
from bot_keyboards import *
from database import *
from config import *

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN, parse_mode="html")
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user_id = message.from_user.id
    await create_user(user_id,message.from_user.username)
    check = None
    for channel in CHANNELS:
        check = await bot.get_chat_member(channel['id'], user_id)
        if check.status == 'left':
            break
        
    if check.status == 'left':
        btn = await chennel_btn(CHANNELS)
        await message.answer("kanallar", reply_markup=btn)
    else:
        await message.answer("Salom")

@dp.message_handler(content_types=["video"])
async def addFilm_handler(message: types.Message):
    caption = message.caption.split("\n")
    film_code = int(caption[0])
    film_name = caption[1]
    film_id = message.video.file_id
    await create_film(film_code, film_name, film_id)
    await message.answer("<b>Фильм добавлен!</b>")


@dp.message_handler(content_types=['text'])
async def get_film_handler(message: types.Message):
    text = message.text

    if text.isdigit():
        film_into = await get_film(text)
        await message.answer_video(film_into[2],caption=f"KOD:{film_into[0]}\nNOMI:{film_into[1]}")
    else:
        await message.answer("eogdguiggh!")


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=create_tables)