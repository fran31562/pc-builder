class Case:
    def __init__(self, size: int, price: int) -> None:
        self.size = size
        self.price = price

    def __str__(self) -> str:
        return str(self.__dict__)