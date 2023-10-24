def make_album(artist_name, album_title, num_of_songs=None):
    album =  {
        'Artist Name': artist_name,
        'Album Title': album_title,
    }

    if num_of_songs:
        album['Number of Songs'] = num_of_songs

    return album

while True:
    artist_name = input("Please Enter artist name ")
    if artist_name == 'q':
        break

    album_title = input("Please Enter album title ")
    if album_title == 'q':
        break

    num_of_songs = input("Please Enter number of songs on album ")
    if num_of_songs == 'q':
        break

    album = make_album(artist_name, album_title, num_of_songs)
    print(album)
