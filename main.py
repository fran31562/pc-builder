from JSONDictEncoder import JSONDictEncoder
from resources import *
import json

cooling = Cooling(False, True)
disk = Disk('SSD', 10)
power = PowerSupply(1, 'bronze')
processor = Processor(2, 10, "LGA1700")
motherboard = Motherboard(10, 10, 'LGA1700', 'type1')
memory = Memory(8, 10, 'type1')
case = Case(15, 180)
graphics = Graphics(12, 10)

computer = Computer(cooling, case, graphics, memory, motherboard, power, processor, disk)
 

print(json.dumps(computer, cls=JSONDictEncoder))