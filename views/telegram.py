from telegram.ext import Updater
from telegram.ext import CommandHandler
from controllers import feed

def start(bot, update):
    bot.send_message(chat_id=update.message.chat.id, text="Welcome to Simple Feed Bot. ;)")

def add(bot, update):
    chat_id = update.message.chat.id
    feed_url = feed.get_msg(update.message.text)
    if(not feed_url):
        msg = "No feed was entered."
    elif(not feed.check_feed(feed_url)):
        msg = "This feed is invalid."
    else:
        if(not feed.save_feed(chat_id, feed_url)):
            msg = "The feed can not be inserted."
        msg = "The feed has been added."
    bot.send_message(chat_id=chat_id, text=msg)

def test(bot, job):
    print('Test')

def initialize(token):
    update = Updater(token=token)
    job = update.job_queue
    dispatcher = update.dispatcher

    start_handler = CommandHandler('start', start)
    add_handler = CommandHandler('add', add)
    job_minute = job.run_repeating(test, interval=10, first=0)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(add_handler)

    update.start_polling()
    update.idle()