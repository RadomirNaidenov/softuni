from project.product import Product


class ProductRepository:

    def __init__(self):
        self.products: list[Product] = []

    def add(self, product: Product) -> None:
        self.products.append(product)

    def find(self, product_name: str):
        for product in self.products:
            if product.name == product_name:
                return product

    def remove(self, product_name):
        current_product = self.find(product_name)
        if current_product:
            self.products.remove(current_product)

    def __repr__(self):
        output = []
        for product in self.products:
            output.append(f"{product.name}: {product.quantity}")

        return "\n".join(output)









