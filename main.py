import telebot
import datetime
import threading
import os
from connection import key

print(key)

from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())

bot = telebot.TeleBot(os.getenv("TOKEN"))


@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, "wassup homie,i am reminder bot,enter /reminder")


@bot.message_handler(commands=["reminder"])
def reminder_message(message):
    bot.send_message(message.chat.id, "ENTER THE NAME OF THE REMINDER")
    bot.register_next_step_handler(message, set_reminder_name)


def set_reminder_name(message):
    user_data = {}
    user_data[message.chat.id] = {"reminder_name": message.text}
    bot.send_message(
        message.chat.id,
        "enter the date and time when you want to receive a reminder in the format YYYY-MM-DD hh:mm:ss.",
    )
    bot.register_next_step_handler(message, reminder_set, user_data)


def reminder_set(message, user_data):
    try:
        reminder_time = datetime.datetime.strptime(message.text, "%Y-%m-%d %H:%M:%S")
        now = datetime.datetime.now()
        delta = reminder_time - now
        if delta.total_seconds() <= 0:
            bot.send_message(message.chat.id, "you entered a past date,try again.")

        else:
            reminder_name = user_data[message.chat.id]
            ["reminder_name"]
            bot.send_message(
                message.chat.id,
                'reminder "{}" is set to {}.'.format(reminder_name, reminder_time),
            )
            reminder_timer = threading.Timer(
                delta.total_seconds(), send_reminder, [message.chat.id, reminder_name]
            )
            reminder_timer.start()
    except ValueError:
        bot.send_message(
            message.chat.id, "you entered the wrong date and time format,try again."
        )


def send_reminder(chat_id, reminder_name):
    bot.send_message(chat_id, 'Time to get your reminder "{}"!'.format(reminder_name))


@bot.message_handler(func=lambda message: True)
def handle_all_message(message):
    bot.send_message(
        message.chat.id,
        "i dont understand what you're saying . tO create a reminder,type /reminder",
    )


if __name__ == "__main__":
    bot.polling(none_stop=True)
