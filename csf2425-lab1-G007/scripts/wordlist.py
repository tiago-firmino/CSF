import re

def clean_text(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()
    
    cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', text)

    words = cleaned_text.split()

    with open(output_file, 'w', encoding='utf-8') as file:
        for word in words:
            file.write(word + '\n')

    print(f'Cleaned words saved to {output_file}')

input_file = 'thrones.txt'  
output_file = 'wordlist.txt'

clean_text(input_file, output_file)