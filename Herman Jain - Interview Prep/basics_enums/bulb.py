class BulbWithEnum:
    class BulbSize:
        SMALL = 'SMALL'
        MEDIUM = 'MEDIUM'
        LARGE = 'LARGE'

    def __init__(self):
        self.isOn = False
        self.size = BulbWithEnum.BulbSize.MEDIUM

    def getBulbSize(self):
        return self.size

    def setBulbSize(self, value):
        self.size = value
