from aiogram import Bot, Dispatcher, types
import asyncio
import logging
import sys
from aiogram.filters import CommandStart, Command
from handlers import commands

TOKEN = '6550885808:AAGofxj2z2E-cQ4n9F5ZOCzna9SWv12qb5U'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

dp.message.register(commands.start, CommandStart())
dp.message.register(commands.send_photo, Command('photo'))
dp.message.register(commands.quiz, Command('quiz'))
dp.message.register(commands.echo)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

