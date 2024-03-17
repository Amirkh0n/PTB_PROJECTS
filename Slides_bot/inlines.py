from telegram import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup
from menu import main_menu

def inline_handler(update, context):

    query = update.callback_query

    if query.data == "edit_data":
        buttons = [
            [
                InlineKeyboardButton(text="Ism", callback_data="edit_first_name"),
                #InlineKeyboardButton(text="Familiya", callback_data="edit_last_name"),
#            ],
#            [
#                #InlineKeyboardButton(text="Yosh", callback_data="edit_age"),
                InlineKeyboardButton(text="Oliygoh", callback_data="edit_study"),
            ],
            [
                InlineKeyboardButton(text="Kontakt", callback_data="edit_contact")
            ]
        ]
        query.message.edit_reply_markup(
            reply_markup=InlineKeyboardMarkup(buttons)
        )

    elif query.data == "edit_first_name":
        query.message.edit_text("Ism familiyangizni kiriting!")
        context.user_data['edit_step'] = True
        context.user_data['step'] = 1

    

    elif query.data == "edit_study":
        
        context.bot.delete_message(chat_id=query.message.chat_id, message_id=query.message.message_id)
        query.message.reply_text(text="O'qish joyingiz, yo'nalish hamda guruhingizni kiriting!\n\nMasalan: FarDU, filologiya, 19.112-guruh, yoki FJSTI, TPI, 521-guruh")
        context.user_data['edit_step'] = True
        context.user_data['step'] = 4

    elif query.data == "edit_contact":
        buttons = [
            [KeyboardButton(text="📞Kontaktni ulashish", request_contact=True)]
        ]
        context.bot.delete_message(chat_id=query.message.chat_id, message_id=query.message.message_id)
        query.message.reply_text("Kontaktingizni ulashing!", reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=True))
        context.user_data['edit_step'] = True
        context.user_data['step'] = 5

    elif query.data == "main_menu":
        context.bot.delete_message(chat_id=query.message.chat_id, message_id=query.message.message_id)
        main_menu(update, context, query.message.chat_id)

