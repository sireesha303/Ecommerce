from eCommerce.store.interactors.storages.EcommerceStorageInterface import *
from eCommerce.store.models import *
from eCommerce.store.dtos.dtos import *

class EcommerceStorageInterfaceImplementation(EcommerceStorageInterface):

    def validate_category_id(self, category_id: int) -> bool:
        is_category_existed = Category.objects.filter(id=category_id).exist()
        return is_category_existed

    def create_product(self, user_id: int, product_dto: ProductDto):
        project_obj = Product.objects.create(
            name=product_dto.name,
            price=product_dto.price,
            category_id=product_dto.category_id,
            description=product_dto.description,
            created_by_id=user_id
        )

        return project_obj
