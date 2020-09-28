# PLAYLISTEXT
A Python program that makes Spotify's playlists based in text.

This is my first program using an API. For this project, I choose to work with the Spotipy library, since it's very begginer friendly and simple to use.

The program basically takes the phrase that the user inputs and looks up each word from that phrase into Spotify to see if there's a song with the same name, if it has, the program adds it to a new playlist that it also created in the user's account. In the end, we have a playlist with all the music based in the words in the user's input phrase.

Here's an exemple, if the input is: "That's a demonstration to show PLAYLISTEXT in action, this words will become a playlist"

The playlist created will look like this:      
-Demonstration 

-Action 

-Words 

-Will 

-Become 

-Playlist
