from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
from telegram import ReplyKeyboardRemove, ChatAction
from menu import main_menu
from messages import message_handler
from inlines import inline_handler
from buyurtma import photo_handler 
from config import *



def start_handler(update, context):
    user = update.message.from_user
    update.message.reply_chat_action(action=ChatAction.TYPING)
    
    if data.get(str(user.id), {}).get('info', {}).get('contact'):
        main_menu(update, context, user.id)
    else:
        data[str(user.id)]={
            'info': {},
            'buyurtmalar':[],
            'fanlar':[],
            'mavzular':[], 
            'summalar':[]
        }
        save_data(data)
        context.user_data['step'] = steps['name']
        update.message.reply_text(
            text="Assalom aleykum,  Mustaqil ishlar uchun slaytlar, maqolalar va tezislar hamda kurs ishi yozib beramiz. \nBatafsil ma'lumot: /info \n\nBotdan foydalanish uchun ism familiyangizni yozing.\n\n (Misol: Abdulloh Akbaraliyev)\n\t❗❗❗❗❗❗❗❗❗❗❗❗\n(Iltimos fake ma'lumotlar bermang, har bir buyurtma adminlar tomonidan tekshiriladi!) ",
            reply_markup=ReplyKeyboardRemove()
        )

def contact_handler(update, context):
    step = context.user_data.get('step',0)
    user = update.message.from_user
    if step == steps["contact"]:
        #context.user_data["contact"] = update.message.contact.phone_number
        data.get(str(user.id), {}).get('info', {})['contact']=update.message.contact.phone_number
        save_data(data)
        context.user_data['step'] = steps['menu']
        main_menu(update,context,user.id)


def info_handler(update, context):
    text = f"\tAssalom aleykum\n📕PEDAGOGIK FANLAR VA 📚TIBBIY FANLAR bo'yicha:\n\n📝Kurs ishi - 35 000 so'm\n📝Maqola - 30 000 so'm\n📝Tezis - 20 000 so'm\n📝Slaydlar  - 5 000 so'm."
    update.message.reply_text(text)
    start_handler(update, context)


def help_handler(update, context):
    text = f"Bot haqida ma'lumot olish uchun /info 👈ni bosing.\n Buyurmalar 24-72 soat ichida tayyor bo'ladi!"
    update.message.reply_text(text)
    start_handler(update, context)


def main():
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start_handler))
    dispatcher.add_handler(CommandHandler('info', info_handler))
    dispatcher.add_handler(CommandHandler('help', help_handler))
    
    dispatcher.add_handler(MessageHandler(Filters.text, message_handler))
    dispatcher.add_handler(MessageHandler(Filters.contact, contact_handler))
    dispatcher.add_handler(MessageHandler(Filters.photo, photo_handler))
    
    dispatcher.add_handler(CallbackQueryHandler(inline_handler))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
    