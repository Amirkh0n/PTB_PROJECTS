from telegram import InlineKeyboardButton,  InlineKeyboardMarkup 

def inlines(update, context):
    query=update.callback_query 
    if query.data=="gpt":
        context.user_data["isGPT"]=True
        text="Salom men *Chat GPT*man. Menga istagan mavzuyingizda savol berishingiz mumkin!"
        buttons = InlineKeyboardMarkup([[ InlineKeyboardButton( text="Ortga", callback_data="back")]])
        
    elif query.data == "back":
        context.user_data["isGPT"]=False
        text = "*ASOSIY MENU*"
        buttons = InlineKeyboardMarkup([[ InlineKeyboardButton( text="Chat GPT", callback_data="gpt")]])
    query.edit_message_text(
            text=text,
            reply_markup=buttons,
            parse_mode="Markdown"
        )