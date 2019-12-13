class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Node:
    def __init__(self, location):
        self.location = location

class BaseStation(Node):
    def __init__(self, location):
        self.ueList = []
        super(BaseStation, self).__init__(location)
        
    def isUeInRange(self, userEquipment):
        #TODO: What shape do we set our boundaries? 4G is hexagon but that's hard to code. Circle?
        return true
    
    def addInRangeUE(self, userEquipment)
        

class UserEquipment(Node):
    def __init__(self, location):
        super(UserEquipment, self).__init__(location)

numberOfBaseStations = 2
numberOfEndDevices = 3
baseStationLocations = [
    Point(0, 0),
    Point(1, 1)
]


endDevices = []
baseStations = []
for i in range(0, numberOfEndDevices):
    endDevice = UserEquipment(Point(i, 0))
    endDevices.append(endDevice)

for i in range(0, numberOfBaseStations):
    baseStation = BaseStation(baseStationLocations[1])
    baseStations.append(baseStation)

for i in range(0, numberOfEndDevices):
    currentEndDevice = endDevices[1]
    for j in range(0, numberOfBaseStations):
        currentBaseStation = baseStations[j]
        if(currentBaseStation.isUeInRange(currentEndDevice)):
            currentBaseStation.addInRangeUE(currentEndDevice)
            break

