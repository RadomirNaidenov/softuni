from project.stores.base_store import BaseStore


class FurnitureStore(BaseStore):
    INITIAL_CAPACITY = 50

    def __init__(self, name: str, location: str):
        super().__init__(name, location, self.INITIAL_CAPACITY)

    @property
    def store_type(self):
        return "FurnitureStore"

    def store_stats(self):
        products_summary = {}

        for product in self.products:
            if product.model not in products_summary:
                products_summary[product.model] = {"count": 0, "total_price": 0}
            products_summary[product.model]["count"] += 1
            products_summary[product.model]["total_price"] += product.price

        result = [f"Store: {self.name}, location: {self.location}, available capacity: {self.capacity}",
                  self.get_estimated_profit(),
                  "**Furniture for sale:"]

        for model in sorted(products_summary.keys()):
            count = products_summary[model]["count"]
            avg_price = products_summary[model]["total_price"] / count
            result.append(f"{model}: {count}pcs, average price: {avg_price:.2f}")

        return "\n".join(result).strip()







