from dataclasses import dataclass
from typing import Optional, List


@dataclass
class CustomerDto:
    """
    User DTO
    """
    user_id: int
    first_name: str
    last_name: str
    phone: str
    email: str
    password: str


@dataclass
class ProductDto:
    """
    Product DTO
    """
    name: str
    price: int
    category_id: int
    description: str
    # image = models.ImageField(upload_to='uploads/products/')
