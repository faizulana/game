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

takt = 1

bot = telebot.TeleBot("6009093323:AAGvxCnZm7VYWtqFluSNEqzFVMt2QpJp9FQ", parse_mode=None)
admin_id = 861236842
helper_id = 861236842

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
    markup.add(types.InlineKeyboardButton("Другое", callback_data="другое"),)
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
    markup.add(types.InlineKeyboardButton("Done", callback_data="done"))
    return markup

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "Для совершения действия нажмите на кнопку внизу и выберите нужную команду из списка для получения инструкции. \n\nПроверить свое имущество и баланс можно нажав на кнопку Мое состояние внизу экрана \n\nНазвания комнапий можно писать кириллицей или латинницей. \n\nБудьте внимательны с командами перевода денег и создания продуктов, опечатки могут помешать обработать вашизапросы")

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, is_persistent=True)
    btn1 = types.KeyboardButton("/help")
    btn2 = types.KeyboardButton("Совершить действие")
    btn3 = types.KeyboardButton("Мое состояние")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, "Привет! Я бот для совершения действия в игре. \n\nВведите проверочный код, выданный вам игротехником:", reply_markup=markup)
    

#@bot.message_handler(func=lambda message: message.chat.id != admin_id)
@bot.message_handler(func=lambda message: message.chat.id == admin_id)
def answer_message(message):

    if message.text in a.codes.keys():
        a.authenticate(message)
        bot.reply_to(message, f'Вы вошли как {a.authorize(message.chat.id).name}. Теперь все ваши действия будут происходить от его имени')

    elif message.text == a.ADMIN_CODE:
        global helper_id
        helper_id = int(message.text)
        bot.send_message(helper_id, 'Теперь вам будут приходить сообщения о важных событиях')
        a.admins.append()
    elif (message.text == 'Мое состояние'):
        bot.reply_to(message, a.authorize(message.chat.id).check_capital())
        bot.reply_to(message, f'Свободная аудитория в данный момент: {audience}')  
    
    elif (message.text == 'Совершить действие'):
        company = a.authorize(message.chat.id)
        bot.reply_to(message, 'Выберите действие', reply_markup=action_markup(company))
    else:
        company=a.authorize(message.chat.id)
        check = is_auto(message.text)
        if check is not False:
            give_answer(message)
            ans = auto.process_message(company=company, text=message.text)
            bot.reply_to(message, ans)
            bot.send_message(helper_id, f'{company.name}: {message.text}: {ans}')

        else:
            bot.reply_to(message, f'{message.from_user.first_name}, ваш запрос на обработке у игротехника')
            bot.forward_message(
                chat_id=admin_id,
                from_chat_id=message.chat.id,
                message_id=message.message_id)
            bot.send_message(chat_id=admin_id, text=f'От {company.name}, баланс {company.capital}, т1: {company.technology2}, т2: {company.technology3}, аудитория {company.audience}', reply_markup=request_markup())

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    chat_id = call.message.chat.id
    if call.data == "капитал":
        bot.send_message(chat_id, 'Какой компании?', reply_markup=company_markup())
        bot.answer_callback_query(call.id, "Выберите компанию из списка")
    elif call.data == "перевод":
        bot.send_message(chat_id, 'Вы собираетесь сделать перевод. Для этого введите сообщение вида: \nперевести *число* *компания-получатель*')
    elif call.data == "курс":
        company = a.authorize(call.message.chat.id)
        bot.send_message(chat_id, 'Вы собираетесь создать курс. Чтобы подтвердить действие, введите сообщение вида: \nсоздать курс')
    elif call.data == "наставничество":
        company = a.authorize(call.message.chat.id)
        bot.send_message(chat_id, 'Вы собираетесь создать наставничество. Чтобы подтвердить действие, введите сообщение вида: \nсоздать наставничество')
    elif call.data == "простой":
        company = a.authorize(call.message.chat.id)
        bot.send_message(chat_id, 'Вы собираетесь создать простой продукт. Чтобы подтвердить действие, введите сообщение вида: \nсоздать простой')
    elif call.data == "сложный":
        company = a.authorize(call.message.chat.id)
        bot.send_message(chat_id, 'Вы собираетесь создать сложный продукт. Чтобы подтвердить действие, введите сообщение вида: \nсоздать сложный')
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
        if admin.takt == 1: 
            bot.answer_callback_query(call.id, 'Эта технология станет доступна только во втором такте')
        else: 
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
        bot.send_message(chat_id, 'Вы собираетесь обучить игрока - это значит, что он получит право создавать простые образовательные продукты. \nЧтобы сделать это, напишите сообщение вида: \n\n"обучить игрока *название компании или инфлюенсера*"')
    elif call.data == "купить":
        company = a.authorize(call.message.chat.id)
        bot.send_message(chat_id, 'Напишите сообщение вида: \n\n"купить *число* аудитории')
    elif call.data == "передать":
        company = a.authorize(call.message.chat.id)
        bot.send_message(chat_id, 'Напишите сообщение вида: \n\n"передать экспертов *название компании-получателя*')
    elif call.data == "продать":
        company = a.authorize(call.message.chat.id)
        bot.send_message(chat_id, 'Вы собираетесь продать простой или сложный продукт на свободный рынок. Помните, что для привлечения аудитории на этот продукт вы должны будете сначала оплатить услуги маркетинга по 2 у.е. за человека, если продукт простой, и по 4 у.е. за человека, если продукт сложный')
        bot.send_message(chat_id, 'Чтобы реализовать продукт на рынок, введите сообщение вида: \n\n"продать простой/сложный на *число* аудитории"')
    elif call.data == "реализовать":
        company = a.authorize(call.message.chat.id)
        bot.send_message(chat_id, 'Напишите сообщение вида: \n\n"реализовать *тип продукта* свой или *название компании*')
    elif call.data == "внедрить":
        company = a.authorize(call.message.chat.id)
        bot.send_message(chat_id, 'Напишите сообщение вида: \n\n"внерить *название или номер технологии* *название компании-получателя*')
    elif call.data == "другое":
        company = a.authorize(call.message.chat.id)
        bot.send_message(chat_id, 'Опишите детали своего запроса, и я направлю его игротехнику')
    elif call.data == "done":
        bot.delete_message(chat_id=admin_id, message_id=call.message.message_id)

    elif call.data in names:
        companytocheck = a.identify_company(call.data)
        bot.send_message(chat_id, companytocheck.check_capital())

    else: 
        bot.send_message(call.message.chat.id, 'Вижу, но не знаю что с этим делать. Напишите запрос текстом.', reply_markup=company_markup())

@bot.message_handler(func=lambda message: message.chat.id == admin_id)
def handle_admin (message):
    if re.match(r'!', str(message.text)) is not None:
       bot.reply_to(message, admin.process_request(str(message.text)))
    elif message.text == 'отбивка':
        global takt
        players.expences()
        takt+=1
        for s in a.sessions:
            bot.send_message(s.chat_id, 'Такт завершен. Дождитесь итогов такта')
            bot.send_message(admin_id, f'{s.company.name}: {s.company.capital}, {s.company.audience}')
    else:
      bot.send_message(chat_id=message.reply_to_message.forward_from.id,
                     text = message.text)
      bot.reply_to(message, f'Your answer is sent to {message.reply_to_message.forward_from.username}')



bot.infinity_polling()