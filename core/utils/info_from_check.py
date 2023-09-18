import requests
from core.settings import settings
import json
from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: float
    quantity: float


def receipt_request(data):
    json_items = json.loads(requests.post(url=settings.connects.api,
                                          data=data).text)["data"]["json"]["items"]
    items = []
    for json_item in json_items:
        items.append(Product(name=json_item["name"],
                             price=json_item["price"],
                             quantity=json_item["quantity"])
                     )
    return items
