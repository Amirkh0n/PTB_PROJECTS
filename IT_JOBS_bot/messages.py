import admins
import config as conf 
from telegram import KeyboardButton, ReplyKeyboardMarkup 


def messages(update, context):
    message = update.message.text
    step = context.user_data.get('step', 0)
    
    if message in ["Hodim kerak", "Ish joyi kerak", "Ustoz kerak", "Shogird kerak", "Sherik kerak", "O'quv kursi"]:
        context.user_data['forms_title'] = message 
        message = message.replace('kerak', '')
        text = f"<b>{message} {conf.text}"
        
        update.message.reply_text(
            text = text, 
            parse_mode = "HTML"
        )
        context.user_data['step']=conf.steps['forms']
        
        if message == "Hodim ":
            context.user_data['form'] = conf.form_hodim
        else:
            context.user_data['form'] = conf.forms_all
            
        context.user_data['form_id'] = 1
        context.user_data['info'] = []
        
        update.message.reply_text(
            text = context.user_data['form'][context.user_data['form_id']], 
            parse_mode = "HTML"
        )
    
    elif step == conf.steps['forms']:
        form_id = context.user_data['form_id']+1
        context.user_data['form_id'] = form_id 
        form = context.user_data['form']
        context.user_data['info']. append(message)
        
        if form_id == 10:
            context.user_data['step']=conf.steps['confirm']
            admins.send_info(update,  context )
            buttons = [[ KeyboardButton(text ='HA'), KeyboardButton(text = "Yo'q") ]]
            update.message.reply_text(text="Barcha ma'lumotlar to'g'rimi?", reply_markup=ReplyKeyboardMarkup(buttons,  resize_keyboard=True,  one_time_keyboard= True))
        else:
            try:
                update.message.reply_text(
                    text = form[form_id], 
                    parse_mode = "HTML"
                )
            except Exception as e:
                print(f" Xatolik:  {e}")
                
    elif step == conf.steps['confirm']:
        if message == 'HA':
            admins.send_info_to_admin(update,  context)
            update.message.reply_text(
                text = "📪 <b>So`rovingiz tekshirish uchun adminga jo`natildi!</b>\n\nE'lon 24-48 soat ichida kanalda chiqariladi.",
                parse_mode = "HTML",
                reply_markup = conf.menu_buttons 
            )
            context.user_data['step']=conf.steps['main_menu']
    
            
        elif message == "Yo'q":
             update.message.reply_text(
                 text = 'Qabul qilinmadi!',
                 reply_markup = conf.menu_buttons 
             )
             context.user_data['step']=conf.steps['main_menu']
    
