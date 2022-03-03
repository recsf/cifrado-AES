from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex

key = 'abcdefghigklmnor'


def pad(text):
    text = str(text)
    while len(text) % 16 != 0:
        text += ' '
    return text


def encriptar(archivo, clave):
    aes = AES.new(clave.encode(), AES.MODE_ECB)
    with open(archivo, 'r') as file:
        archivo_info = file.read()
    encrypted_text = aes.encrypt(pad(archivo_info).encode())
    encrypted_text_hex = b2a_hex(encrypted_text)
    with open(archivo, 'wb') as file:
        file.write(encrypted_text_hex)


def desencriptar(archivo, clave):
    aes = AES.new(clave.encode(), AES.MODE_ECB)
    with open(archivo, 'r') as file:
        encrypted = file.read()
    de = str(aes.decrypt(a2b_hex(encrypted)), encoding='utf-8', errors="ignore")
    with open(archivo, 'w') as file:
        file.write(de)


path = 'archivo.txt'

opc = int(input("Presione\n1)Encriptar\n2)Desencriptar: "))

if opc == 1:
    encriptar(path, key)
elif opc == 2:
    desencriptar(path, key)
else:
    print('Hasta Luego')
