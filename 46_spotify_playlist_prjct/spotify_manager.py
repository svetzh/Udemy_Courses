import spotipy
from spotipy import SpotifyOAuth
from spotipy.exceptions import SpotifyException


class SpotifyManager:
    def __init__(self, client_id, client_secret, redirect_uri, scope='playlist-modify-private', cache_path='token.txt'):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            scope=scope,
            redirect_uri=redirect_uri,
            client_id=client_id,
            client_secret=client_secret,
            show_dialog=True,
            cache_path=cache_path
        ))

    def get_user_id(self):
        try:
            user_info = self.sp.current_user()
            if 'id' in user_info:
                return user_info['id']
            else:
                print("Unable to retrieve user ID.")
                return None
        except SpotifyException as spotify_exception:
            print(f"Spotify API error: {spotify_exception}")
            return None
