import config as conf 
import functions as func 
import register as reg


def messages(update, context):
    """This function responds to messages from the user!"""
    
    user_id =update.message.from_user.id
    message = update.message.text 
    step = conf.get_data(user_id).get('step', 0)
    
    if step == conf.steps['name']:
        reg.save_name(update, context)
    
    elif step ==conf.steps['contact']:
        reg.save_contact(update, context)
    
    elif message == "Ma'lumotlarim":
        func.send_my_info(update, context)
    
    elif step == conf.steps['main_menu']:
        func.main_menu(update, context, chat_id=user_id)
    
