from bulb import BulbWithEnum
import sys


class BulbDemo:

    @classmethod
    def main(cls, args):
        b = BulbWithEnum()
        print(f"bulb size {b.getBulbSize()}")


if __name__ == "__main__":
    BulbDemo.main(sys.argv)
