import openai
from config import API_KEY 

openai.api_key = API_KEY

#messages = [{"role": "system", "content": "You are an intelligent assistant."}]

def gpt_chat(message, messages):
    if message:
        messages.append({"role": "user", "content": message})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages = messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply 
    else:
        return "*XATOLIK*"

def messagess(update, context):
    isGPT = context.user_data.get("isGPT", False)
    if isGPT:
        messages = context.user_data.get( "messages", [{"role": "system", "content": "You are an intelligent assistant."}])
        message=update.message.text
        text=gpt_chat(message, messages)
        context.user_data["messages"]=messages
    else:
        text= "Xatolik bor"
    update.message.reply_text(text=text, parse_mode="Markdown")