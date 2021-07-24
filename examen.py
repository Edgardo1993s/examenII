import os
import telebot

TOKEN = '1905710559:AAE4HjhUrrHo7R5kOIgotxlU3XP-p5cB9lM'

bot=telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['formula'])

def formula(m):
    cid=m.chat.id
    bot.send_photo(cid, open('formula.png','rb'))

@bot.message_handler(commands=['conversion'])

def conversion(m):
    cid=m.chat.id
    bot.send_photo(cid, open('conversion.jpg','rb'))

@bot.message_handler(commands=['documento'])

def pdf(m):
    cid=m.chat.id
    bot.send_document(cid, open('documento.pdf','rb'))

@bot.message_handler(commands=['localizacion'])
def documento(m):
    cid=m.chat.id
    bot.send_location(cid, 15.49560, -87.99128)

bot.polling()

