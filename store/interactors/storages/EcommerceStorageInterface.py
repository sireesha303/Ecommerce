from abc import ABC
from abc import abstractmethod
from eCommerce.store.dtos.dtos import *


class EcommerceStorageInterface(ABC):

    @abstractmethod
    def validate_category_id(self, category_id: int) -> bool:
        pass

    @abstractmethod
    def create_product(self, user_id: int, product_dto: ProductDto) -> str:
        pass


