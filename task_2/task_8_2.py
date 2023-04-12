import json


def write_order_to_json(item, quantity, price, buyer, date):
    data = {
        'item': item,
        'quantity': quantity,
        'price': price,
        'buyer': buyer,
        'date': date,
    }
    with open('orders.json', 'w', encoding='UTF-8') as write_json:
        json.dump(data, write_json, indent=4)


write_order_to_json(
    item=['Toys', 'Books', 'Dishes'],
    quantity=[5, 4, 10],
    price=[100.00, 10.00, 50.50],
    buyer=['Grekov Maksim'],
    date=['12.04.23'])
