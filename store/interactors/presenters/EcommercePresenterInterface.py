from abc import ABC
from abc import abstractmethod


class EcommercePresenterInterface(ABC):

    @abstractmethod
    def raise_invalid_category_exception(self):
        pass

    @abstractmethod
    def get_product_details_response(self):
        pass


