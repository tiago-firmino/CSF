import re
from datetime import datetime

def extract_timestamp_and_message(line):
    match = re.match(r'(\[.*?\]) (.*)', line)
    if match:
        timestamp_str = match.group(1).strip('[]')
        message = match.group(2)
        
        timestamp = datetime.fromisoformat(timestamp_str)
        return timestamp, line
    return None, line

def sort_messages_by_timestamp(input_file, output_file):
    lines_with_timestamps = []
    
    with open(input_file, 'r', encoding='utf-8', errors='ignore') as file:
        for line in file:
            timestamp, original_line = extract_timestamp_and_message(line)
            if timestamp:
                lines_with_timestamps.append((timestamp, original_line))
    
    lines_with_timestamps.sort(key=lambda x: x[0])
    
    with open(output_file, 'w', encoding='utf-8', errors='ignore') as file:
        for _, sorted_line in lines_with_timestamps:
            file.write(sorted_line)

input_file = './past_discord_chat.txt'
output_file = './sorted_past_discord_chat.txt'

sort_messages_by_timestamp(input_file, output_file)

print(f"Messages sorted by timestamp and written to {output_file}")