#!/usr/bin/env python3

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from termcolor import colored
import base64
import getpass
import os

banner = r'''
  ____                            ____                  _   
 / ___|  ___  ___ _   _ _ __ ___ / ___|_ __ _   _ _ __ | |_ 
 \___ \ / _ \/ __| | | | '__/ _ \ |   | '__| | | | '_ \| __|
  ___) |  __/ (__| |_| | | |  __/ |___| |  | |_| | |_) | |_ 
 |____/ \___|\___|\__,_|_|  \___|\____|_|   \__, | .__/ \__|
            # Coded by Ilham | @ilhamrzr    |___/|_|        
'''

if os.name == 'nt':
    os.system('color')


def generate_fernet_key(password, salt=None):
    if salt is None:
        salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    return key, salt


def encrypt_file(file_path, password):
    key, salt = generate_fernet_key(password)

    with open(file_path, 'rb') as file:
        data = file.read()

    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)

    with open(file_path, 'wb') as file:
        file.write(b"ENC!" + salt + encrypted_data)


def decrypt_file(file_path, password):
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()

    if not encrypted_data.startswith(b"ENC!"):
        print('[{0}] This is not an encrypted file.'.format(colored('x', 'red')))
        return False
    
    encrypted_data = encrypted_data[4:]
    salt = encrypted_data[:16]
    encrypted_data = encrypted_data[16:]

    key, _ = generate_fernet_key(password, salt)

    try:
        fernet = Fernet(key)
        decrypted_data = fernet.decrypt(encrypted_data)

        with open(file_path, 'wb') as file:
            file.write(decrypted_data)

        print('[{0}] Files are decrypted!!\n'.format(colored('+', 'green')))
        return True

    except:
        print('[{0}] Wrong password. Retrying..'.format(colored('x', 'red')))
        return False


if __name__ == '__main__':
    while True:
        print(colored(banner, 'light_grey', attrs=['bold']))
        print("Select option:\n1. {0}\n2. {1}\n3. {2}\n".format(colored('Encrypt File', 'red'), colored(
            'Decrypt File', 'green'), colored('Exit', 'yellow')))
        operation = input(
            "Choose (1/2/3): ")

        if operation == '1':
            file_path = input("Your file path: ")
            password = getpass.getpass("Your key: ").encode()
            encrypt_file(file_path, password)

            print('[{0}] Encrypted file!!\n'.format(
                colored('+', 'green')))
            break
        elif operation == '2':
            file_path = input("Your file path: ")
            password = getpass.getpass("Your key: ").encode()

            while not decrypt_file(file_path, password):
                password = getpass.getpass("Your key: ").encode()

            break
        elif operation == '3':
            break
        else:
            print(colored(
                '\nSelect 1. To encryption or 2. To decryption or 3. Exit\n', 'yellow'))
