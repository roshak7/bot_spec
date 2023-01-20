import telebot
import datetime

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# TOKEN
TOKEN = '5829963774:AAFMR1qVuV1hkkTytcYeGJty7A0NsHmRnUc'

bot = telebot.TeleBot(TOKEN)
 
 
@bot.message_handler(commands=['start'])
def process_start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    msg = bot.send_message(message.chat.id,
                           text='Welcome!',
                           reply_markup=keyboard)
 
 
@bot.message_handler(content_types=['text'])
def send_email(message):
    try:
        username = "{0.username}".format(message.from_user, bot.get_me())
        fromaddr = "mail@gmail.com"
        mypass = "password"
        toaddr = "roshak7@gmail.cinom"
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "Отправитель: Telegram bot"  # + str(message.chat.id)
        body = "Message: Telegram_bot \n\n" + message.text
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, mypass)
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()
        bot.reply_to(message, "Отправлено на %s:" % (msg['To']))
    except Exception:
        bot.reply_to(message, "ERROR")
bot.polling()





server = smtplib.SMTP(host='host_address',port=your_port)
msg = MIMEMultipart()


message = "Hi Yandex Q"

# параметры сообщения
password = "IDarinho077"
msg['From'] = "idarkubalov@ya.ru"
msg['To'] = ""
msg['Subject'] = "Subscription"

# Тело сообщения
msg.attach(MIMEText(message, 'plain'))

#Запуск сервера SMTP
server = smtplib.SMTP('smtp.gmail.com: 587')

server.starttls()

# Логин 
server.login(msg['From'], password)


# Отправка
server.sendmail(msg['From'], msg['To'], msg.as_string())

server.quit()

print ("Отправлено на %s:" % (msg['To']))