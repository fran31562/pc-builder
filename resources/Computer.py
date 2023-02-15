from resources.Cooling import Cooling
from resources.Case import Case
from resources.Graphics import Graphics
from resources.Memory import Memory
from resources.Motherboard import Motherboard
from resources.PowerSupply import PowerSupply
from resources.Processor import Processor
from resources.Disk import Disk


class Computer:
    def __init__(self, cooling: Cooling, case: Case, graphics: Graphics, memory: Memory, motherboard: Motherboard, power_supply: PowerSupply, processor: Processor, 
                 storage: Disk) -> None:
        self.cooling = cooling
        self.case = case
        self.graphics = graphics
        self.memory = memory
        self.motherboard = motherboard
        self.power_supply = power_supply
        self.processor = processor
        self.storage = storage

    def __str__(self) -> str:
        return str(self.__dict__)
