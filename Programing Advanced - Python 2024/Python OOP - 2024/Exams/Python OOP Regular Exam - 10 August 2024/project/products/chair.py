from project.products.base_product import BaseProduct


class Chair(BaseProduct):

    def __init__(self, model: str, price: float):
        super().__init__(model, price, material="Wood", sub_type="Furniture")

    def discount(self):
        self.price *= 0.90
