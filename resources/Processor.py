class Processor:
    def __init__(self, speed: int, power: int, socket: str) -> None:
        self.speed = speed
        self.power = power
        self.socket = socket
    
    def __str__(self) -> str:
        return str(self.__dict__)