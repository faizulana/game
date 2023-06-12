import re
import telebot
from datetime import datetime
import json
from telebot import types
import player 
import admin
import authorize as a
import players
import autoprocessing as auto

bot = telebot.TeleBot("6009093323:AAGvxCnZm7VYWtqFluSNEqzFVMt2QpJp9FQ", parse_mode=None)
admin_id = 861236842

audience = 1000
names = ['entspace', 'skolkovo', 'skillbox', 'netology', 'couch', 'mentor', 'tutor', 'expert', 
         'bank', 'investor', 'soe', 'smart']

def give_answer (message):
    ans = 'В обработке'
    bot.reply_to(message, ans)

def is_auto(text):
    if re.match(r'перевести|создать', str(text).lower()) is not None:
        return True
    else: return False

def action_markup(company):
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 2
    # действия в зависимости от роли
    markup.add(types.InlineKeyboardButton("Перевести деньги", callback_data="перевод"),
                               types.InlineKeyboardButton("Проверить состояние", callback_data="капитал"),
                               )
    if company.influencer == True:
        markup.add(types.InlineKeyboardButton("Создать курс для аудитории", callback_data="курс"),
                   types.InlineKeyboardButton("Создать наставничество", callback_data="наставничество"),
                   types.InlineKeyboardButton("Реализовать на свою аудиторию", callback_data="реализовать"),
                   types.InlineKeyboardButton("Купить аудиторию", callback_data="купить"),)
    if company.teacher == True:
        markup.add(types.InlineKeyboardButton("Создать простой продукт", callback_data="простой"),
                   types.InlineKeyboardButton("Создать сложный продукт", callback_data="сложный"),
                   types.InlineKeyboardButton("Продать свободной аудитории", callback_data="продать"),)
    if company.name == 'Smart Lab':
        markup.add(types.InlineKeyboardButton("Разработать технологию 1", callback_data="технология1"),
                   types.InlineKeyboardButton("Разработать технологию 2", callback_data="технология2"),
                   types.InlineKeyboardButton("Разработать технологию 3", callback_data="технология3"),
                   types.InlineKeyboardButton("Внедрить технологию игроку", callback_data="внедрить"),
                   )
    if company.name == 'School of Education':
        markup.add(types.InlineKeyboardButton("Создать команду", callback_data="эксперты"),
                   types.InlineKeyboardButton("Обучить другого игрока", callback_data="обучить"),
                   types.InlineKeyboardButton("Передать команду экспертов", callback_data="передать"),
                   )
    return markup

def company_markup():
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(types.InlineKeyboardButton("Entspace", callback_data="entspace"),
                               types.InlineKeyboardButton("Сколково", callback_data="skolkovo"),
                               types.InlineKeyboardButton("Нетология", callback_data="netology"),
                               types.InlineKeyboardButton("Скиллбокс", callback_data="skillbox"),
                               types.InlineKeyboardButton("Коуч", callback_data="couch"),
                               types.InlineKeyboardButton("Наставник", callback_data="tutor"),
                               types.InlineKeyboardButton("Ментор", callback_data="mentor"),
                               types.InlineKeyboardButton("Эксперт", callback_data="expert"),
                               types.InlineKeyboardButton("Тинькофф банк", callback_data="bank"),
                               types.InlineKeyboardButton("Российская Инвестиционная Компания", callback_data="investor"),
                               types.InlineKeyboardButton("Smart Lab", callback_data="smart"),
                               types.InlineKeyboardButton("School of education", callback_data="soe"),
                               )
    return markup
          
def request_markup():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Done", callback_data="entspace"))

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "Объясняю как мной пользоваться. Можно сделать FAQ")

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, is_persistent=True)
    btn1 = types.KeyboardButton("/help")
    btn2 = types.KeyboardButton("Совершить действие")
    btn3 = types.KeyboardButton("Мое состояние")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, "Привет! Я бот для совершения действия в игре. \n\nВведите проверочный код, выданный вам игротехником:", reply_markup=markup)
    

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
        bot.reply_to(message, 'Выберите действие', reply_markup=action_markup(company))
    else:
        company=a.authorize(message.chat.id)
        check = is_auto(message.text)
        if check is not False:
            give_answer(message)
            bot.reply_to(message, auto.process_message(company=company, text=message.text))

        else:
            bot.reply_to(message, f'{message.from_user.first_name}, ваш запрос на обработке у игротехника')
            bot.forward_message(
                chat_id=admin_id,
                from_chat_id=message.chat.id,
                message_id=message.message_id)
            bot.send_message(chat_id=admin_id, text=f'От {company.name}', reply_markup=request_markup())

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    chat_id = call.message.chat.id
    if call.data == "капитал":
        bot.send_message(chat_id, 'Какой компании?', reply_markup=company_markup())
        bot.answer_callback_query(call.id, "Выберите компанию из списка")
    elif call.data == "перевод":
        bot.send_message(chat_id, 'Введите сообщение вида "перевести *число* *компания-получатель*"')
    elif call.data == "курс":
        company = a.authorize(call.message.chat.id)
        ans = auto.process_message(company, 'создать курс')
        bot.send_message(call.message.chat.id, ans)
        bot.send_message(admin_id, f'{company.name} заявка на курс: {ans}')
    elif call.data == "наставничество":
        company = a.authorize(call.message.chat.id)
        ans = auto.process_message(company, 'создать наставничество')
        bot.send_message(call.message.chat.id, ans)
        bot.send_message(admin_id, f'{company.name} заявка на наставничество: {ans}')
    elif call.data == "простой":
        company = a.authorize(call.message.chat.id)
        ans = auto.process_message(company, 'создать простой')
        bot.send_message(call.message.chat.id, ans)
        bot.send_message(admin_id, f'{company.name} заявка на простой продукт: {ans}')
    elif call.data == "сложный":
        company = a.authorize(call.message.chat.id)
        ans = auto.process_message(company, 'создать сложный')
        bot.send_message(call.message.chat.id, ans)
        bot.send_message(admin_id, f'{company.name} заявка на сложный продукт: {ans}')
    elif call.data == "технология1":
        company = a.authorize(call.message.chat.id)
        ans = auto.process_message(company, 'создать технология1')
        bot.send_message(call.message.chat.id, ans)
        bot.send_message(admin_id, f'{company.name} заявка на разработку технологии 1: {ans}')
    elif call.data == "технология2":
        company = a.authorize(call.message.chat.id)
        ans = auto.process_message(company, 'создать технология2')
        bot.send_message(call.message.chat.id, ans)
        bot.send_message(admin_id, f'{company.name} заявка на разработку технологии 2: {ans}')
    elif call.data == "технология3":
        company = a.authorize(call.message.chat.id)
        ans = auto.process_message(company, 'создать технология3')
        bot.send_message(call.message.chat.id, ans)
        bot.send_message(admin_id, f'{company.name} заявка на разработку технологии 3: {ans}')
    elif call.data == "эксперты":
        company = a.authorize(call.message.chat.id)
        ans = auto.process_message(company, 'создать эксперты')
        bot.send_message(call.message.chat.id, ans)
        bot.send_message(admin_id, f'{company.name} заявка на создание команды экспертов: {ans}')
    elif call.data == "обучить":
        company = a.authorize(call.message.chat.id)
        bot.send_message(chat_id, 'Напишите сообщение вида "обучить игрока *название компании или инфлюенсера*"')
    elif call.data == "купить":
        company = a.authorize(call.message.chat.id)
        bot.send_message(chat_id, 'Напишите сообщение вида "купить *число* аудитории')
    elif call.data == "передать":
        company = a.authorize(call.message.chat.id)
        bot.send_message(chat_id, 'Напишите сообщение вида "передать экспертов *название компании-получателя*')
    elif call.data == "продать":
        company = a.authorize(call.message.chat.id)
        bot.send_message(chat_id, 'Напишите сообщение вида "продать простой/сложный на *число* аудитории"')
    elif call.data == "реализовать":
        company = a.authorize(call.message.chat.id)
        bot.send_message(chat_id, 'Напишите сообщение вида "реализовать *тип продукта*')
    elif call.data == "внедрить":
        company = a.authorize(call.message.chat.id)
        bot.send_message(chat_id, 'Напишите сообщение вида "внерить *название или номер технологии* *название компании-получателя*')

    elif call.data in names:
        companytocheck = a.identify_company(call.data)
        bot.send_message(chat_id, companytocheck.check_capital())

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