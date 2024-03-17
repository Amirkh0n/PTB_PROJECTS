from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler
import wikipedia
import globals

# Bot token va Wikipedia kutubxonasini o'rnatish
TOKEN = ""
wikipedia.set_lang("uz")  # Wikipedia tilini o'zgartiring

def start(update, context):
    buttons=[
       [InlineKeyboardButton(text="O'zbek", callback_data="uz"), InlineKeyboardButton(text="Русскый", callback_data="ru"), InlineKeyboardButton(text="English", callback_data="en")]
    ]
    if "lang" in context.user_data:
        lang=context.user_data["lang"]
    else:
        lang=update.message.from_user.language_code
    update.message.reply_text(
        text = globals.MESSAGES["start"][lang],
        reply_markup = InlineKeyboardMarkup( buttons ),
        parse_mode="Markdown"
    )

def search_wikipedia(update, context):
    lang=context.user_data.get("lang", "en")
    buttons = []
    text = update.message.text
    search_list = wikipedia.search(text)
    if search_list:
        for i in search_list:
            button = [InlineKeyboardButton(text=i, callback_data=search_list.index(i))]
            buttons.append(button)
        buttons.append([InlineKeyboardButton(text=globals.MESSAGES[ "button_menu"][lang], callback_data="menu")])
        context.user_data["list"] = search_list
        context.user_data["text"] = text
        context.user_data["buttons"] = buttons
        update.message.reply_text(
            text=globals.MESSAGES["in_search"][lang],
            reply_markup= InlineKeyboardMarkup(buttons),
            parse_mode="Markdown"
        )
    else:
        update.message.reply_text(
            text=globals.MESSAGES[ "not_search"][lang],
            parse_mode="Markdown"
        )

def inlines(update, context):
    query = update.callback_query
    list_items = context.user_data.get("list", [])
    lang = context.user_data.get("lang", "en")
    
    if query.data in ["uz", "ru", "en"]:
        wikipedia.set_lang(query.data)
        context.user_data["lang"] = query.data
        text = globals.MESSAGES["post_lang"][query.data]
        markup = None
    elif query.data == "back":
        markup = InlineKeyboardMarkup(context.user_data["buttons"])
        text = context.user_data["text"]
    elif query.data == "menu":
        text = globals.MESSAGES["menu"][lang]
        markup = None
    elif int(query.data) in range(len(list_items)):
        list_item = list_items[int(query.data)]
        button = [ [InlineKeyboardButton(text=globals.MESSAGES["button_back"][lang], callback_data="back")]]
        markup = InlineKeyboardMarkup(button)
        send_long_message_by_sentences( bot=context.bot, chat_id=query.message.chat_id, text=wikipedia.summary(list_item), inline_buttons=markup, parse_mode=None)
        return  # query.message.edit_text ni chaqirmang, chunklarga bo'lingan xabarlarni jo'natish uchun
    else:
        text = "*404 XATOLIK*"
        markup = None
    
    query.message.edit_text(
        text=text,
        reply_markup=markup,
        parse_mode="Markdown"
    )

#def send_long_message(bot, chat_id, text, parse_mode=None):
#    max_length = 4000
#    for i in range(0, len(text), max_length):
#        bot.send_message(chat_id, text[i:i + max_length], parse_mode=parse_mode)

def send_long_message_by_sentences(bot, chat_id, text, parse_mode=None, inline_buttons=None):
    sentences = text.split('. ')
    current_chunk = sentences[0]

    for sentence in sentences[1:]:
        if len(current_chunk) + len(sentence) + 2 <= 4000:  # 2 for space and dot between sentences
            current_chunk += f". {sentence}"
        else:
            bot.send_message(chat_id, current_chunk, parse_mode=parse_mode)
            current_chunk = sentence

    # Send the last chunk
    send_chunk_with_inline_keyboard(bot, chat_id, current_chunk, parse_mode=parse_mode, inline_buttons=inline_buttons)

def send_chunk_with_inline_keyboard(bot, chat_id, text, parse_mode=None, inline_buttons=None):
    markup = None
    if inline_buttons:
        markup = inline_buttons
    bot.send_message(chat_id, text, reply_markup=markup, parse_mode=parse_mode)

def main():
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # /start va /wikipedia buyrug'lariga javob berish
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text, search_wikipedia))
    dispatcher.add_handler(CallbackQueryHandler(inlines))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()