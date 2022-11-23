import json
import spotipy
import webbrowser


# username = '7350485057'
# clientID = '14ce4455979541ddb95c856475564aad'
# clientSecret = '99a07aa919e54280bae8efb81f7dbebd'
# redirect_uri = 'http://google.com/callback/'
# oauth_object = spotipy.SpotifyOAuth(clientID, clientSecret, redirect_uri)
# token_dict = oauth_object.get_access_token()
# token = token_dict['access_token']
# spotifyObject = spotipy.Spotify(auth=token)
# user_name = spotifyObject.current_user()
# # To print the response in readable format.
# print(json.dumps(user_name, sort_keys=True, indent=4))
username = 'Sk Sayril'
clientID = '14ce4455979541ddb95c856475564aad'
clientSecret = '99a07aa919e54280bae8efb81f7dbebd'
redirect_uri = 'http://google.com/callback/'
oauth_object = spotipy.SpotifyOAuth(clientID, clientSecret, redirect_uri)
token_dict = oauth_object.get_access_token()
token = token_dict['access_token']
spotifyObject = spotipy.Spotify(auth=token)
user_name = spotifyObject.current_user()
  
# To print the JSON response from 
# browser in a readable format.
# optional can be removed
print(json.dumps(user_name, sort_keys=True, indent=4))
  
while True:
    print("Welcome to the project, " + user_name['display_name'])
    print("0 - Exit the console")
    print("1 - Search for a Song")
    user_input = int(input("Enter Your Choice: "))
    if user_input == 1:
        search_song = input("Enter the song name: ")
        results = spotifyObject.search(search_song, 1, 0, "track")
        songs_dict = results['tracks']
        song_items = songs_dict['items']
        song = song_items[0]['external_urls']['spotify']
        webbrowser.open(song)
        print('Song has opened in your browser.')
    elif user_input == 0:
        print("Good Bye, Have a great day!")
        break
    else:
        print("Please enter valid user-input.")