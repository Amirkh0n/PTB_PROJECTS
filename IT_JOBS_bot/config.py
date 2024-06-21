import json 
from telegram import KeyboardButton,  ReplyKeyboardMarkup 


TOKEN = "BOT TOKEN"
ADMIN_ID = 0000000 # your  tg ID
CHANNEL_ID = -1008888888 # your channel ID


with open("data/data.json", 'r') as file:
    data = json.load(file)

def save_data(data):
    with open('data/data.json', 'w') as file:
        json.dump(data, file, indent = 4)


with open("data/orders.json", 'r') as file:
    orders = json.load(file)
    
def save_order(orders = orders):
    with open('data/orders.json', 'w') as file:
        json.dump(orders, file, indent = 4)

steps = {
    'main_menu': 0,
    'forms' : 1,
    'confirm' : 2
}

form_titles = {"Ish joyi kerak": "👨‍💼 Xodim", "Ustoz kerak" : "🎓 Shogird", "Shogird kerak": "🎓 Ustoz", "Sherik kerak": '👨‍💼 Sherik'}

forms = {
    #umumiy
    'ism' : '<b>Ism, familiyangizni kiriting?</b>',
    'yosh' : "<b>🕑 Yosh: </b>\n\nYoshingizni kiriting?\nMasalan, 19",
    'texnologiya' : "<b>📚 Texnologiya:</b>\n\nTalab qilinadigan texnologiyalarni kiriting?\nTexnologiya nomlarini vergul bilan ajrating. Masalan, \n\nJava, C++, C#",
    'aloqa' : "<b>📞 Aloqa: </b>\n\nBog`lanish uchun raqamingizni kiriting?\nMasalan, +998 90 123 45 67",
    'hudud' : "<b>🌐 Hudud:</b> \n\nQaysi hududdansiz?\nViloyat nomi, Toshkent shahar yoki Respublikani kiriting.",
    'narx' : "<b>💰 Narxi:</b>\n\nTolov qilasizmi yoki Tekinmi?\nKerak bo`lsa, Summani kiriting?",
    'kasbi' : "<b>👨🏻‍💻 Kasbi: </b>\n\nIshlaysizmi yoki o`qiysizmi?\nMasalan, Talaba",
    'vaqt' : "<b>🕰 Murojaat qilish vaqti:</b>\n\n Qaysi vaqtda murojaat qilish mumkin?\nMasalan, 9:00 - 18:00",
    'maqsad' : "<b>🔎 Maqsad: </b>\n\nMaqsadingizni qisqacha yozib qoldiring.",
    #hodim kerak
    'idora' : "<b>🎓 Idora nomi?</b>",
    'masul' : "<b>✍️Mas'ul ism sharifi?</b>",
    'ish vaqti' : "<b>🕰 Ish vaqtini kiriting?</b>",
    'maosh' : "<b>💰 Maoshni kiriting?</b>",
    'malumot' : "<b>‼️ Qo`shimcha ma`lumotlar?</b>",
}


forms_all = {
  1 : forms['ism'],
  2 : forms['yosh'],
  3 : forms['texnologiya'],
  4 : forms['aloqa'],
  5 : forms['hudud'],
  6 : forms['narx'],
  7 : forms['kasbi'],
  8 : forms['vaqt'],
  9 : forms['maqsad']
}

form_hodim = {
  1 : forms['idora'],
  2 : forms['texnologiya'],
  3 : forms['aloqa'],
  4 : forms['hudud'],
  5 : forms['masul'],
  6 : forms['vaqt'],
  7 : forms['ish vaqti'],
  8 : forms['maosh'],
  9 : forms['malumot']
}

text = """ topish uchun ariza berish</b>

Hozir sizga bir necha savollar beriladi. 
Har biriga javob bering. 
Oxirida agar hammasi to`g`ri bo`lsa, <b> HA</b> tugmasini bosing va arizangiz Adminga yuboriladi.
"""
buttons = [
        [KeyboardButton(text='Hodim kerak'), KeyboardButton(text='Ish joyi kerak')],
        [KeyboardButton(text='Ustoz kerak'), KeyboardButton(text='Shogird kerak')],
        [KeyboardButton(text='Sherik kerak'), KeyboardButton(text='O\'quv kursi')]
    ]

menu_buttons = ReplyKeyboardMarkup(buttons, resize_keyboard=True,  one_time_keyboard=True)