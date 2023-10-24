from enum import Enum

class Bulb:
    class BulbSize(Enum):
        SMALL = 'SMALL',
        MEDIUM = 'MEDIUM',
        LARGE =  'LARGE'

    def __init__(self):
        self.isOn = False 
        self.size = Bulb.BulbSize.MEDIUM.name

    def getBulbSize(self):
        return self.size 

    def setBulbSize(self,value):
        self.size = value

class BulbDemo:

    @classmethod
    def main(cls, args):
        b = Bulb()
        print(f"Bulb Size {b.getBulbSize()}")

if __name__ == '__main__':
    import sys
    BulbDemo.main(sys.argv)