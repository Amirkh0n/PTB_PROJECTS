import config as conf 
from telegram import KeyboardButton,  ReplyKeyboardMarkup 


def start_command(update, context):
    user_id =update.message.from_user.id 
    if user_id not in conf.data:
        conf.data.append(user_id)
        conf.save_data(conf.data)
        
    
    
    context.user_data['step']=conf.steps['main_menu']
    
    update.message.reply_text(
        text = "<b>Assalom alaykum \nIT - JOBS</b> kanalining rasmiy botiga xush kelibsiz! \n\n/help yordam buyrugi orqali nimalarga qodir ekanligimni bilib oling!", 
        reply_markup = conf.menu_buttons,
        parse_mode = "HTML"
    )


def help_command(update, context):
    text = """<b>DevInnovator</b> tomonidan tuzilgan IT - JOBS kanali. 

Bu yerda dasturlash bo`yicha
  #Ustoz,  
  #Shogird,
  #oquvKursi,
  #Sherik,  
  #Xodim va 
  #IshJoyi 
 topishingiz mumkin. 

E'lon berish: @IT_JOBS_ROBOT

Admin @DevInnovator"""
        
    buttons = [
        [KeyboardButton(text='Hodim kerak'), KeyboardButton(text='Ish joyi kerak')],
        [KeyboardButton(text='Ustoz kerak'), KeyboardButton(text='Shogird kerak')],
        [KeyboardButton(text='Sherik kerak'), KeyboardButton(text='O\'quv kursi')]
    ]
     
    update.message.reply_text(
        text = text,
        reply_markup = ReplyKeyboardMarkup(buttons, resize_keyboard=True,  one_time_keyboard=True),
        parse_mode = "HTML"
    )