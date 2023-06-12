import re
import telebot
from datetime import datetime
import json
from telebot import types
import player 
import admin
import authentication as a
import players
import autoprocessing as auto

bot = telebot.TeleBot("6009093323:AAGvxCnZm7VYWtqFluSNEqzFVMt2QpJp9FQ", parse_mode=None)
admin_id = 861236842

audience = 1000
NAMES = ['entspace', 'skolkovo']

requests = {}

def text_normalize (text):
    words = str(text).lower()

def give_answer (message):
    ans = 'Заявка принята в обработку'
    bot.reply_to(message, ans)

def is_auto(text):
    if re.match(r'перевод|капитал|создать', str(text).lower()) is not None:
        return True
    else: return False

def action_markup():
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 2
    # действия в зависимости от роли
    markup.add(types.InlineKeyboardButton("Перевести деньги", callback_data="перевод"),
                               types.InlineKeyboardButton("Проверить состояние", callback_data="капитал"),
                               types.InlineKeyboardButton("Создать курс для аудитории", callback_data="курс"))
    return markup

def company_markup():
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(types.InlineKeyboardButton("Entspace", callback_data="entspace"),
                               types.InlineKeyboardButton("Сколково", callback_data="skolkovo"),
                               types.InlineKeyboardButton("Лайк Центр", callback_data="like"),
                               types.InlineKeyboardButton("Скиллбокс", callback_data="entspace"),
                               types.InlineKeyboardButton("Коуч", callback_data="couch"),
                               types.InlineKeyboardButton("Наставник", callback_data="mentor"),
                               types.InlineKeyboardButton("Эксперт", callback_data="expert"),
                               types.InlineKeyboardButton("Тинькофф банк", callback_data="bank"),
                               types.InlineKeyboardButton("Российская Инвестиционная Компания", callback_data="investor"),
                               types.InlineKeyboardButton("Smart Lab", callback_data="smart"),
                               types.InlineKeyboardButton("School of education", callback_data="soe"),
                               )
    return markup
          
@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "Объясняю как мной пользоваться")

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, is_persistent=True)
    btn1 = types.KeyboardButton("/help")
    btn2 = types.KeyboardButton("Совершить действие")
    btn3 = types.KeyboardButton("Мое состояние")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, "Привет! Я бот для совершения действия в игре. Введите проверочный код, выданный вам игротехником:", reply_markup=markup)
    

# @bot.message_handler(func=lambda message: message.chat.id != admin_id)
@bot.message_handler(func=lambda message: message.chat.id == admin_id)
def answer_message(message):

    if message.text in a.codes.keys():
        a.authenticate(message)
        bot.reply_to(message, f'Вы вошли как {a.authorize(message.chat.id).name}. Теперь все ваши действия будут происходить от его имени')
    
    elif (message.text == 'Мое состояние'):
        bot.reply_to(message, a.authorize(message.chat.id).check_capital())   
    
    elif (message.text == 'Совершить действие'):
        company = a.authorize(message.chat.id)
        bot.reply_to(message, 'Выберите действие', reply_markup=action_markup())

        #кнопки в зависимости от типа
    else:
        check = is_auto(message.text)
        if check is not False:
            #продолжаем вопрошать
            give_answer(message)
            #bot.reply_to(message, process_message(message.text))

        else:
            bot.reply_to(message, f'{message.from_user.first_name}, ваш запрос на обработке у игротехника')
            bot.forward_message(
                chat_id=admin_id,
                from_chat_id=message.chat.id,
                message_id=message.message_id)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "перевод":
        requests[call.message.chat.id] = 'перевод '
        bot.send_message(call.message.chat.id, 'Кому?', reply_markup=company_markup())
        bot.answer_callback_query(call.id, "Следуйте инструкциям")
    elif call.data == "капитал":
        chat_id = call.message.chat.id
        bot.send_message(chat_id, a.authorize(chat_id).check_capital())
    elif call.data == "курс":
        company = a.authorize(call.message.chat.id)
        ans = auto.process_message(company, 'создать курс')
        bot.send_message(call.message.chat.id, ans)
        bot.send_message(admin_id, f'{company.name} создал курс: {ans}')
    elif call.data in NAMES:
        requests[call.message.chat.id] += call.data
        bot.send_message(call.message.chat.id, 'Сколько?')
    else: 
        bot.send_message(call.message.chat.id, 'Вижу', reply_markup=company_markup())

#@bot.message_handler(func=lambda message: message.chat.id == admin_id)
#def handle_admin (message):
#    if re.match(r'!', str(message.text)) is not None:
#        bot.reply_to(message, process_request(str(message.text)))
#    else:
#       bot.forward_message(chat_id=message.reply_to_message.forward_from.id,
#                        from_chat_id=admin_id,
#                        message_id=message.message_id)
#       bot.reply_to(message, f'Your answer is sent to {message.reply_to_message.forward_from.username}')



bot.infinity_polling()