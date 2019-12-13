class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Node:
    def __init__(self, location):
        self.location = location
        self.signalStrength = 0

class BaseStation(Node):
    def __init__(self, location):
        self.ueList = []
        super(BaseStation, self).__init__(location)
        
    #TODO: What shape do we set our boundaries? 4G is hexagon but that's hard to code. Squares?
    def isUeInRange(self, userEquipment):
        return True
    
    #TODO: Account for distance as well as BaseStation number of equipments
    def getBandwidth(self, userEquipment):
        return 1

    def addInRangeUE(self, userEquipment):
        self.ueList.append(userEquipment)
        

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

#Initializing nodes
for i in range(0, numberOfEndDevices):
    endDevice = UserEquipment(Point(i, 0))
    endDevices.append(endDevice)

for i in range(0, numberOfBaseStations):
    baseStation = BaseStation(baseStationLocations[1])
    baseStations.append(baseStation)

#Assigning nodes to base stations
for i in range(0, numberOfEndDevices):
    currentEndDevice = endDevices[1]
    for j in range(0, numberOfBaseStations):
        currentBaseStation = baseStations[j]
        if(currentBaseStation.isUeInRange(currentEndDevice)):
            currentBaseStation.addInRangeUE(currentEndDevice)
            break

#Calculating signal strengths base off of naive assignment
unoptimizedBandwidths = []
for i in range(0, numberOfBaseStations):
    currentBaseStation = baseStations[i]
    currentEndDevices = currentBaseStation.ueList
    for j in range(0, len(currentEndDevices)):
        currentDevice = currentEndDevices[j]
        bandwidth = currentBaseStation.getBandwidth(currentDevice)
        unoptimizedBandwidths.append(bandwidth)


