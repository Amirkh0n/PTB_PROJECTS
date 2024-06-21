import re
import config as conf 
from functions import main_menu, send_my_info
from telegram import ReplyKeyboardRemove, KeyboardButton, ReplyKeyboardMarkup,  InlineKeyboardButton, InlineKeyboardMarkup 



def save_name(update, context):
    message = update.message.text
    user_id = update.message.from_user.id 
    conf.data.get(str(user_id), {}).get('info', {})['name']=message.title()
    conf.save_data(conf.data)
    if context.user_data.get("edit_step"):
        context.user_data['edit_step'] = False
        conf.data[str(user_id)]['step'] = conf.steps['main_menu']
        send_my_info(update, context)
    else:
        conf.data[str(user_id)]['step'] = conf.steps['contact']
        update.message.reply_text(
            text="Kontaktingizni ulashing!",
            reply_markup=ReplyKeyboardMarkup([[KeyboardButton(text='Kontaktni ulashish 📞', request_contact=True)]],  resize_keyboard=True,  one_time_keyboard=True)
        )


def save_contact(update, context):
    user = update.message.from_user
    conf.data[str(user_id)]['step'] = conf.steps['main_menu']
    data=conf.get_data(user.id)    
    if data.get('step') == conf.steps["contact"]:
        conf.data.get(str(user.id), {}).get('info', {})['contact']=update.message.contact.phone_number
        conf.save_data(conf.data)
        main_menu(update, context, chat_id = user.id)
        

