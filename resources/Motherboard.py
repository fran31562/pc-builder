class Motherboard:
    def __init__(self, memory_slots: int, pcie_slots: int, socket: str, memory_type: str ) -> None:
        self.memory_slots = memory_slots
        self.pcie_slots = pcie_slots
        self.socket = socket
        self.memory_type = memory_type

    def __str__(self) -> str:
        return str(self.__dict__)