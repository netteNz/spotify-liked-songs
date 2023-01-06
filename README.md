## This code defines four functions:
- `get_spotify_client()`: This function takes your Spotify API credentials as input and
returns a Spotify client that you can use to make API requests.

- `get_liked_songs()`: This function takes a Spotify client as input and retums a list of the
liked songs in your account.

- `save_liked_songs_to_file()`: This function takes a list of tracks and a file path as input,
and saves the song names and artists of the tracks to the specified file, one song per line.

- `main()`: This function contains the main logic of the program. It retrieves your liked
songs, saves them to a text file, and prints "Done!".