import sys
import time
import telepot
from pprint import pprint
from telepot.loop import MessageLoop
import importlib
##############################################################
#### BOT INFO ####

#TOKEN 1525175182:AAEZVTBmwguwj2SKLGmsLd-21YLIjaKfwsg

#{'id': 1525175182, 
#'is_bot': True, 
#'first_name': 'Dio', 
#'username': 'BlasfemicoBot', 
#'can_join_groups': True, 
#'can_read_all_group_messages': False,
#'supports_inline_queries': False}


#### MY INFO ####

#{'first_name': 'Bonaventura',
#'id': 467817356,
#'last_name': 'Testa',
#'type': 'private',
#'username': 'Skaren'},
##############################################################



##############################################################
#### DEFINITIONS ####
module = importlib.import_module("FileHandling")


Bestemmie = {
    "dio" : "dio",
    "madonna" : "madonna",
    "gesù" : "gesù",
    "maronn" : "maronn"
}


def handle(msg):
    countbestemmie = 0
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    
    if content_type == 'text':  
        for key in Bestemmie:
            if key in msg['text']:
                bot.sendMessage(chat_id, key)  #FOR NOW RETURNS THE KEY VALUE
                module.RaiseCounter()
                


            
##############################################################




##############################################################
#### MAIN ####
  

print("BOT RUNNING")
bot = telepot.Bot("1525175182:AAEZVTBmwguwj2SKLGmsLd-21YLIjaKfwsg")
MessageLoop(bot, handle).run_as_thread()






# Keep the program running.
while 1:
    time.sleep(10)

##############################################################