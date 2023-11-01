from musical_track import Track
from media_player_queue import MediaPlayerQueue

track1 = Track("white whistle")
track2 = Track("butter butter")
track3 = Track("oh black star")
track4 = Track("watch that chicken")
track5 = Track("Don't go")

print(track1.length)
print(track2.length)

print()

media_player = MediaPlayerQueue()
media_player.add_track(track1)
media_player.add_track(track2)
media_player.add_track(track3)
media_player.add_track(track4)
media_player.add_track(track5)

media_player.play()