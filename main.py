import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from db import Database

db = Database("users.db")

TOKEN = ""
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    db.add_user(message.from_user.id, message.from_user.full_name)
    await message.answer("Salom !")


async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
