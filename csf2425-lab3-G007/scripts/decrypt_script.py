import base64
import urllib.parse
from Crypto.Cipher import AES
import hashlib

password = "CZN.pjp0paz3jej5jgajcj!hzx3yzp2DTB1hgy"

def decrypt(enc, password):
    parsed_data = urllib.parse.parse_qs(enc)

    enc = list(parsed_data.keys())[0].decode('utf-8')

    print(enc)
    # The value is a list, so get the first element

    private_key = hashlib.sha256(password.encode("utf-8")).digest()
    enc = base64.b64decode(enc)
    iv = enc[:16]
    cipher = AES.new(private_key, AES.MODE_CFB, iv)
    return cipher.decrypt(enc[16:])

def main():
    inputFile = "./first_file.txt"  # Input file containing the encrypted data
    outFile = "./first_output.txt"   # Output file for decrypted data
    
    # Read the encrypted data from the input file
    with open(inputFile, "rb") as infile:
        encrypted_data = infile.read()  # Read the entire file content
    
    # Decrypt the data
    decrypted_file = decrypt(encrypted_data, password)

    print(decrypted_file)

    # Write the decrypted data to the output file
    with open(outFile, "wb") as outfile:
        outfile.write(decrypted_file)

if __name__ == "__main__":
    main()