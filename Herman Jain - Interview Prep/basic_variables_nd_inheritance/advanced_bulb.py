from bulb import Bulb


class AdvancedBulb(Bulb):
    def __init__(self):
        self.intensity = 0
        super().__init__()

    def setIntensity(self, i):
        self.intensity = i

    def getIntensity(self):
        return self.intensity
