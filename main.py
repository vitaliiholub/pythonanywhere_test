from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('/help')
b2 = KeyboardButton('/description')
b3 = KeyboardButton('/photo')

kb.add(b1).insert(b2).add(b3)

HELP_COMMAND = """
<b>/help</> - <em>список команд</em>
<b>/start</> - <em>запуск бота</em>
<b>/description</> - <em>описание бота</em>
<b>/photo</> - <em>отправка фото</em>
"""


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(message.from_user.id,
                           text=HELP_COMMAND,
                           parse_mode='HTML',)
    await message.delete()


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id,
                           text='Добро пожаловать в бота',
                           parse_mode='HTML',
                           reply_markup=kb)
    await message.delete()


@dp.message_handler(commands=['description'])
async def description_command(message: types.Message):
    await bot.send_message(message.from_user.id,
                           text="Бот умеет отправлять фотографии",
                           parse_mode='HTML')
    await message.delete()


@dp.message_handler(commands=['photo'])
async def photo_command(message: types.Message):
    await bot.send_photo(message.from_user.id,
                         photo='https://i.guim.co.uk/img/media/26392d05302e02f7bf4eb143bb84c8097d09144b/446_167_3683_2210/master/3683.jpg?width=1200&quality=85&auto=format&fit=max&s=a52bbe202f57ac0f5ff7f47166906403')
    await message.delete()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
