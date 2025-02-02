import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

from config import TOKEN

# Initialize dispatcher
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message):
    """
    Handle the /start command
    """
    await message.answer(
        f"Привіт, {html.bold(message.from_user.full_name)}👋\n"
        f"Твій айді: {html.code(message.from_user.id)}"
    )


async def main() -> None:
    """
    Main function to run the bot
    """
    bot = Bot(
        token=TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    # Configure logging
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    
    # Run the bot
    asyncio.run(main())
