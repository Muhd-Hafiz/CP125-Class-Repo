def manage_playlist(current_playlist, add_songs, import_playlist, banned_songs):
   
    for song in add_songs:  
        current_playlist.add(song)

    for song in import_playlist:
        current_playlist.add(song)

    for song in banned_songs:
        current_playlist.discard(song)
    
    while len(current_playlist) > 6:
        current_playlist.pop()

    return len(current_playlist)
       
          


