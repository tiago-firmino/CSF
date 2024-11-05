from PIL import Image

def extract_lsb_rgb(image_path, output_rgb):

    img = Image.open(image_path) 

    f_rgb = open(output_rgb, "w")

    width, height = img.size


    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            
            lsb_r = add_3_bits(bin(r & 7)[2:])
            lsb_g = add_3_bits(bin(g & 7)[2:])
            lsb_b = add_3_bits(bin(b & 7)[2:])


            f_rgb.write(f'{lsb_r}{lsb_g}{lsb_b}')
        

    f_rgb.close()


def convert_to_readable(text_path):

    with open(text_path, 'r') as file:
        binary = file.read().strip()

    byte_data = [binary[i:i+8] for i in range(0, len(binary), 8)]
    byte_values = [int(b, 2) for b in byte_data]
    binary_data = bytearray(byte_values)

    with open(text_path, 'wb') as file:
        file.write(binary_data)

def add_3_bits(lsb):
    if len(lsb) == 1:
        lsb = "00" + lsb
    if len(lsb) == 2:
        lsb = "0" + lsb
    return lsb

if __name__ == '__main__':

    image_path = '../wallpaper.png' 
    output_rgb = 'output_wallpaper'
    extract_lsb_rgb(image_path, output_rgb)
    convert_to_readable(output_rgb)