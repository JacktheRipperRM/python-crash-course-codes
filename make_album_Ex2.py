def make_album(artist_name,album_title):
    total_name={'Name' : artist_name, 'Title' : album_title}
    return total_name

create_album = make_album('Rabindranath','Sesh Kobita')
for album in create_album.values():
    print(album)
