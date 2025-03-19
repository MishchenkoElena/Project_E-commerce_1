import json
import os

from src.products import Category, Product


def read_json(path: str) -> dict:
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as file:
        data = json.load(file)
    return data


def create_objects_from_json(data):
    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))

    return categories


if __name__ == "__main__":
    data_json = read_json("../data/products.json")
    categories_data = create_objects_from_json(data_json)

    print(categories_data[1].name)
    print(categories_data[1].products)
