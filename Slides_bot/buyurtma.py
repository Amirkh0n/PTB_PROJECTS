import re
from telegram import ReplyKeyboardRemove
from menu import main_menu, send_my_info, product
from config import data, save_data, sent_to_admin, KARTA 

def buyurtma(update, context):
    user_id = update.message.from_user.id 
    message = update.message.text
    summalar = {"Maqola": '30_000', 'Tezis': '20_000', 'Slayd': '5_000', 'Kurs ishi': '35_000'}
    if message in ["Maqola", 'Tezis', 'Slayd', 'Kurs ishi']:
        data[str(user_id)]['summalar']. append(summalar[message])
        data[str(user_id)]['buyurtmalar']. append(message)
        save_data(data)
        context.user_data['step'] = 8
        update.message.reply_text(
            text=f"Fan nomini kiriting:",
            reply_markup=ReplyKeyboardRemove()
        )
    else:
        product(update, context)


def fan_nomi(update, context):
    user_id = update.message.from_user.id 
    message = update.message.text
    
    data[str(user_id)]['fanlar']. append(message)
    save_data(data)
    context.user_data['step'] = 9
    update.message.reply_text(
        text=f"{data.get(str(user_id),  {}).get('buyurtmalar',  [0])[-1]} mavzusini kiriting:",
        reply_markup=ReplyKeyboardRemove()
    )
    

def mavzu(update, context):
    message =update.message.text 
    user_id = update.message.from_user.id
    data[str(user_id)]['mavzular']. append(message)
    save_data(data)
    update.message.reply_text(text=f"Buyurtmangiz qabul qilindi. Buyurtmangizni tayyorlashimiz uchun quyidagi karta raqamiga {data.get(str(user_id), {}).get('summalar', [0])[-1]} so'm to'lov qilib, chekini screenshot qilib rasm ko'rinishida jo'natishingiz kerak bo'ladi!!!\n<pre>{KARTA}</pre>(Fazliddin Turg’unboev)\n\nBuyurtmani bekor qilish uchun👉 /start 👈ni bosing! ", parse_mode="HTML")
    
    context.user_data['step'] = 10
    #main_menu(update, context, user_id)
#    
#    date=data.get(str(user_id), {})
#    datas={
#        'id': user_id, 
#        'name': date.get('info', {}).get('name'),
#        'contact': date.get('info', {}).get('contact'),
#        'univercity': date.get('info', {}).get('univercity'),
#        'buyurtma': date.get('buyurtmalar', [0])[-1],
#        'fan': date.get('fanlar', [0])[-1],
#        'mavzu': date.get('mavzular', [0])[-1]
#    }
#    sent_to_admin(update, context, datas)


def photo_handler(update, context):
    if context.user_data.get('step')==10:
        photo =update.message.photo[-1]
        user_id = update.message.from_user.id
        date=data.get(str(user_id), {})
        datas={
            'id': user_id, 
            'name': date.get('info', {}).get('name'),
            'contact': date.get('info', {}).get('contact'),
            'univercity': date.get('info', {}).get('univercity'),
            'buyurtma': date.get('buyurtmalar', [0])[-1],
            'fan': date.get('fanlar', [0])[-1],
            'mavzu': date.get('mavzular', [0])[-1]
        }
        sent_to_admin(update, context, photo, datas)
        main_menu(update, context, user_id)