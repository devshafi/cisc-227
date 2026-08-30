class Product:
    def __init__(self, id, name, sku, unit_price, quantity_on_hand):
        self.id = id
        self.name = name
        self.sku = sku
        self.unit_price = unit_price
        self.quantity_on_hand = quantity_on_hand

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "sku": self.sku,
            "unit_price": self.unit_price,
            "quantity_on_hand": self.quantity_on_hand,
        }
