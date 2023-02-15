import requests
from bs4 import BeautifulSoup as bs

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command


URL = 'https://anekdotov.net/anekdot/day/'


def parser(url: str) -> list:
    r = requests.get(url)
    soup = bs(r.text, 'html.parser')
    anekdots = soup.findAll(class_='anekdot')
    return [item.text.strip() for item in anekdots]


API_TOKEN: str = ''
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()
a: list = parser(URL)


@dp.message(Command(commands=['start']))
async def process_start_command(message: Message):
    await message.answer(f'Привет!\nТы здесь чтобы словить кринжатинки.\nСегодня есть отборное дерьмо в количестве {len(a)} штук.\n'
                         f'Введи любой текст, чтобы заценить!')


@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(f'Введи любой текст, и я пришлю тебе анекдот.\nСегодня есть еще {len(a)} штук!')


@dp.message()
async def send_echo(message: Message):
    if a:
        await message.answer(a.pop())
    else:
        await message.reply("На сегодня все, возвращайся завтра!")


if __name__ == '__main__':
    dp.run_polling(bot)
