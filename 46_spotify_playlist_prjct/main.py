import os
from song_manager import Top100
from spotify_manager import SpotifyManager

if __name__ == "__main__":
    top_100 = Top100()
    date, year, month, day = top_100.pick_date()
    songs = top_100.songs()
    CLIENT_ID = os.environ.get('SPOTIPY_CLIENT_ID')
    CLIENT_SECRET = os.environ.get('SPOTIPY_CLIENT_SECRET')
    REDIRECT_URI = 'http://localhost:3000/callback'
    DISPLAY = os.environ.get('username')

    spotify_manager = SpotifyManager(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI)
    user_id = spotify_manager.get_user_id()
    song_uri = []
    for song in songs:
        sp_search = spotify_manager.sp.search(q=f'track:{song} year:{year}', type='track')
        try:
            uri = sp_search['tracks']['items'][0]['uri']
            song_uri.append(uri)
        except IndexError:
            print(f'{song} is currently unavailable on Spotify')

    playlist = spotify_manager.sp.user_playlist_create(user=user_id,
                                                       name=f'{date} Billboard 100',
                                                       public=False)

    spotify_manager.sp.user_playlist_add_tracks(user=user_id,
                                                playlist_id=playlist['id'],
                                                tracks=song_uri)

