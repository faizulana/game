import re
import telebot
from datetime import datetime
import json

bot = telebot.TeleBot("6009093323:AAGvxCnZm7VYWtqFluSNEqzFVMt2QpJp9FQ", parse_mode=None)
admin_id = 861236842

class Player:
    def __init__(self, name, capital, property):
        self.name = name
        self.capital = capital
        self.property = property

    def transfer_money(self, amount, to):
        if self.capital < amount:
            return 'Недостаточно средств'
        else: 
            self.capital-=amount
            to.capital+=amount
            return f'Перевод выполнен. Ваш баланс {self.capital} у.е.'
    
    def check_capital(self):
        return f'Ваш баланс {self.capital} у.е., \nИмущество: \n{self.property}'
        
skillbox = Player('Skillbox', 400, 'Лицензия на оказание образовательных услуг')
entspace = Player('Entspace', 400, 'Команда экспертов')

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

def process_message(text):
    components=str(text).lower().split()
    if components[0] == 'перевод':
        sender = identify_company(components[1])
        receiver = identify_company(components[3])
        answer = sender.transfer_money(amount=int(components[2]), to=receiver)
        return answer
    elif components[0] == 'капитал':
        company = identify_company(components[1])
        return company.check_capital()
    
        
def identify_company(name):
    if name in ['skillbox', 'skilbox', 'скилбокс', 'скиллбокс']:
        return skillbox
    if name in ['entspace', 'enspace', 'энтспейс', 'энтспэйс', 'ентспейс', 'ентспэйс']:
        return entspace
    
def process_request(text):
    components = str(text).lower().split()
    if components[0] == '!добавить':
        if components[1] == 'имущество':
            company = identify_company(components[2])
            company.property+=', '
            company.property+=' '.join(components[3::])
            return company.property
        if components[1] == 'деньги':
            company = identify_company(components[2])
            company.capital+=int(components[3])
            return company.capital
    if components[0] == '!убрать':
        if components[1] == 'деньги':
            company = identify_company(components[2])
            company.capital-=int(components[3])
            return company.capital
    if components[0] == '!изменить':
        if components[1] == 'имущество':
            company = identify_company(components[2])
            company.property=' '.join(components[3::])
            return company.property
        if components[1] == 'деньги':
            company = identify_company(components[2])
            company.capital=int(components[3])
            return company.capital
    if components[0] == '!изменить':
        if components[1] == 'имущество':
            company = identify_company(components[2])
            company.property=' '.join(components[3::])
            return company.property
        if components[1] == 'деньги':
            company = identify_company(components[2])
            company.capital=int(components[3])
            return company.capital
        

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Введите нужную команду из списка: \nПеревод денег: /перевод \nПроверить ресурсы: /капитал")

@bot.message_handler(commands='перевод')
def send_money(message):
    bot.reply_to(message, "Напишите сообщение вида 'ПЕРЕВОД компания-отправитель сумма компания-получатель'")

@bot.message_handler(commands='капитал')
def send_money(message):
    bot.reply_to(message, "Напишите сообщение вида 'КАПИТАЛ название_компании'")

#@bot.message_handler(func=lambda message: message.chat.id != admin_id)
@bot.message_handler(func=lambda message: message.chat.id == admin_id)
def answer_message(message):
    check = is_command(message.text)
    if check is not False:
        give_answer(message)
        bot.reply_to(message, process_message(message.text))

    else:
        bot.reply_to(message, f'{message.from_user.first_name}, перенаправил ваш запрос игротехнику')
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