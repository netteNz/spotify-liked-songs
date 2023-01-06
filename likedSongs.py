import spotipy
import spotipy.util as util

def get_spotify_client(client_id, client_secret, username):
    # Request authorization from the user
    scope = 'user-library-read'
    redirect_uri = 'http://localhost:8888/callback'

    token = util.prompt_for_user_token(username, scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)

    # Create a Spotify client
    return spotipy.Spotify(auth=token)

def get_liked_songs(client):
    # Retrieve the list of liked songs
    results = client.current_user_saved_tracks()
    tracks = results['items']
    while results['next']:
        results = client.next(results)
        tracks.extend(results['items'])
    return tracks

def save_liked_songs_to_file(tracks, filepath):
    # Open the text file for writing
    with open(filepath, 'w') as f:
        # Write the song names and artists to the text file
        for track in tracks:
            name = track['track']['name']
            artist = track['track']['artists'][0]['name']
            f.write(f"{name} - {artist}\n")

def main():
    # Replace these with your own Spotify API credentials
    CLIENT_ID = 'your-client-id'
    CLIENT_SECRET = 'your-client-secret'
    USERNAME = 'your-spotify-username'

    client = get_spotify_client(CLIENT_ID, CLIENT_SECRET, USERNAME)
    tracks = get_liked_songs(client)
    save_liked_songs_to_file(tracks, 'liked_songs.txt')

if __name__ == '__main__':
    main()
