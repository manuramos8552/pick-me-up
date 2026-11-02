# store.py - Store and DisplayStand


class DisplayStand:
    def __init__(self, standId, location, screen=None):
        self.standId = standId
        self.location = location
        self.slots = []
        self.screen = screen          # Display, 0..1

    def addSlot(self, slot):
        self.slots.append(slot)

    def checkSlots(self):
        """Check every slot; return the PickupEvents that finished."""
        finished = []
        for slot in self.slots:
            event = slot.checkSensor()
            if event:
                finished.append(event)
        return finished


class Store:
    def __init__(self, name):
        self.name = name
        self.stands = []

    def addStand(self, stand):
        self.stands.append(stand)

    def getAllSlots(self):
        return [slot for stand in self.stands for slot in stand.slots]
