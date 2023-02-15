class PowerSupply:
    def __init__(self, power: int, rating: str) -> None:
        self.power = power
        self.rating = rating

    def __str__(self) -> str:
        return str(self.__dict__)