import telebot
from telebot import types
#Для работы необходима библиотека PyTelegramBotAP (Telebot),если она не установлена,
# то необходимо  ввести в терминале или в командной строке pip install pytelegrambotapi


#Вводим токен,для подключения
# Для этого необходимо найти бота @BotFather написать ему /start или /newbot
bot = telebot.TeleBot("TOKEN")

#Список кнопок
item1 = types.InlineKeyboardButton("Общая информация", callback_data="question_1")
item2 = types.InlineKeyboardButton("Программы", callback_data="question_2")
item3 = types.InlineKeyboardButton("Детское меню", callback_data="question_3")
item4 = types.InlineKeyboardButton("Взрослое меню", callback_data="question_4")
item5 = types.InlineKeyboardButton("Геолокация", callback_data="question_5")
item6 = types.InlineKeyboardButton("Контакты", callback_data="question_6")
item7 = types.InlineKeyboardButton("Instagram", callback_data="question_7")
markup = types.InlineKeyboardMarkup(row_width=2)
markup.add(item1, item2, item3, item4, item5, item6, item7)


#Функция отслеживающая команду /start
@bot.message_handler(commands=["start"])
def send_start(message):
            app_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            app_keyboard = types.KeyboardButton(text="Отравить заявку")
            app_markup.add(app_keyboard)
            mess = f"Здравствуйте, <b>{message.from_user.first_name}</b> ! Что Вас интересует?"
            mess_1 = f"<b>{message.from_user.first_name}</b> , здесь Вы можете отправить заявку в формате [ДАТА МЕРОПРИЯТИЯ/КОНТАКТНЫЙ НОМЕР]"
            bot.send_message(message.chat.id, mess, parse_mode="html", reply_markup=markup)
            mess_2=bot.send_message(message.chat.id, mess_1, parse_mode="html",reply_markup=app_markup)
            bot.register_next_step_handler(mess_2, create_request)

#Получения сообщения от пользователя
# forward_message пересылает сообщения от пользователя (которое он отправил боту) в нужный чат (в сообщении будет "переслано от...")
# send_message отправляет в нужный чат: текст сообщения, id имя, фамилию, ник пользователя
# (в сообщении будут те поля которые указаны)
# 463912483 - id куда отправлять\пересылать сообщение

def create_request(message):
    bot.send_message(message.chat.id, 'Ваша заявка принята,администратор свяжется Вами в ближайшее время')
    bot.forward_message(123, message.chat.id, message.message_id)
    bot.send_message(123, '{0}\n{1}\n{2}\n{3}\n{4}'.format(message.text, message.chat.id, message.from_user.first_name,
                                                           message.from_user.last_name, message.from_user.username))



@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.message:
        if call.data == "question_1":
            bot.send_message(call.message.chat.id,
                             "ДЕТСКИЙ ДЕНЬ РОЖДЕНИЯ \nКОСМОС БАР ждёт в гости вас и ваших детей, чтобы в весёлой компании провести незабываемый праздник 🔥 \nМы предоставляем огромный зал, который будет в вашем распоряжении на весь период проведения мероприятия.\nУ нас можете ЗАКАЗАТЬ:\n Стандартный пакет -280 BYN\n▫️аниматор (игровая программа)-45 минут \n▫️оформление зала\n▫️стилистическая посуда \n▫️фотограф- 60 минут\n▫️караоке \n▫️дымовая машина\n▫️лазерное шоу\n▫️дискотека\nДОПОЛНИТЕЛЬНО:\n▫️детские коктейли\n▫️детское/взрослое меню\n▫️торт",
                             reply_markup=markup)
    if call.message:
        if call.data == "question_2":
            bot.send_message(call.message.chat.id,
                             "👼Для малышей: \n▫️Щенячий патруль\n▫️Три кота \n▫️Фиксики\n▫️Дракоша\n▫️Клоун \n▫️Ми-ми-мишки\n▫️Микки Маус \n▫️Свинка Пеппа\n▫️Хаги-Ваги\n👱Для мальчиков:\n▫️Миньон\n▫️Пират \n▫️Minecraft \n▫️Brawl stars \n▫️Brawl stars \n▫️Brawl stars \n▫️Among us \n▫️Военная вечеринка \n▫️Marvel \n👩‍🦰Для девочек :\n▫️Русалочка\n▫️Пони искорка\n▫️Сказочный патруль\n▫️Эльза \n▫️Тролль розочка\n▫️Гавайская вечеринка \n▫️Кукла LoL\n▫️Уточка Лалафан \n👫Для подростков:\n▫️Tik-Tok туса\n▫️Кальмар \n▫️Челлендж пати \n▫️Ведущий для подростков\n▫️Айфон патти",
                             reply_markup=markup)
    if call.message:
        if call.data == "question_3":
            photo = open("DM.png","rb")
            bot.send_photo(call.message.chat.id, photo, reply_markup=markup)

    if call.message:
        if call.data == "question_4":
           photo_3 = open("M3.png", "rb")
           bot.send_photo(call.message.chat.id, photo_3,reply_markup=markup)

    if call.message:
        if call.data == "question_5":
           bot.send_location(call.message.chat.id, 54.308880, 26.837523,
                             reply_markup=markup)

    if call.message:
        if call.data == "question_6":
            bot.send_message(call.message.chat.id,
                             "📍 г. Молодечно, ул. Партизанская,3А \nБронирование\Дополнительная информация по ☎ (25) 778-91-74",
                             reply_markup=markup)
    if call.message:
        if call.data == "question_7":
            markup.add(types.InlineKeyboardButton("Перейдите в Instagram !", url="https://instagram.com/cosmos_bar_molo?igshid=YmMyMTA2M2Y="))
            bot.send_message(call.message.chat.id,"Подписывайтесь на наш Instagram и узнавайте новости первыми!",
                             reply_markup=markup)

#Запускаем бота
bot.polling(none_stop=True)



