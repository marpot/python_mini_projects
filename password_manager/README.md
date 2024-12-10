```markdown
# Password Manager with Encryption

A secure password manager written in Python that encrypts stored passwords using the `cryptography` library. This script allows you to securely store and view account credentials by encrypting passwords with a master password and a stored key.

---

## Features

- **Encryption**: Passwords are encrypted using a combination of a master password and a key file for enhanced security.
- **Master Password**: Protects access to your saved credentials.
- **Secure Storage**: Credentials are stored in an encrypted format in a local file (`passwords.txt`).
- **User-Friendly**: Easily add new credentials or view existing ones.
- **Error Handling**: Handles invalid formats and missing files gracefully.

---

## How It Works

1. **Key Management**:
   - A key file (`key.key`) is used to encrypt and decrypt passwords.
   - The script combines the master password and key file to generate a unique encryption key.

2. **Password Encryption**:
   - New passwords are encrypted and stored in the `passwords.txt` file.
   - Each password is tied to an account name.

3. **Password Decryption**:
   - When viewing passwords, they are decrypted using the same master password and key file.

---

## Setup

### Prerequisites

- **Python 3.6+** installed on your system.
- Install the `cryptography` library:
  ```bash
  pip install cryptography
  ```

### Generating a Key File

- Uncomment and run the `write_key` function in the script to generate a key file:
  ```python
  def write_key():
      key = Fernet.generate_key()
      with open("key.key", "wb") as key_file:
          key_file.write(key)
  ```

- Save the generated `key.key` file securely. It is required for encryption and decryption.

---

## Usage

1. **Run the Script**:
   ```bash
   python password_manager.py
   ```

2. **Enter Your Master Password**:
   - When prompted, provide your master password.

3. **Choose an Action**:
   - `add`: Add a new account and encrypted password.
   - `view`: View stored account credentials.
   - `q`: Quit the application.

### Example

#### Adding a Password
```plaintext
Would you like to add a new password or view existing ones? (view, add), press q to quit: add
Account Name: Gmail
Password: mySecureP@ssw0rd
```

#### Viewing Passwords
```plaintext
Would you like to add a new password or view existing ones? (view, add), press q to quit: view
User: Gmail | Password: mySecureP@ssw0rd
```

---

## File Details

- **`key.key`**: Stores the encryption key.
- **`passwords.txt`**: Stores encrypted account credentials in the format:
  ```
  account_name|encrypted_password
  ```

---

## Notes

- **Important**: Losing the `key.key` file or forgetting the master password will make decryption impossible.
- **Security Tip**: Keep `key.key` and `passwords.txt` in a secure location.
- **Do Not Share**: Never share your master password or key file.

---

## Dependencies

- [cryptography](https://cryptography.io/)

---

## License

This project is licensed under the MIT License.

---

Enjoy managing your passwords securely! 🔒
```