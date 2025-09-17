"""
Протестируйте классы из модуля homework/models.py
"""

import pytest
from models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def cart():
    cart = Cart()
    return cart


@pytest.fixture
def cart_with_product(product):
    cart = Cart()
    cart.add_product(product, 10)
    return cart


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(999)
        assert product.check_quantity(1000)
        assert not product.check_quantity(1001)

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        buy_count = 2
        expected_quantity = product.quantity - buy_count
        product.buy(buy_count)
        assert expected_quantity == product.quantity

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        buy_count = 2000
        with pytest.raises(ValueError):
            assert product.buy(buy_count)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product_to_empty_cart(self, cart, product):
        buy_count = 500
        cart.add_product(product, buy_count)
        assert product in cart.products
        assert cart.products[product] == buy_count

    def test_remove_product(self, cart_with_product, product):
        cart_with_product.remove_product(product, 1)
        assert cart_with_product.products[product] == 9
        cart_with_product.remove_product(product, 2)
        assert cart_with_product.products[product] == 7

    def test_remove_whole_product(self, cart_with_product, product):
        cart_with_product.remove_product(product)
        assert product not in cart_with_product.products

    def test_remove_product_exceed(self, cart_with_product, product):
        cart_with_product.remove_product(product, 10)
        assert product not in cart_with_product.products

    def test_clear_cart(self, cart_with_product, product):
        cart_with_product.clear()
        assert cart_with_product.products == {}

    def test_get_total_price(self, cart_with_product, product):
        expected_total_price = cart_with_product.get_total_price()
        assert expected_total_price == 1000

    def test_buy(self, cart_with_product, product):
        cart_with_product.buy()
        assert cart_with_product.products == {}
