from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command


API_TOKEN: str = 'TOKEN'
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()


@dp.message(Command(commands=['start']))
async def process_start_command(message: Message):
    await message.answer('Привет!\nЯ - Эхо-бот!\nНапиши мне что-нибудь')


@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer('Отправь мне сообщение и я отвечу тебе им же!')


@dp.message()
async def send_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply("Данный тип сообщений не поддерживается")


if __name__ == '__main__':
    dp.run_polling(bot)
