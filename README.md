# 🔐 SecureCrypt - Secure & Easy File Encryption

<p align="center">
  <img src="https://raw.githubusercontent.com/ilhamrzr/SecureCrypt/main/static/SecureCrypt.png" alt="SecureCrypt" width="500">
</p>

SecureCrypt is a Python-based encryption tool that allows you to **securely encrypt and decrypt files** using **Fernet (AES-128-CBC)**. It utilizes **PBKDF2-HMAC-SHA256** for key derivation, ensuring **high security** to protect your files from unauthorized access.



## **🚀 Key Features**

✅ **Strong Encryption:** Uses **Fernet (AES-128-CBC)** for high-level security.

✅ **Supports Various File Types:** Works with **.txt, .pdf, .docx, .xlsx, .sh, .py, .php, .html, .mp3, .mp4, .zip, .exe**, and more.

✅ **Password Protection:** Files can only be decrypted with the correct password.

✅ **Encrypted File Detection:** Automatically detects whether a file is already encrypted.

✅ **Cross-Platform:** Runs on **Windows, Linux, and macOS** without additional modifications.

## **How to install**

> Note: Tested on Windows WSL/Linux/Termux

## **Installation on Windows WSL/Linux**

```
$ git clone https://github.com/ilhamrzr/SecureCrypt
$ cd SecureCrypt
$ python3 -m venv env
$ source env/bin/activate
$ pip3 install -r requirements.txt
$ python3 main.py
```

### 📲 Installation on Termux

> Note: Tested with python version 3.11.2 and pip version 23.0.1

1. Update & Upgrade Packages

   ```bash
   pkg update && pkg upgrade -y
   ```

2. Install Dependencies

   ```bash
   pkg install python python-pip python-cryptography openssl-tool
   ```

3. Clone the Repository

   ```bash
   git clone https://github.com/ilhamrzr/SecureCrypt
   ```

4. Navigate to the SecureCrypt folder

   ```
   cd SecureCrypt
   ```

5. Edit `requirements.txt`

   Since `cryptography==44.0.1` is not compatible with Termux, remove it from `requirements.txt`.
   You can manually edit the file or use this command to delete it automatically:

   ```bash
   sed -i '/cryptography==44.0.1/d' requirements.txt
   ```

6. After removing `cryptography`, install the remaining dependencies with:

   ```bash
   pip install --no-cache-dir -r requirements.txt
   ```

7. Run SecureCrypt

   ```bash
   python main.py
   ```

## **⚠️ Important Notes**

⚠ **Do not forget your password!** If lost, the file **cannot be decrypted**.

⚠ **Do not encrypt files that are currently in use** (e.g., an open Excel file).

⚠ **Make a backup before encrypting important files to avoid data loss.**

## How to use

[https://youtu.be/WsBtD41f6LU](https://youtu.be/WsBtD41f6LU)

## **🤝 Contribution**

We welcome contributions from everyone! To contribute, follow these steps:

1. **Fork** this repository
2. Create a **new branch** (`git checkout -b new-feature`)
3. Make your changes and **commit** (`git commit -m 'Add new feature'`)
4. **Push** to the branch (`git push origin new-feature`)
5. Create a **Pull Request**

We will review your contributions as soon as possible! 😊

### **📜 License**

This project is licensed under the **MIT License** – you are free to use it for personal and commercial purposes as long as you provide attribution to the original creator.
