class Product:
    """
    Класс продукта
    """

    name: str
    price: float
    description: str
    quantity: int

    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

    def check_quantity(self, quantity) -> bool:
        """
        TODO Верните True если количество продукта больше или равно запрашиваемому
            и False в обратном случае
        """
        return self.quantity >= quantity

    # '''Код ниже для проверки метода check_quantity'''
    # p = Product(name='Laptop', price=1500, description='Gaming', quantity=10)
    # print(p.check_quantity(1))

    def buy(self, quantity):
        """
        TODO реализуйте метод покупки
            Проверьте количество продукта используя метод check_quantity
            Если продуктов не хватает, то выбросите исключение ValueError
        """
        if not self.check_quantity(quantity):
            raise ValueError(
                f'Not enough quantity: requested {quantity}, available {self.quantity}'
            )
        self.quantity = self.quantity - quantity

    # '''Код ниже для проверки метода buy'''
    # p = Product(name='Laptop', price=1500, description='Gaming', quantity=10)
    # p.buy(3)
    # print(p.quantity)
    # p.buy(8)
    # print(p.quantity)

    def __hash__(self):
        return hash(self.name + self.description)


# '''Код ниже для проверки метода __hash__'''
# p = Product(name='Laptop', price=1500, description='Gaming', quantity=10)
# print(p.__hash__())
# p1 = Product(name='Computer', price=1500, description='Gaming', quantity=10)
# print(p1.__hash__())


class Cart:
    """
    Класс корзины. В нем хранятся продукты, которые пользователь хочет купить.
    TODO реализуйте все методы класса
    """

    # Словарь продуктов и их количество в корзине
    products: dict[Product, int]

    def __init__(self):
        # По-умолчанию корзина пустая
        self.products = {}

    def add_product(self, product: Product, buy_count=1):
        """
        Метод добавления продукта в корзину.
        Если продукт уже есть в корзине, то увеличиваем количество
        """
        if product in self.products:
            self.products[product] = self.products[product] + buy_count
        else:
            self.products[product] = buy_count

    def remove_product(self, product: Product, remove_count=None):
        """
        Метод удаления продукта из корзины.
        Если remove_count не передан, то удаляется вся позиция
        Если remove_count больше, чем количество продуктов в позиции, то удаляется вся позиция
        """
        if product in self.products:
            if remove_count is None or remove_count >= self.products[product]:
                del self.products[product]
            elif remove_count < self.products[product]:
                self.products[product] = self.products[product] - remove_count

    def clear(self):
        self.products.clear()

    def get_total_price(self) -> float:
        total_price = 0.0
        for product, count in self.products.items():
            total_price = product.price * count
        return total_price

    def buy(self):
        """
        Метод покупки.
        Учтите, что товаров может не хватать на складе.
        В этом случае нужно выбросить исключение ValueError
        """
        for product, count in self.products.items():
            if product.check_quantity(count):
                product.buy(count)
            else:
                raise ValueError
        self.clear()
