"""
INF1103 Week 8 - File handling
"""
import json

from product import Product

# Global Constant
INVENTORY_FILE = "inventory.json"


def load_inventory():
    products = []
    status = "not_found"

    try:
        with open(INVENTORY_FILE, "r") as file:
            data = json.load(file)

        if not isinstance(data, list):
            return [], "error"

        for item in data:
            product = Product(
                item["id"],
                item["name"],
                float(item["price"]),
                int(item["stock"])
            )
            products.append(product)
        status = "loaded"

    except FileNotFoundError:
        products = []
        status = "not_found"
    except (json.JSONDecodeError, KeyError, TypeError, ValueError):
        products = []
        status = "error"

    return products, status


def save_inventory(products):
    data = []
    for product in products:
        data.append({
            "id": product.get_product_id(),
            "name": product.get_name(),
            "price": product.get_price(),
            "stock": product.get_stock()
        })

    with open(INVENTORY_FILE, "w") as file:
        json.dump(data, file, indent=4)