import config as conf 
import commands as comm 
import messages as mess 
from inlines import inlines 
from telegram.ext import Updater,  CommandHandler,  MessageHandler, Filters, CallbackQueryHandler 


def main():
    updater = Updater (token = conf.TOKEN)
    dp = updater.dispatcher 
    
    dp.add_handler(CommandHandler('start', comm.start_command))
    dp.add_handler(CommandHandler('help', comm.help_command))
    dp.add_handler(MessageHandler(Filters.text, mess.messages))
    dp.add_handler(CallbackQueryHandler(inlines))
    
    print("\tRUNNING 🏃")
    updater.start_polling()
    updater.idle()
    print('\n\tSTOP 🛑 \n')


if __name__ == '__main__':
    main()