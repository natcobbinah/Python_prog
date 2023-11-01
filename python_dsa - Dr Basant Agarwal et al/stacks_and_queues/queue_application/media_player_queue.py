import time
import sys,os
sys.path.append(os.path.abspath(os.path.join('..')))
from node_based_queue import Queue


class MediaPlayerQueue(Queue):

    def __init__(self):
        super().__init__()

    def add_track(self,track):
        self.enqueue(track)

    def play(self):
        while self.count > 0:
            current_track_node = self.dequeue()
            print(f"Now playing {current_track_node.title}",  
                  time.sleep(current_track_node.length))