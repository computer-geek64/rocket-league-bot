# Encryption.py
# Ashish D'Souza
# September 9th, 2018

from Crypto.Cipher import AES
import base64


def encrypt(text, passphrase):
    IV = "1234567890123456"
    aes = AES.new(str.encode(passphrase), AES.MODE_CFB, str.encode(IV))
    return base64.b64encode(aes.encrypt(str.encode(text))).decode("ascii")


def decrypt(cipher_text, passphrase):
    IV = "1234567890123456"
    aes = AES.new(str.encode(passphrase), AES.MODE_CFB, str.encode(IV))
    return aes.decrypt(base64.b64decode(cipher_text)).decode("ascii")
