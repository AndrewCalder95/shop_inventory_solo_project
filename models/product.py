class Product:
    def __init__(self, name, description, in_stock, purchase_cost, selling_price, manufacturer, id = None):
        self.id = id
        self.name = name
        self.description = description
        self.in_stock = in_stock
        self.purchase_cost = purchase_cost
        self.selling_price = selling_price
        self.manufacturer = manufacturer