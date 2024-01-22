from bulb import Bulb


class BulbDemo:

    @classmethod
    def main(cls, args):
        b = Bulb()
        print(f"Bulb is on return {b.isOnFun()}")

        b.turnOn()
        print(f"bulb is on return {b.isOnFun()}")

        print(f"bulb count {Bulb.getBulbCount()}")


if __name__ == "__main__":
    import sys
    BulbDemo.main(sys.argv)
