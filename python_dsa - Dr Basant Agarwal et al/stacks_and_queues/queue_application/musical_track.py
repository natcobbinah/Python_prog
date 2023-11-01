from random import randint 

class Track:

    def __init__(self, title=None):
        self.title = title 
        self.length = randint(5,10)

# testing out the track class
#track1 = Track("white whistle")
#track2 = Track("butter butter")
#print(track1.length)
#print(track2.length)
        