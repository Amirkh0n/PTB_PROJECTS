import config as conf 


def inlines(update, context):
    query = update.callback_query
    user_id = query.from_user.id 
    
    if user_id == conf.ADMIN_ID:
        query_list = query.data.split('_')
        
        if query_list[0]=='post':
            context.bot.send_message(
                chat_id = conf.CHANNEL_ID,
                text = conf.orders.get('1'),
                parse_mode = "HTML"
            )
            query.edit_message_text(
                text = 'Muvaffaqiyatli bajarildi!!!'
            )
            
        elif query_list[0]=='del':
            pass
    