class Bulb:
    TotalBulbCount = 0

    def __init__(self):     # constructor
        Bulb.TotalBulbCount += 1
        self.isOn = False
    
    @classmethod
    def getBulbCount(cls):  # Class Method
        return cls.TotalBulbCount
    
    def turnOn(self):       # Instance method    
        self.isOn = True

    def turnOff(self):      # Instance method
        self.isOn = False

    def isOnFun(self):      # Instance method
        return self.isOn 
    
class BulbDemo:

    @classmethod
    def main(cls,args):
        b = Bulb()
        print(f"Bulb is on return {b.isOnFun()}")
        b.turnOn()
        print(f"Bulb is on return {b.isOnFun()}")
        print(Bulb.getBulbCount())

if __name__ == '__main__':
    import sys
    BulbDemo.main(sys.argv)