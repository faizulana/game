import re
import telebot
from datetime import datetime
import json
from telebot import types
import player 
import admin
import authentication as a
import players

bot = telebot.TeleBot("6009093323:AAGvxCnZm7VYWtqFluSNEqzFVMt2QpJp9FQ", parse_mode=None)
admin_id = 861236842

audience = 1000

def text_normalize (text):
    words = str(text).lower()

def give_answer (message):
    ans = 'Заявка принята в обработку'
    bot.reply_to(message, ans)

def validate_user(input):
    return True

def is_command(text):
    if re.match(r'перевод|капитал', str(text).lower()) is not None:
        return True
    else: return False

# def process_message(text):
#     components=str(text).lower().split()
#     if components[0] == 'перевод':
#         sender = identify_company(components[1])
#         receiver = identify_company(components[3])
#         answer = sender.transfer_money(amount=int(components[2]), to=receiver)
#         return answer
#     elif components[0] == 'капитал':
#         company = identify_company(components[1])
#         return company.check_capital()
    
    
#def expences():
    # skolkovo.capital-=150
    # entspace.capital-=150
    # like.capital-=150
    # skillbox.capital-=150
    # influencer1.capital-=50
    # influencer2.capital-=50
    # influencer3.capital-=50
    # smart.capital-=50
    # soe.capital-=50
    # bank.capital-=100
    # regulator.capital-=80
          
@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "Объясняю как мной пользоваться")

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("/help")
    btn2 = types.KeyboardButton("Совершить действие")
    btn3 = types.KeyboardButton("Мое состояние")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, "Привет! Я бот для совершения действия в игре. Введите проверочный код, выданный вам игротехником:", reply_markup=markup)
    

# @bot.message_handler(func=lambda message: message.chat.id != admin_id)
@bot.message_handler(func=lambda message: message.chat.id == admin_id)
def answer_message(message):
    if int(message.text) in a.codes.keys():
        a.authenticate(message)
        bot.reply_to(message, f'Вы вошли как {a.authorize(message.chat.id).name}. Теперь все ваши действия будут происходить от его имени')
    elif (message.text == 'Мое состояние'):
        bot.reply_to(message, a.authorize(message.chat.id).check_capital())   
    elif (message.text == 'Совершить действие'):
        company = a.authorize(message.chat.id)
        bot.reply_to(message, 'Выберите действие')
        #кнопки в зависимости от типа
        check = is_command(message.text)
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