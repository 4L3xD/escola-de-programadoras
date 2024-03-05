import sys
import time
import telepot
from telepot.loop import MessageLoop
import env
from nlp import ia

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    ai_msg = ia(msg['text'])
    if content_type == 'text':
        bot.sendMessage(chat_id, ai_msg)


#TOKEN = sys.argv[1]  # get token from command-line
TOKEN = env.token

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)