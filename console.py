from models.product import Product
from models.product_series import Product_Series
from models.manufacturer import Manufacturer
import repositories.product_repository as product_repository
import repositories.product_series_repository as product_series_repository
import repositories.manufacturer_repository as manufacturer_repository

manufacturer1 = Manufacturer('British Drum Co.')
product_series2 = Product_Series("Stage", "Beginner", manufacturer1)
product1 = Product("Blue", "Birch", 20, 500, 600, product_series2)
manufacturer_repository.save(manufacturer1)
product_series_repository.save(product_series2)
product_repository.save(product1)


# product_series_repository.save(product_series1)
# manufacturer_repository.save(manufacturer1)

# pick = manufacturer_repository.select(2)
# print (pick)

# pick = product_series_repository.select(4)
# print (pick)

# product_repository.select_all()
