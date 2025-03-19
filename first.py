
import hashlib

def hash_password(password):
    """Хешує пароль за допомогою MD5."""
    return hashlib.md5(password.encode()).hexdigest()

def verify_password(stored_password, entered_password):
    """Перевіряє, чи відповідає введений пароль збереженому хешу."""
    return hash_password(entered_password) == stored_password

# Словник користувачів (логін: (хеш пароля, ПІБ))
users = {
    "john_doe": (hash_password("password123"), "Джон Доу"),
    "jane_smith": (hash_password("securepass"), "Джейн Сміт"),
    "peter_jones": (hash_password("mysecret"), "Пітер Джонс"),
}

def login():
    """Функція для входу користувача."""
    username = input("Введіть логін: ")
    password = input("Введіть пароль: ")

    if username in users:
        stored_password, full_name = users[username]
        if verify_password(stored_password, password):
            print(f"Вітаємо, {full_name}!")
            return True
        else:
            print("Неправильний пароль.")
            return False
    else:
        print("Користувача не знайдено.")
        return False

# Приклад використання
login()
print(users)
