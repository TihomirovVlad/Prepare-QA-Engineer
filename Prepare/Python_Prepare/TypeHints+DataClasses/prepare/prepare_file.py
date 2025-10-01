from dataclasses import dataclass
from typing import Optional
from enum import Enum

class PaymentStatus(Enum):
    PENDING = "pending"
    SUCCESS = "success"
    FAILED = "failed"

@dataclass
class PaymentData:
    amount: float
    currency: str = "RUB"
    status: PaymentStatus = PaymentStatus.PENDING
    idempotency_key: Optional[str] = None

#Основа
#Type Hints - IDE подсказывает подсказки, ловим ошибки ДО запуска
#DataClasses - автоматически генерирует init, repr
#Enum - ограничивываем возможные значения статусов
#Optional - поле может быть None

#Плюсы
# Самодокументирующийся код
# Меньше runtime ошибок
# Легко рефакторить