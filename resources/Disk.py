class Disk:
    def __init__(self, disk_type: str, speed:int) -> None:
        self.disk_type = disk_type
        self.speed = speed

    def __str__(self) -> str:
        return str(self.__dict__)
    

