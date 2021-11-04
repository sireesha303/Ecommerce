from storages import EcommerceStorageInterface
from presenters import EcommercePresenterInterface
from typing import Dict
from eCommerce.store.exceptions.exceptions import *
from eCommerce.store.dtos.dtos import *


class CreateProductInteractor:
    def __init__(self,
                 storage: EcommerceStorageInterface):
        self.storage = storage

    def create_product_wrapper(self, user_id: int, product_data: Dict,
                               presenter: EcommercePresenterInterface):
        try:
            product_details_dto = self.create_product(user_id, product_data)
        except InvalidCategory:
            presenter.raise_invalid_category_exception()

        response = presenter.get_product_details_response(
            product_details_dto)

        return response

    def create_product(self, user_id: int, product_data: dict):

        category_id = product_data['category_id']
        is_category_not_existed = not self.storage.validate_category_id(
            category_id=category_id)

        if is_category_not_existed:
            raise InvalidCategory()

        product_dto = self._convert_product_data_to_dto(product_data)

        product_details_dto = self.storage.create_product(
            user_id=user_id,
            product_dto=product_dto
        )
        return product_details_dto

    @staticmethod
    def _convert_product_data_to_dto(product_data):
        product_dto = ProductDto(
            name=product_data.get('name'),
            price=product_data('price'),
            category_id=product_data.get('category_id'),
            description=product_data.get('description')
        )
        return product_dto
