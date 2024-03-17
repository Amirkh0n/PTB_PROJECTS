import json 
from telegram import InlineKeyboardMarkup, InlineKeyboardButton 

TOKEN="YOUR_BOT_TOKEN"
KARTA='YOUR_CARD_NUMBER'

steps = {
    "name": 1,
    "study": 4,
    "contact": 5,
    "menu": 6,
    "buyurtma":7,
    'fan': 8,
    "mavzu":9,
    'chek_photo':10
}

admin_id="type: int, admin's ID"

with open("data.json", 'r') as file:
    data = json.load(file)
    
def save_data(data):
    with open('data.json', 'w') as file:
        json.dump(data, file, indent = 4)

#def sent_to_admin(update, context, datas):
#    context.bot.send_message(
#        chat_id = admin_id, 
#        text = f"""ㅤㅤㅤㅤ<b>🌟Yangi buyurtma:</b> 
#👤<b>User:</b> <a href="tg://user?id={datas['id']}">{datas['name']}</a>
#📞<b>Nomer:</b> +{datas['nomer']}
#📤<b>Buyurtma:</b> {datas['buyurtma']}
#📃<b>Mavzu:</b> {datas['mavzu']}
#""", 
#        reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(text="📞 Bog'lanish", url="tg://user?id={datas['id']}")]]),
#        parse_mode = 'HTML'
#    )
    
def sent_to_admin(update, context, photo, datas):
    admin_id = 717862748
    if 'id' in datas and 'name' in datas and 'contact' in datas and 'buyurtma' in datas and 'mavzu' in datas:
        context.bot.send_photo(
            chat_id=admin_id,
            photo = photo, 
            caption = f"""ㅤㅤㅤㅤ🌟Yangi buyurtma: 
👤<b>User:</b> <a href="tg://user?id={datas['id']}">{datas['name']}</a>
📞<b>Nomer:</b> +{datas['contact']}
📤<b>Buyurtma:</b> {datas['buyurtma']}
📃<b>Mavzu:</b> {datas['mavzu']}
""", 
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="📞 Bog'lanish", url=f"tg://user?id={datas['id']}")]]),
            parse_mode='HTML'
        )
    else:
        context.bot.send_message(chat_id=admin_id, text="Ma'lumotlar to'liq kiritilmagan, xatolik!")
