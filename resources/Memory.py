class Memory:
    def __init__(self, capacity: int, speed: int, memory_type: str) -> None:
        self.capacity = capacity
        self.speed = speed
        self.memory_type  = memory_type

    def __str__(self) -> str:
        return str(self.__dict__)