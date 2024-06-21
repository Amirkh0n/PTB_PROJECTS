import json 

TOKEN = "BOT_TOKEN"

with open("data/data.json", 'r') as file:
    data = json.load(file)

def get_data(user_id):
    return data.get(str(user_id), {})
    
def save_data(data):
    with open('data/data.json', 'w') as file:
        json.dump(data, file, indent = 4)
        
steps={
    'main_menu' : 0,
    'name' : 1,
    'contact' : 2,
}

