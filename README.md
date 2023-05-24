# SecureCrypt - Tool to encrypt or decrypt all file formats



![SecureCrypt](https://raw.githubusercontent.com/ilhamrzr/SecureCrypt/main/static/SecureCrypt.png)

## How to install

> Note: Tested on Windows WSL/Linux/Termux

### Installation on Windows WSL/Linux

```
$ git clone https://github.com/ilhamrzr/SecureCrypt
$ cd SecureCrypt
$ python3 -m venv env
$ source env/bin/activate
$ pip3 install -r requirements.txt
$ python3 main.py
```

### Installation on Termux

> Note: Tested with python version 3.11.2 and pip version 23.0.1

1. pkg update && pkg upgrade

2. pkg install python-cryptography

3. clone this repo

   ``````
   git clone https://github.com/ilhamrzr/SecureCrypt
   ``````

4. change directory

   ``````
   cd SecureCrypt
   ``````

5. edit file `requirements.txt` and remove `cryptography==40.0.2`

6. install `requirements.txt`

   ``````
   pip install -r requirements.txt
   ``````

7. run this tool

   ``````
   python main.py
   ``````

### How to use

[https://youtu.be/WsBtD41f6LU](https://youtu.be/WsBtD41f6LU)
