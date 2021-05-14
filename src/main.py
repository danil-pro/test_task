import time
import telebot
import requests
import json
import config
import os

bot = telebot.TeleBot(config.TOKEN)
service_url = config.SERVICE_URL
db_path = config.DB_PATH
db_cache_time = config.DB_CACHE_TIME
messages = config.MESSAGES


def get_data():
    db_last_mod_time = int(os.path.getmtime(db_path))
    current_time = int(time.time())

    if db_last_mod_time + db_cache_time < current_time:
        data = json.loads(requests.get(service_url).text)['rates']

        with open(db_path, 'w') as f:
            f.write(str(data).replace("\'", "\""))

    else:
        with open(db_path, 'r') as f:
            data = json.load(f)

    res = ''
    for k, v in data.items():
        v = round(v, 2)
        res += f'{k}: {v}\n'

    return res


@bot.message_handler(commands=['list'])
def list_handler(message):
    res = get_data()
    bot.send_message(message.chat.id, res)


@bot.message_handler(commands=['exchange'])
def exchange_handler(message):
    try:
        data = json.loads(requests.get(service_url).text)['rates']

        user_data = message.text.split()
        num = int(user_data[1])
        cur_ex = user_data[-1]
        price = data[cur_ex] * num
        bot.send_message(message.chat.id, f'{round(price, 2)} {cur_ex}')
    except Exception as e:
        print(e)
        bot.send_message(message.chat.id, messages['exchange_format_error'])


def main():
    bot.polling(none_stop=True)


if __name__ == '__main__':
    main()
