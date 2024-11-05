import json
import os

def extract_chat_from_json(json_file, output_file):
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    with open(output_file, 'a', encoding='utf-8') as out_file:
        for message in data:
            content = message.get('content')
            author = message.get('author', {}).get('username')
            timestamp = message.get('timestamp')

            if author and content and timestamp:
                out_file.write(f"[{timestamp}] {author}: {content}\n")

folder_path = './messages/' 
output_file = './discord_messages.txt'

with open(output_file, 'w', encoding='utf-8'):
    pass

if os.path.isdir(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):
            extract_chat_from_json(os.path.join(folder_path, filename), output_file)
else:
    extract_chat_from_json(folder_path, output_file)

print(f"Chat data has been written to {output_file}")