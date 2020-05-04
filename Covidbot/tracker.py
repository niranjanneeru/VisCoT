from bot import telegram_chatbot

bot = telegram_chatbot("config.cfg")
def help(msg):
    if msg =='/abort':
        return True

def age():
    return '''How old are you?
    
    /abort to quit the process'''


def gender():
    return '''Please select your gender
    /Male
    /Female
    /Others
    
    Click the desired
    
    /abort to quit the process'''


def temp():
    return '''Please let us know your current body temperature in degree Fahrenheit (Normal body temperature is 98.6°F):
/Normal (96°F-98.6°F)
/Fever (98.6°F-102°F)
/HighFever (>102°F)
/Unaware

Click on desired category

/abort to quit the process
    '''


def symptom():
    return '''Are you experiencing any of the symptoms below
1.Dry Cough
2.Loss or diminished sense of smell
3.Sore Throat
4.Weakness
5.Change in Appetite
6.None of these

Enter the appropriate numbers with a space in between

eg :- 2 3 4

/abort to quit the process'''


def symptom2():
    return '''Additionally, please verify if you are experiencing any of the symptoms below
1.Moderate to Severe Cough
2.Difficulty in Breathing
3.Drowsiness
4.Persistant Pain and Pressure in Chest
5.Severe Weakness
6.None of these

Enter the appropriate numbers with a space in between

eg :- 2 3 4

/abort to quit the process'''


def travel():
    return '''Please select your travel and exposure details
1.No Travel History
2.No contact with anyone with Symptoms
3.History of travel or meeting in affected geographical area in last 14 days
4.Close contact with a person with Fever and Cough in last 14 days

Enter the appropriate number

/abort to quit the process    '''


def end(grade):
    if grade > 20:
        return '''Potential Risk Status : High
Consider a Medical Check-up'''
    elif grade > 2:
        return '''Potential Risk Status : Medium
Consider Taking Rest'''
    else:
        return '''Potential Risk Status : Low
You seems Fine'''


def checkUpdates(update_id=None):
    grade = 0
    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if True:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = str(item["message"]["text"])
            except:
                message = None
            from_ = item["message"]["from"]["id"]
            bot.send_message('''Welcome to our VisCoT Covid Diagonoser
                Our coronavirus disease self assessment scan has been developed on the basis of guidelines from the WHO and MHFW, Government of India. This interaction should not be taken as expert medical advice. Any information you share with us will be kept strictly confidential.''',
                             from_)
            bot.send_message(age(), from_)
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
                    if help(message):
                        return update_id
                    if not message.isdigit():
                        bot.send_message('''Invalid Input''', from_)
                        bot.send_message(age(), from_)
                    else:
                        break
            bot.send_message(gender(), from_)
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
                    if help(message):
                        return update_id
                    if not (message == '/Male' or message == '/Female' or message == '/Others'):
                        bot.send_message('''Invalid Gender''', from_)
                        bot.send_message(gender(), from_)
                    else:
                        break
            bot.send_message(temp(), from_)
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
                    if help(message):
                        return update_id
                    if not (
                            message == '/Normal' or message == '/Fever' or message == '/HighFever' or message == "/Unaware"):
                        bot.send_message('''Invalid''', from_)
                        bot.send_message(temp(), from_)
                    else:
                        break
            if message == '/HighFever':
                grade += 5
            elif message == 'Fever':
                grade += 3
            bot.send_message(symptom(), from_)
            while True:
                updates = bot.get_updates(offset=update_id)
                updates = updates["result"]
                if updates:
                    for item in updates:
                        update_id = item["update_id"]
                        try:
                            message = str(item["message"]["text"]).split()
                        except:
                            message = None
                        from_ = item["message"]["from"]["id"]
                    if help(message):
                        return update_id
                    if not (
                            '1' in message or '2' in message or '3' in message or '4' in message or '5' in message or '6' in message):
                        bot.send_message('''Invalid''', from_)
                        bot.send_message(symptom(), from_)
                    elif len(message) > 1 and '6' in message:
                        bot.send_message('''You can't select 6 along with the others''', from_)
                        bot.send_message(symptom(), from_)
                    else:
                        break
            if len(message) > 2:
                grade += 5
            elif len(message) >= 0 and '6' not in message:
                grade += 3
            bot.send_message(symptom2(), from_)
            while True:
                updates = bot.get_updates(offset=update_id)
                updates = updates["result"]
                if updates:
                    for item in updates:
                        update_id = item["update_id"]
                        try:
                            message = str(item["message"]["text"]).split()
                        except:
                            message = None
                        from_ = item["message"]["from"]["id"]
                    if help(message):
                        return update_id
                    if not (
                            '1' in message or '2' in message or '3' in message or '4' in message or '5' in message or '6' in message):
                        bot.send_message('''Invalid''', from_)
                        bot.send_message(symptom2(), from_)
                    elif len(message) > 1 and '6' in message:
                        bot.send_message('''You can't select 6 along with the others''', from_)
                        bot.send_message(symptom2(), from_)
                    else:
                        break
            if len(message) > 2:
                grade += 5
            elif len(message) >= 0 and '6' not in message:
                grade += 3
            bot.send_message(travel(), from_)
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
                    if help(message):
                        return update_id
                    if not ('1' in message or '2' in message or '3' in message or '4' in message):
                        bot.send_message('''Invalid''', from_)
                        bot.send_message(travel(), from_)
                    else:
                        break
            if '3' in message:
                grade += 5
            elif '4' in message:
                grade += 20
            bot.send_message(end(grade), from_)
            return update_id

