def convert_spaces_dots_to_binary(input_file_path, output_file_path):
    binary_output = ""

    with open(input_file_path, 'r') as input_file:
        input_string = input_file.read()

    for char in input_string:
        if char == ' ':
            binary_output += '0'
        elif char == '.':
            binary_output += '1'

    with open(output_file_path, 'w') as output_file:
        output_file.write(binary_output)

    print(f"Binary output written to {output_file_path}")

input_file_path = 'user_comments_concatenated.txt' #concatenation of all user comments in the order lactea.jpg + andromeda.png + cartwheel.tiff
output_file_path = 'output.txt'
convert_spaces_dots_to_binary(input_file_path, output_file_path)