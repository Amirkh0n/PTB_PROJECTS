import config as conf
import commands as comm
import messages as mess
import register as reg 
from inlines import inlines 
from telegram.ext import ( 
    Updater, 
    CommandHandler,  
    MessageHandler,
    Filters,
    CallbackQueryHandler, 
)


def main():
    updater = Updater(token = conf.TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', comm.start_command))
    dp.add_handler(MessageHandler(Filters.text, mess.messages))
    dp.add_handler(MessageHandler(Filters.contact, reg.save_contact))
    
    dp.add_handler(CallbackQueryHandler(inlines))
    print("RUNNING!!! ;)\n")
    updater.start_polling()
    updater.idle()
    print('STOP 🛑 \n')
    
if __name__ == '__main__':
    main()