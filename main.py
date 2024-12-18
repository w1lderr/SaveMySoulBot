import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from config import TOKEN

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message):
    await message.answer(f"Привіт, {html.bold(message.from_user.full_name)}👋\nТвій айді: {html.code(message.from_user.id)}")

async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())