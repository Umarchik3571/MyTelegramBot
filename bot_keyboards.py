from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def chennel_btn(channels):
    btn = InlineKeyboardMarkup()
    for channel in channels:
        btn.add(
            InlineKeyboardButton(f"{channel['name']}", url=f"{channel['link']}"),
        )
    
    btn.add(
            InlineKeyboardButton(f"A`zo bo`ldim", callback_data="check_subs"),
        )

    return btn