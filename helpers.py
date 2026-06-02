import uuid

def generate_uid() -> str:
    """Генерирует уникальный суффикс для тестовых данных."""
    return uuid.uuid4().hex[:8]
