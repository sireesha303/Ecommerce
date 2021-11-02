"""
 Functions To Create Objects for Products,Customer,Order and Category
"""

from .models import *
from datetime import date

class CustomerNotExisted(Exception):
    """
    Customer DoesNot Existed Exception handling
    """
    pass


def create_customer(first_name: str, last_name: str, email: str, phone: str, password: str):
    """
    :param first_name:
    :param last_name:
    :param email:
    :param phone:
    :param password:
    :return:
    """
    customer_object = Customer.objects.create(first_name=first_name, last_name=last_name,
                                              email=email, phone=phone, password=password)
    return customer_object


def create_category(name: str):
    """

    :param name:
    """
    category_object = Category.objects.create(name=name)
    return category_object


def add_product_to_category(name: str, price: int, category: Category, description: str):
    """
    :param name:
    :param price:
    :param category:
    :param description:
    :return:
    """
    product_object = Product.objects.create(name=name, price=price,
                                            category=category, description=description)
    return product_object


def place_the_order(product: Product, customer: Customer, quantity: int, price: int, address: str,
                    phone: str, date: date, status: str):
    """
    :param product:
    :param customer:
    :param quantity:
    :param price:
    :param address:
    :param phone:
    :param date:
    :param status:
    """
    order_object = Order.objects.create(product=product, customer=customer,
                                        quantity=quantity, price=price,
                                        address=address, phone=phone, date=date,
                                        status=status)
    return order_object


def get_all_categories():
    """

    :return:
    """
    category_objects = Category.objects.all()
    return [category_object for category_object in category_objects]


def get_customer_by_email(email: str):
    """
    :param email:
    :return:
    """
    try:
        customer_object = Customer.objects.get(email=email)
        return customer_object
    except Customer.DoesNotExist:
        raise CustomerNotExisted


def get_customer_orders(customer_id: int):
    """

    :param customer_id:
    :return:
    """
    customer_orders = Order.objects.filter(customer__id=customer_id)
    return [order for order in customer_orders]


def get_all_products():
    """

    :return:
    """
    product_objects = Product.objects.all()
    return [product_object for product_object in product_objects]


def get_products_by_category_id(category_id: int):
    """

    :param category_id:
    :return:
    """
    category_products_objects = Product.objects.filter(category__id=category_id)
    return [category_product for category_product in category_products_objects]