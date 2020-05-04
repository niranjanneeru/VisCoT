from bot import telegram_chatbot
import msgmanage
import tracker

bot = telegram_chatbot("config.cfg")


def text(msg):
    if msg.startswith('/start') or msg.startswith('/menu'):
        return msgmanage.if_start()
    elif msg.startswith('/help'):
        return msgmanage.helper()
    elif msg.startswith('/info'):
        return msgmanage.info()
    elif msg.startswith('/global'):
        return msgmanage.global_()
    elif msg.startswith('/checker'):
        tracker.checkUpdates(update_id=update_id)
        return '''Thanks for Using me

See my Creators Over here
https://meenakshi2604.github.io/Covid-tracker/

I work for VisCoT App find the application in the above link

See My Manual :-  /help
'''
    else:
        return '''Invalid Inputs try /help'''


def make_reply(msg):
    reply = None
    if msg is not None:
        reply = text(msg.strip())
    return reply


update_id = None
while True:
    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = str(item["message"]["text"])
            except:
                message = None
            from_ = item["message"]["from"]["id"]
            reply = make_reply(message)
            bot.send_message(reply, from_)