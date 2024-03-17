import re
from telegram import ReplyKeyboardRemove, KeyboardButton, ReplyKeyboardMarkup
from menu import main_menu, send_my_info
from config import data, save_data 

def get_name(update, context):
    message = update.message.text
    user_id = update.message.from_user.id 
    data.get(str(user_id), {}).get('info', {})['name']=message.title()
    save_data(data)
    if context.user_data.get("edit_step"):
        context.user_data['edit_step'] = False
        context.user_data['step'] = 6
        send_my_info(update, context)
    else:
        context.user_data['step'] = 4
        update.message.reply_text(
            text="Oliygoh nomi, fakultet, guruhingizni kiriting:\nMisol: FarDU,  filologiya,  19.112-guruh",
            reply_markup=ReplyKeyboardRemove()
        )



def get_univercity(update, context):
    user_id = update.message.from_user.id 
    message = update.message.text     
    data.get(str(user_id), {}).get('info', {})['univercity']=message
    save_data(data)
    if context.user_data.get("edit_step"):
            context.user_data["edit_step"] = False
            context.user_data["step"] = 6
            send_my_info(update, context)

    else:
            context.user_data['step'] = 5
            buttons = [
                [KeyboardButton(text="Kontaktni ulashish", request_contact=True)]
            ]
            update.message.reply_text(
                text=f"Kontaktingizni ulashing!",
                reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=True)
            )
    


def get_text_contact(update, context):
    try:
        message = update.message.text
        user_id = update.message.from_user.id 
        data.get(str(user_id), {}).get('info', {})['contact']=message
        save_data(data)
        context.user_data['step'] = 6
        
        if context.user_data.get("edit_step"):
            context.user_data["edit_step"] = False
            send_my_info(update, context)
        else:
            main_menu(update, context, message.from_user.id)
    except:
        get_univercity(update, context)
        
    
