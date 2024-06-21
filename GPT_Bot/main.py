from telegram.ext import Updater,  CommandHandler, CallbackQueryHandler,  MessageHandler,  Filters 
from telegram import InlineKeyboardMarkup, InlineKeyboardButton 
from config import TOKEN
from inlines import inlines
from messages_gpt_chat import messagess 

def start_command(update, context):
     user=update.message.from_user
     name=user.first_name
     buttons=InlineKeyboardMarkup([[ InlineKeyboardButton(text="Chat GPT", callback_data = "gpt")]])
     update.message.reply_text( text=f"Assalomu aleykum,  *{name.title()}*.\nBo'limlardan birini tanlang:", reply_markup=buttons, parse_mode="Markdown")
 
def delete_context(update, context):
    context.user_data["messages"] = [{"role": "system", "content": "You are an intelligent assistant."}]
    update.message.reply_text(text = "Chat GPT tarixi tozalandi!")

def main():
    updater = Updater(token=TOKEN)
    dp = updater.dispatcher 
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler( "clear", delete_context))
    dp.add_handler(MessageHandler(Filters.text, messagess))
    dp.add_handler(CallbackQueryHandler( inlines))
    
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()