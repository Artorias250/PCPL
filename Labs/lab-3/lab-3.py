import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import F
import asyncio
bot = Bot(token="Токен")
dp = Dispatcher()

keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="QTE", callback_data="button1")],
    [InlineKeyboardButton(text="StyleRank", callback_data="button2")],
    [InlineKeyboardButton(text="Stratagems", callback_data="button3")],
    [InlineKeyboardButton(text="Scripts", callback_data="button4")]
])


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Выберите кнопку:", reply_markup=keyboard)


@dp.callback_query(F.data.in_(["button1", "button2", "button3", "button4"]))
async def button_handler(callback: types.CallbackQuery):
    if callback.data == "button1":
        text = "Quick Time Events (QTE) in the God of War series are not just" \
        "cinematic cutscenes, but a core gameplay element that merges action and narrative" \
        "into a seamless whole."
    elif callback.data == "button2":
        text = "This mechanic encourages the player for an aggressive and spectacular fighting style, rating their performance on a seven-point " \
        "from Dismal to the legendary Smokin' Sick Style!!"
    elif callback.data == "button3":
        text = "Stratagems in the Helldivers series are not merely additional abilities " \
        "but the cornerstone of the entire gameplay and its philosophy."
    elif callback.data == "button4":
        text = "The hacking script system, or cyberdeck, in Cyberpunk 2077 is a " \
        "masterful gamification of the hacker's role in a hyper-technological world."

    await callback.message.edit_text(text, reply_markup=keyboard)
    await callback.answer()


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
