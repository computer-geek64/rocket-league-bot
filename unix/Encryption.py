# Encryption.py
# Ashish D'Souza
# September 8th, 2018

from Crypto.Cipher import AES
import base64


def encrypt(text, passphrase):
    IV = "1234567890123456"
    aes = AES.new(passphrase, AES.MODE_CFB, IV)
    return base64.b64encode(aes.encrypt(text)).decode("ascii")


def decrypt(cipher_text, passphrase):
    IV = "1234567890123456"
    aes = AES.new(passphrase, AES.MODE_CFB, IV)
    return aes.decrypt(base64.b64decode(cipher_text)).decode("ascii")
