from telebot import TeleBot
from telebot.types import Message, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from decouple import config


token = config('TOKEN')

bot = TeleBot(token)


@bot.message_handler(['start', 'lesson', 'jun'])
def start_message(message: Message):
    bot.send_message(message.chat.id, f'Салам, {message.chat.username}')


@bot.message_handler(func=lambda message: message.text == 'Кнопки')
def get_buttons(message: Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton('Кнопка 1')
    button2 = KeyboardButton('Кнопка 2')
    keyboard.add(button1, button2)

    bot.send_message(message.chat.id, "На кнопку по-братски нажми", reply_markup=keyboard)


@bot.message_handler(func=lambda m: m.text == 'Кнопка 1')
def inline_buttons(message: Message):
    keyboard = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton('Салам', callback_data='call1')
    button2 = InlineKeyboardButton('Общий', callback_data='call2')
    keyboard.add(button1, button2)

    bot.reply_to(message, 'Лови кнопки, брат', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda c: True)
def handle_callback_data(callback: CallbackQuery):
    if callback.data == 'call1':
        bot.send_sticker(callback.message.chat.id, sticker='CAACAgIAAxkBAAEJ91Nk05bKzAZ4O4Cir-QHM_ciLFmv6wACvAwAAuZy-Ul3XvZh_lwl_TAE')
    else:
        bot.send_sticker(callback.message.chat.id, sticker='CAACAgIAAxkBAAEJ935k05dauhi6WU4hu7C9WN1lsx9cvgACQgADEmXGPE761JzgbbSgMAQ')




bot.infinity_polling()