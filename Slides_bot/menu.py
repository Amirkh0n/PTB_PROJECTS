from telegram import (
    KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove,
    InlineKeyboardButton, InlineKeyboardMarkup
)
from config import data 


def main_menu(update, context, chat_id):
    context.user_data['step']=6
    buttons = [
        [
            KeyboardButton(text="Buyurtma"), 
            KeyboardButton(text="Ma'lumotlarim")
        ]
    ]
    context.bot.send_message(
        chat_id=chat_id,
        text="Asosiy Menu",
        reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True)
    )

def send_my_info(update, context):
    user_id =update.message.from_user.id 
    date = data.get(str(user_id), {}).get('info')
    buttons = [
        [
            InlineKeyboardButton(text="Ma'lumotlarni o'zgartirish", callback_data="edit_data"),
        ],
        [
            InlineKeyboardButton(text="Asosiy Menu", callback_data="main_menu"),
        ]
    ]
    msg = update.message.reply_text(
        text="🕓",
        reply_markup=ReplyKeyboardRemove(),
    )
    context.bot.delete_message(chat_id=update.message.chat_id, message_id=msg.message_id)
    update.message.reply_text(
        text=f"👤<b>Ism-Familiya</b>: {date.get('name', None)}\n"
             f"<b>Oliygoh</b>: {date.get('univercity', None)}\n"
             f"📞<b>Nomer</b>: +{date.get('contact')}",
        reply_markup=InlineKeyboardMarkup(buttons),
        parse_mode="HTML"
    )

def product(update, context):
    buttons=[
        [
            KeyboardButton(text='Maqola'), 
            KeyboardButton(text='Tezis')
        ],
        [
            KeyboardButton(text='Slayd'),
            KeyboardButton(text = 'Kurs ishi')
        ]
    ]
    context.user_data['step'] = 7
    update.message.reply_text(
        text="Nima buyurtma qilmoqchisiz?",
        reply_markup= ReplyKeyboardMarkup(buttons, resize_keyboard=True)
    )