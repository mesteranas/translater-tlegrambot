import googletrans
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton
stip=0
From=""
to=""
def buttons(FFrom=True):
    if FFrom:
        keyboard_buttons = [[KeyboardButton(text="auto detect")]]
    else:
        keyboard_buttons = []
    for key,value in googletrans.LANGUAGES.items():
        keyboard_buttons.append([KeyboardButton(text=value)])
    return ReplyKeyboardMarkup(keyboard=keyboard_buttons, one_time_keyboard=True)
def message(msg):
    try:
        global stip,From,to,auto
        content_type,chat_type,chat_id=telepot.glance(msg)
        if content_type == 'text':
            if msg["text"]=="/start":
                bot.sendMessage(chat_id, f"Welcome {msg['from']['first_name']} to this bot. This bot allows you to  translate . Please select from language", reply_markup=buttons())
                stip=0
            else:
                if stip==0:
                    try:
                        if msg["text"]=="auto detect":
                            re="auto"
                        else:
                            re=msg["text"]
                        From=re
                        stip=1
                        bot.sendMessage(chat_id,"now send to language", reply_markup=buttons(False))
                    except:
                        bot.sendMessage(chat_id,"error")
                elif stip==1:
                    try:
                        re=msg["text"]
                        to=re
                        stip=2
                        bot.sendMessage(chat_id,"now send   text", reply_markup=None)
                    except:
                        bot.sendMessage(chat_id,"error")
                elif stip==2:
                    try:
                        translater=googletrans.Translator()
                        if From=="auto":
                            ff=translater.detect(msg['text']).lang
                        else:
                            ff=From
                        result=translater.translate(msg["text"],src=ff,dest=to).text
                        stip=0
                        bot.sendMessage(chat_id,"result=" + str(result))   
                        bot.sendMessage(chat_id, f"Welcome {msg['from']['first_name']} to this bot. This bot allows you to   translate . Please select from  language", reply_markup=buttons())
                    except Exception as e:
                        print(e)
                        result="error"
                        stip=0
                        bot.sendMessage(chat_id,"result=" + str(result))   
        else:
            bot.sendMessage(chat_id,"please send text messages only")
    except Exception as e:
        print(e)

bot=telepot.Bot("token")
bot.deleteWebhook()
MessageLoop(bot,{"chat":message}).run_as_thread()
print("runing")
while True:
    pass