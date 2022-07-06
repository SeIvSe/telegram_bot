import telebot
from conf import Token, vales
from extensions import ConExp, ConErr

# Создаем экземпляр бота
bot = telebot.TeleBot(Token)


# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, '''Здравствуйте! Я помощник в конвертации валют.В какую валюту будем конвертировать?
    О том, как работать, введите /help
    Какие есть валюты, введите /values''')

@bot.message_handler(commands=["help"])
def help(m, res=False):
    bot.send_message(m.chat.id, '''Как работать с ботом: 
    1.Введите валюту в которую конвертируем.
    2.Введите базовую валюту
    3.Введите количество базовой валюты
    Пример: рубль доллар 53.7''')

@bot.message_handler(commands=["values"])
def values(m, res=False):
    bot.send_message(m.chat.id, 'Евро, доллар, рубль, биткоин')

# Получение сообщений от пользователя
@bot.message_handler(content_types=["text",])
def conv(message):
    try:
        values = message.text.split(' ')
        if len(values) != 3:
            raise ConExp('Необходимо указать только три параметра, например "биткоин доллар 1"')

        quote, base, amount = values
        t_base = ConErr.convert(quote, base, amount)
    except ConExp as e:
        bot.reply_to(message, f'Ошибка пользователя {e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось выполнить команду {e}')
    else:
        text = f'Цена {amount} {quote} в {base} - {t_base}'
        bot.send_message(message.chat.id, text)

# Запускаем бота
bot.polling()  #none_stop=True, interval=0



