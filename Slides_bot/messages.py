import register
from menu import send_my_info, product
from buyurtma import buyurtma, mavzu, fan_nomi 

def message_handler(update, context):
    message = update.message.text
    step = context.user_data.get("step", 0)

    if step == 1:
        register.get_name(update, context)
    
    elif step == 4:
        register.get_univercity(update, context)
    elif step == 5:
        register.get_text_contact(update, context)
    elif step == 6:
        if message == "Ma'lumotlarim":
            send_my_info(update, context)
        elif message == "Buyurtma":
            product(update, context)
    elif step==7:
        buyurtma(update, context)
    elif step == 8:
        fan_nomi(update, context)
    elif step == 9:
        mavzu(update, context)
