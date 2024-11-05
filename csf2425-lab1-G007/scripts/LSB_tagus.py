from PIL import Image

def extract_lsb_rgb(image_path, output_rgb):
    
    img = Image.open(image_path) 

    f_rgb = open(output_rgb, "w")

    for i in range(1100):
        if i == 0:
            continue
        col = i - 1
        for row in range(i):
            r, g, b = img.getpixel((col, row))
            
            lsb_r = add_5_bits(bin(r & 31)[2:])
            lsb_g = add_5_bits(bin(g & 31)[2:])
            lsb_b = add_5_bits(bin(b & 31)[2:])


            f_rgb.write(f'{lsb_r}{lsb_g}{lsb_b}')

            col = col - 1
        

    f_rgb.close()


def convert_to_readable(text_path):

    with open(text_path, 'r') as file:
        binary = file.read().strip()

    byte_data = [binary[i:i+8] for i in range(0, len(binary), 8)]
    byte_values = [int(b, 2) for b in byte_data]
    binary_data = bytearray(byte_values)

    with open(text_path, 'wb') as file:
        file.write(binary_data)

def add_5_bits(lsb):
    if len(lsb) == 1:
        lsb = "0000" + lsb
    if len(lsb) == 2:
        lsb = "000" + lsb
    if len(lsb) == 3:
        lsb = "00" + lsb
    if len(lsb) == 4:
        lsb = "0" + lsb
    return lsb

if __name__ == '__main__':

    image_path = '../tagus.png'  
    output_rgb = 'output_rgb_tagus_diagonal' 
    extract_lsb_rgb(image_path, output_rgb)
    convert_to_readable(output_rgb)
    

