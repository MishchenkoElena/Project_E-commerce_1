from unittest.mock import patch

import pytest

from src.products import Product


def test_product_init(product1: Product):
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.price == 180000.0
    assert product1.quantity == 5


def test_category_init(category1, category2, category3):
    assert category1.name == "Смартфоны"
    assert (
            category2.description
            == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert len(category1.products_in_list) == 3
    assert category1.category_count == 3
    assert category2.category_count == 3
    assert category3.category_count == 3
    assert len(category3.products) == 0


def test_add_new_product():
    products_list = []
    new_product_data = {
        "name": "Samsung Galaxy S24 Ultra",
        "description": "512GB, Серый цвет, 200MP камера",
        "price": 250000.0,
        "quantity": 10,
    }
    product = Product.new_product(new_product_data, products_list)
    assert product.name == "Samsung Galaxy S24 Ultra"
    assert product.description == "512GB, Серый цвет, 200MP камера"
    assert product.price == 250000.0
    assert product.quantity == 10


def test_product_price_incorrect(capsys, product1: Product):
    capsys.readouterr()
    product1.price = -500
    captured = capsys.readouterr()
    assert captured.out == "Цена не должна быть нулевая или отрицательная\n"
    assert product1.price
    product1.price = 0
    assert captured.out == "Цена не должна быть нулевая или отрицательная\n"
    assert product1.price


def test_product_price_setter_yes(capsys, product1: Product):
    new_price = 100000.0
    with patch("builtins.input", side_effect=["y"]):
        product1.price = new_price
        captured = capsys.readouterr()
        assert captured.out.split("\n")[-1] == ""
        assert product1.price == 100000.0


def test_product_str(product1):
    assert str(product1) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_category_str(category1):
    assert str(category1) == "Смартфоны, количество продуктов: 27 шт."


def test_product_add(product1, product2):
    assert product1 + product2 == 2580000.0


def test_product_add_incorrect_type(product1):
    with pytest.raises(TypeError):
        product1 + "Строка"

    with pytest.raises(TypeError):
        product1 + 42

    with pytest.raises(TypeError):
        product1 + None


def test_product_iterator(product_iterator):
    iter(product_iterator)
    assert product_iterator.index == 0
    assert next(product_iterator).name == "Samsung Galaxy S23 Ultra"
    assert next(product_iterator).name == "Xiaomi Redmi Note 11"
    assert next(product_iterator).name == "Iphone 15"

    with pytest.raises(StopIteration):
        next(product_iterator)


def test_add_product_error(category1):
    with pytest.raises(TypeError):
        category1.add_product(1)

    with pytest.raises(TypeError):
        category1.add_product("Not a product")

    with pytest.raises(TypeError):
        category1.add_product([1, 2, 3])
