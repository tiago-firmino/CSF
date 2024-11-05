from datetime import datetime, timedelta
import re

def apply_time_shift(input_file, output_file, hours_shift):
    time_shift = timedelta(hours=hours_shift)

    with open(input_file, 'r', encoding='utf-8', errors='ignore') as file:
        lines = file.readlines()

    with open(output_file, 'w', encoding='utf-8', errors='ignore') as out_file:
        for line in lines:
            match = re.match(r'(\[.*?\]) (.*)', line)
            if match:
                timestamp_str = match.group(1).strip('[]')
                message = match.group(2)

                try:
                    timestamp = datetime.fromisoformat(timestamp_str)
                    new_timestamp = timestamp + time_shift
                    new_timestamp_str = new_timestamp.isoformat() + "Z"  
                    out_file.write(f"[{new_timestamp_str}] {message}\n")
                except Exception as e:
                    print(f"Error parsing timestamp: {timestamp_str} - {e}")

input_file = './past_discord_chat.txt'
output_file = './modified_timestamps2.txt'

# Apply the time shift
apply_time_shift(input_file, output_file, hours_shift=-792)

print(f"Time shift applied and written to {output_file}")