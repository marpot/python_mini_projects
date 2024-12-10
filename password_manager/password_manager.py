from cryptography.fernet import Fernet
import hashlib
import base64 
# Funkcja do zapisania klucza - możesz ją odkomentować, jeśli chcesz wygenerować nowy klucz
'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''

# Funkcja do załadowania klucza z pliku
def load_key():
    try:
        with open("key.key", "rb") as key_file:
            key = key_file.read()
        return key
    except FileNotFoundError:
        print("Plik z kluczem 'key.key' nie istnieje. Upewnij się, że go wygenerowałeś.")
        exit()

# Funkcja do generowania klucza na podstawie hasła głównego i klucza z pliku
def get_fernet_key(master_password, file_key):
    # Create a SHA-256 hash of the combined key
    hashed_master = hashlib.sha256(master_password.encode()).digest()
    combined_key = hashlib.sha256(file_key + hashed_master).digest()[:32]
    # Encode the 32-byte key into a URL-safe base64 string
    return Fernet(base64.urlsafe_b64encode(combined_key))


# Pobranie hasła głównego od użytkownika
master_pwd = input("What is the master password? ")
file_key = load_key()
fer = get_fernet_key(master_pwd, file_key)

# Funkcja do wyświetlania zapisanych danych
def view():
    try:
        with open('passwords.txt', 'r') as f:
            for line in f.readlines():
                data = line.strip()
                parts = data.split("|")
                
                # Sprawdzamy, czy linia zawiera dokładnie dwa elementy (user i password)
                if len(parts) == 2:
                    user, password = parts
                    try:
                        decrypted_password = fer.decrypt(password.encode()).decode()
                        print("User:", user, "| Password:", decrypted_password)
                    except Exception as decrypt_error:
                        print(f"Nie udało się odszyfrować hasła dla użytkownika '{user}': {decrypt_error}")
                else:
                    print("Nieprawidłowy format danych w linii:", data)
    except FileNotFoundError:
        print("Plik 'passwords.txt' nie istnieje.")
    except Exception as e:
        print("Wystąpił błąd podczas wyświetlania danych:", str(e))


# Funkcja do dodawania nowych danych
def add():
    name = input('Account Name: ').strip()
    password = input("Password: ").strip()
    if "|" in name or "|" in password:
        print("Nie można używać znaku '|' w nazwie użytkownika lub haśle.")
        return
    try:
        with open('passwords.txt', 'a') as f:
            encrypted_password = fer.encrypt(password.encode()).decode()
            f.write(name + "|" + encrypted_password + "\n")
    except Exception as e:
        print("Wystąpił błąd podczas zapisu danych:", str(e))

# Główna pętla programu
while True:
    mode = input("Would you like to add a new password or view existing ones? (view, add), press q to quit: ")
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
