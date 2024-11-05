import base64

def decode_base64_from_file(file_path):
    
    with open(file_path, 'r') as file:
        encoded_string = file.read()

    decoded_bytes = base64.b64decode(encoded_string)

    try:
        decoded_string = decoded_bytes.decode('utf-8')
        return decoded_string
    except UnicodeDecodeError:
        return decoded_bytes

file_path = '../nmapString.txt' 
decoded_result = decode_base64_from_file(file_path)

byte_data = bytes.fromhex(decoded_result)
decoded_str = byte_data.decode('ISO-8859-1')

with open("nmapResult.txt", 'w') as file:
    file.write(decoded_str)