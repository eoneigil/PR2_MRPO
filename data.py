from Repository.XMLRepository import XMLCategoryRepository, XMLProductRepository
from Models.Category import Categoryes
from Models.Product import Product

# fill_categories.py

category_repo = XMLCategoryRepository("categories.xml")

category_repo.add("Завтрак")
category_repo.add("Обед")
category_repo.add("Ужин")

print(category_repo.get_all())


def populate_products():
    product_repository = XMLProductRepository('products.xml')

    products = [
        Product(id=1, name="Яйца"),
        Product(id=2, name="Хлеб"),
        Product(id=3, name="Суп"),
        Product(id=4, name="Мясо"),
        Product(id=5, name="Рыба"),
        Product(id=6, name="Овощи")
    ]

    for product in products:
        if not product_repository.get_by_id(product.id):
            product_repository.add(product)
            print(f"Продукт '{product.name}' добавлен с id={product.id}.")
        else:
            print(f"Продукт с id={product.id} уже существует.")

if __name__ == "__main__":
    populate_products()
