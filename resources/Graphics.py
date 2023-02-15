class Graphics:
    def __init__(self, speed: int, vram: int) -> None:
        self.speed = speed
        self.vram = vram 
    
    def __str__(self) -> str:
        return str(self.__dict__)