import config as conf
import functions as func

def start_command(update, context):
    referral_code = context.args[0] if context.args else None
    user_id =update.message.from_user.id
    data = conf.get_data(user_id)
    update.message.reply_text("Assalomu aleykum, Botimizga Xush kelibsiz!")
    if referral_code:
        pass
    else:
        if data:
            if data.get('info', {}).get('lang'):
                if data.get('info', {}).get('contact'):
                    func.main_menu(update, context, user_id)
                else:
                    conf.data[str(user_id)]['step']=conf.steps['name']
                    update.message.reply_text("Ismingizni kiriting: ")
            else:
                func.edit_lang(update, context, user_id)
        else:
            conf.data[str(user_id)]={
                'info': {'forms': 0},
                'step': 1,
            }
            func.edit_lang(update, context, user_id)
            #update.message.reply_text("Ismingizni kiriting: ")
    
        