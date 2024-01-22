class Bulb:
    totalBulbCount = 0  # class variables

    def __init__(self):  # constructor
        Bulb.totalBulbCount += 1
        self.isOn = False  # instance variable

    @classmethod
    def getBulbCount(cls):  # class method
        return cls.totalBulbCount

    def turnOn(self):  # instance method
        self.isOn = True

    def turnOff(self):  # instance method
        self.isOn = False

    def isOnFun(self):  # instance method
        return self.isOn
