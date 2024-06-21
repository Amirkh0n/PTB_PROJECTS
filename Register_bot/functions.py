import config as conf 
from telegram import ( 
    InlineKeyboardMarkup, 
    InlineKeyboardButton, 
    ReplyKeyboardRemove,
    KeyboardButton,
    ReplyKeyboardMarkup,
)


def edit_lang(update, context, chat_id):
    buttons=[
        [ InlineKeyboardButton(text = 'Uzbek 🇺🇿', callback_data='uz'), 
          InlineKeyboardButton(text = 'Русский 🇷🇺', callback_data='ru'),
          InlineKeyboardButton(text = 'English 🇺🇸',  callback_data='en')]
    ]
    context.bot.send_message(
        chat_id = chat_id,
        text = "🇺🇸 Choose language!\n🇷🇺 Выберите язык!\n🇺🇿 Kerakli tilni tanlang!\n\t👇👇👇", 
        reply_markup = InlineKeyboardMarkup(buttons)
    )


def main_menu(update, context, chat_id):
    conf.data[str(chat_id)]['step'] = conf.steps['main_menu']
    buttons = [
        [
            KeyboardButton(text="Forma yaratish"), 
            KeyboardButton(text="Ma'lumotlarim")
        ]
    ]
    context.bot.send_message(
        chat_id=chat_id,
        text="<b>Asosiy Menu</b>",
        parse_mode = "HTML",
        reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True)
    )


def send_my_info(update, context):
    user_id =update.message.from_user.id 
    data = conf.get_data(user_id).get('info', {})
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
        text=f"👤<b>Ism</b>: {data.get('name', None)}\n"
                 f"📞<b>Nomer</b>: +{data.get('contact')}\n"
                 f"<b>Formalar soni:</b> {data.get('forms', 0)}",
        reply_markup=InlineKeyboardMarkup(buttons),
        parse_mode="HTML"
    )


