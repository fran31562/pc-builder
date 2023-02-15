class Cooling:
    def __init__(self, air: bool, water: bool) -> None:
        self.air = air 
        self.water = water

    def __str__(self) -> str:
        return str(self.__dict__)

