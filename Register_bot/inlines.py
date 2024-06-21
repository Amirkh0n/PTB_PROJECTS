import config as conf
import functions as func 


def inlines(update, context):
    query =update.callback_query 
    user_id = query.from_user.id 
    data = conf.get_data(user_id)
    
    if query.data in ('uz', 'ru', 'en'):
        conf.data.get(str(user_id), {}).get('info', {})['lang'] = query.data
        if data.get('info', {}).get('contact'):
            context.bot.delete_message(chat_id = user_id,  message_id=query.message.message_id)
            func.main_menu(update, context, chat_id = user_id)
        else:
            conf.data.get(str(user_id), {})['step']= conf.steps['name']
            query.edit_message_text(text = 'Ismingizni kiriting:')
    
    elif query.data == "main_menu":
        context.bot.delete_message(chat_id = user_id,  message_id=query.message.message_id)
        func.main_menu(update, context, chat_id = user_id)
        