import os
from pathlib import Path
from helpers import generate_uid

NEW_USER = {
    "first_name": "Дарья",
    "last_name": "Иванова",
    "username": f"testuser_{generate_uid()}",
    "email": f"test_{generate_uid()}@mail.com",
    "password": "rYH3K/oAFqg<",
}

EXISTING_USER = {
    "email": os.getenv("EXISTING_USER_EMAIL", "Kasper"),
    "password": os.getenv("EXISTING_USER_PASSWORD", "V8CcgkC5Vr#G"),
}

NEW_RECIPE = {
    "title": f"Омлет {generate_uid()}",
    "description": "Классический пышный омлет",
    "cooking_time": 10,
    "ingredients": [
        {"name": "яйца", "amount": "180"},
        {"name": "молоко", "amount": "150"},
        {"name": "сливочное масло", "amount": "10"},
        {"name": "соль", "amount": "1"},
    ],
}

# Путь до изображения
TEST_IMAGE = Path(__file__).parent / "assets" / "omelette.png"
