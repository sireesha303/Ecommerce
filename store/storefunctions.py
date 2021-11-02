"""
 Functions To Create Objects for Products,Customer,Order and Category
"""

from .models import *


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
                    phone: str, date: str, status: str):
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

