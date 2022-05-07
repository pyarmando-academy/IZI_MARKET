import telebot
token = ''
bot = telebot.TeleBot(token)

from db import create_connection, consulta_productos, oferta_productos


@bot.message_handler(content_types=['text'])
def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Consulta de Producto', callback_data=3))
    markup.add(telebot.types.InlineKeyboardButton(text='Producto Sugerido', callback_data=4))
    markup.add(telebot.types.InlineKeyboardButton(text='Ofertas y Promociones', callback_data=5))
    markup.add(telebot.types.InlineKeyboardButton(text='Acerca de Mi', callback_data=6))
    asistente = "Soy un asistente virtual de la tienda IZI MARKET tenemos el objetivo de ayudarte  y reducir el tiempo que empleas en consultar un producto,garantizando una excelente atención."
    if message.text == 'informacion':
        bot.send_message(message.chat.id, text=asistente, reply_markup=markup)
    elif message.text != "informacion":
        conn = create_connection('dbizimarket.db')
        if consulta_productos(conn, message.text):
            bot.send_message(message.chat.id, consulta_productos(conn, message.text))
        else:
            bot.send_message(message.chat.id, "Por Ahora no teenemos ese producto en Stock")


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    asistente = "Soy un asistente virtual de la tienda IZI MARKET tenemos el objetivo de ayudarte  y reducir el tiempo que empleas en consultar un producto,garantizando una excelente atención."
    if call.data == '3':
        answer = 'Adelante!! Ingresa el Producto de categoria abarrotes que desea consultar!'
        bot.send_message(call.message.chat.id, answer)
    elif call.data == "4":
        answer = 'Selecciono Producto Sugerido!'
        bot.send_message(call.message.chat.id, answer)
    elif call.data == "5":
        conn = create_connection('dbizimarket.db')
        bot.send_message(call.message.chat.id, oferta_productos(conn, 1))
    else:
        answer = asistente
        bot.send_message(call.message.chat.id, answer)


bot.polling()
