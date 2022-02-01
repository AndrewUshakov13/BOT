import telebot
import COVID19Py
import requests

bot = telebot.TeleBot('1161971870:AAHSZ_yCu2CoVgG377mzz9uet4QDHcLHlxg')
# keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
# keyboard1.row('Привет', 'Пока')
covid19 = COVID19Py.COVID19()


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start') # reply_markup=keyboard1
@bot.message_handler(content_types=['text'])
def send_text(message):                                                                                                                                                        
	if message.text.lower() == 'привет':
		bot.send_message(message.chat.id, 'Привет, мой создатель')
	elif message.text.lower() == 'пока':
		bot.send_message(message.chat.id, 'Прощай, создатель')
	elif message.text.lower() == 'корона':
		bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAMLXpbiMR17kS4-u-RVvJlDexhUhQkAAsEBAAJWnb0Ky9vpP2Sb6hYYBA')
# def mess(message):
	final_message = ""
	get_message_bot = message.text.strip().lower()
	if get_message_bot == "сша":
		location = covid19.getLocationByCountryCode("US")
	elif get_message_bot == "украина":
		location = covid19.getLocationByCountryCode("UA")
	elif get_message_bot == "россия":
		location = covid19.getLocationByCountryCode("RU")
	elif get_message_bot == "беларусь":
		location = covid19.getLocationByCountryCode("BY")
	elif get_message_bot == "казакхстан":
		location = covid19.getLocationByCountryCode("KZ")
	elif get_message_bot == "италия":
		location = covid19.getLocationByCountryCode("IT")
	elif get_message_bot == "франция":
		location = covid19.getLocationByCountryCode("FR")
	elif get_message_bot == "германия":
		location = covid19.getLocationByCountryCode("DE")
	elif get_message_bot == "япония":
		location = covid19.getLocationByCountryCode("JP")
	else:
	    location = covid19.getLatest()
	    final_message = f"<u>Данные по всему миру:</u>\n<b>Заболевших: </b>{location['confirmed']:,}\n<b>Сметрей: </b>{location['deaths']:,}"

	if final_message == "":
		date = location[0]['last_updated'].split('T')
		time = date[1].split(".")
		final_message = f"<u>Данные по стране:</u>\nНаселение: {location[0]['country_population']:,}\n" \
			f"Последнее обновление: {date[0]} {time[0]}\nПоследние данные:\n<b>" \
			f"Заболевших: </b>{location[0]['latest']['confirmed']:,}\n<b>Сметрей: </b>" \
			f"{location[0]['latest']['deaths']:,}"

	bot.send_message(message.chat.id, final_message, parse_mode='html')

bot.polling(none_stop=True)
