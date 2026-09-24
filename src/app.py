import telebot
import base 
import app_api

bot = telebot.TeleBot(base.TOKEN)

print('bot created ...')

@bot.message_handler(commands=['start'])
def say_hello(message):
    bot.send_message(message.chat.id, text='به بات ما خوش امدید')


@bot.message_handler(commands=['help'])
def support(message):
    bot.reply_to(message, text='در صورت نیاز به پشتیبانی با شماره 5443 تماس بگیرید')


@bot.message_handler(commands=['news'])
def show_news(message):
    markup = telebot.types.InlineKeyboardMarkup(row_width=2)

    btn1 = telebot.types.InlineKeyboardButton(text='اخبار ورزشی', url='https://varzesh3.com')
    btn2 = telebot.types.InlineKeyboardButton(text='اخبار عمومی', url='https://entekhab.ir')
    btn3 = telebot.types.InlineKeyboardButton(text='اخبار اقتصادی', url='https://tradingview.com')

    markup.add(btn1, btn2, btn3)

    bot.send_message(message.chat.id, text='یکی از گزینه های زیرا انتخاب کنید',
                     reply_markup=markup)

@bot.message_handler(commands=['menu'])
def show_menu(message):
    markup = telebot.types.ReplyKeyboardMarkup()

    btn1 = telebot.types.KeyboardButton(text='تماس با ما')
    btn2 = telebot.types.KeyboardButton(text='درباره ما')
    btn3 = telebot.types.KeyboardButton(text='عضویت')
    btn4 = telebot.types.KeyboardButton(text='بازگشت')

    markup.add(btn1, btn2, btn3, btn4)

    bot.send_message(message.chat.id, text='یکی از گزینه های زیرا انتخاب کنید',
                         reply_markup=markup)


@bot.message_handler(commands=['movie'])
def show_movie_message(message):
    msg = bot.send_message(message.chat.id, text='ای دی فیلم را وارد کنید')
    bot.register_next_step_handler(msg, show_movie_info)

def show_movie_info(message):
    movie_id = message.text
    result = app_api.get_movie_info_by_id(movie_id)
    bot.send_message(message.chat.id, text=f'{result[0]} / {result[-1]}')


@bot.message_handler(commands=['movie2'])
def show_movie_message(message):
    msg = bot.send_message(message.chat.id, text='نام فیلم را وارد کنید')
    bot.register_next_step_handler(msg, show_movie_name)

def show_movie_name(message):
    movie_name = message.text
    result = app_api.get_movie_info_by_name(movie_name)
    bot.send_message(message.chat.id, text=f'{result}')



@bot.message_handler(func=lambda message:True)
def handele_other_message(message):
    if message.text == 'تماس با ما':
        email = 'support@gmail.com'
        mobile = '09165437667'
        post_box = '1235498664'
        info = f'email:{email} / mobile:{mobile} / post_box:{post_box}'
        bot.send_message(message.chat.id, text=info)

    elif message.text == 'درباره ما':
        bot.send_message(message.chat.id, text='ما یک گروه اموزشی هستیم')

    elif message.text == 'عضویت':
        pass

    elif message.text == 'بازگشت':
        markup = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, text='بازگشت به منوی اصلی', reply_markup=markup)
        
    else:
        bot.send_message(message.chat.id, text='پیغام شما را متوجه نشدم')

if __name__ == '__main__':
    bot.infinity_polling()