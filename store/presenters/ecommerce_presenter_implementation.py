from abc import ABC
from abc import abstractmethod
from eCommerce.store.interactors.presenters.EcommercePresenterInterface import *
from eCommerce.store.exceptions.exception_messages import *

from django_swagger_utils.drf_server.exceptions\
    import NotFound

class EcommercePresenterInterfaceImplementation(EcommercePresenterInterface):

    @abstractmethod
    def raise_invalid_category_exception(self):
        raise NotFound(*INVALID_CATEGORY)

    @abstractmethod
    def get_product_details_response(self, product_object):
        return product_object

