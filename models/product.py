class Product:
    def __init__(self, colour, wood, in_stock, purchase_cost, selling_price, product_series, id = None):
        self.id = id
        self.colour = colour
        self.wood = wood
        self.in_stock = in_stock
        self.purchase_cost = purchase_cost
        self.selling_price = selling_price
        self.product_series = product_series