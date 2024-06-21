import config as conf 
from telegram import InlineKeyboardMarkup, InlineKeyboardButton 


def send_info(update, context):
    info = context.user_data.get('info', [])
    forms_title = context.user_data.get('forms_title')
    if info:
     if forms_title == "Hodim kerak":
        text= f"""
<b>Xodim kerak:</b>

<b>🏢 Idora:</b> {info[0]} 
<b>📚 Texnologiya:</b> {info[1]}
<b>🇺🇿 Telegram:</b> @{update.message.from_user.username} 
<b>📞 Aloqa: </b> {info[2]}
<b>🌐 Hudud:</b> {info[3]} 
<b>✍️ Mas'ul: </b> {info[4]}
<b>🕰 Murojaat vaqti: </b> {info[5]}
<b>🕰 Ish vaqti:</b> {info[6]}
<b>💰 Maosh: </b> {info[7]}
<b>‼️ Qo`shimcha: </b> {info[8]}
"""
        
     else:
        text = f"""<b>{forms_title}:</b>

<b>{conf.form_titles.get(forms_title)}:</b> {info[0]} 
<b>🕑 Yosh:</b> {info[1]}
<b>📚 Texnologiya:</b> {info[2]}
<b>🇺🇿 Telegram:</b> @{update.message.from_user.username} 
<b>📞 Aloqa:</b> {info[3]} 
<b>🌐 Hudud:</b> {info[4]} 
<b>💰 Narxi:</b> {info[5]} 
<b>👨🏻‍💻 Kasbi:</b> {info[6]} 
<b>🕰 Murojaat qilish vaqti:</b>  {info[7]} 
<b>🔎 Maqsad:</b>  {info[8]}
"""
    context.user_data['full_form'] = text
    
    if conf.orders:
        order_id = context.user_data['order_id'] = str(int(list(conf.orders.keys())[-1])+1)
        conf.orders[order_id] = text
    else:
        conf.orders['1'] = text
        context.user_data['order_id'] = '1'
    conf.save_order(conf.orders)
    
    update.message.reply_text(text = text,  parse_mode = "HTML")


def send_info_to_admin(update,  context ):
    context.bot.send_message(
        chat_id = conf.ADMIN_ID,
        text = context.user_data.get('full_form'),
        parse_mode = "HTML",
    )
    context.bot.send_message(
        chat_id = conf.ADMIN_ID,
        text = "Kanalga yuborilsinmi?",
        reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(text='HA', callback_data=f"post_{context.user_data.get('order_id')}"), InlineKeyboardButton(text='Yo\'q', callback_data=f"del_{context.user_data.get('order_id')}")]])
        )