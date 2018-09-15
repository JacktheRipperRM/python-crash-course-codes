def make_album(artist_name,album_title):
    total_name={'Name' : artist_name, 'Title' : album_title}
    return total_name

while 1:
    print('Please enter the name of Artist Name and his/her Album Name')
    print('("Print \'q\' to quit from the program")')

    artist_name=input('Artist Name : ')
    if artist_name=='q':
        break
    album_title=input('Album Name : ')
    if album_title=='q':
        break
    
    complete_name = make_album(artist_name,album_title)
    for names in complete_name.values():
        print(names)
    
