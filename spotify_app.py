import os
import streamlit as st
from dotenv import load_dotenv
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth

# Load environment variables from .env file
load_dotenv()

# Retrieve Spotify credentials from environment variables
CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")

# Define the scope for your Spotify app
SCOPES = "user-read-playback-state user-modify-playback-state playlist-modify-public playlist-modify-private"

# Initialize Spotify OAuth
sp_oauth = SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=SCOPES
)

# Initialize Spotify client
sp = None


# Streamlit App
def main():
    global sp

    # Sidebar for Authentication
    st.sidebar.title("🎧 Spotify Authentication")
    auth_url = sp_oauth.get_authorize_url()
    st.sidebar.markdown(f"[Login with Spotify]({auth_url})")

    # User Authentication
    code = st.sidebar.text_input("Enter Spotify Authorization Code:")
    if code:
        try:
            token_info = sp_oauth.get_access_token(code)
            if token_info:
                sp = Spotify(auth=token_info['access_token'])
                st.sidebar.success("Authentication Successful!")
            else:
                st.sidebar.error("Authentication Failed. Please try again.")
        except Exception as e:
            st.sidebar.error(f"Error: {e}")

    # App Main Interface
    if sp:
        st.title("🎶 Spotify Playlist Manager & Player")

        # Search for Tracks
        st.subheader("🔍 Search for Tracks")
        search_query = st.text_input("Enter a song, artist, or album:")
        if st.button("Search"):
            search_results(search_query)

        # Manage Playlists
        st.subheader("📂 Manage Your Playlists")
        playlists = fetch_user_playlists()
        selected_playlist = st.selectbox("Select a Playlist", options=list(playlists.keys()))

        if selected_playlist:
            playlist_id = playlists[selected_playlist]
            if st.button("Show Playlist"):
                show_playlist(playlist_id)
            if st.button("Play Playlist"):
                play_playlist(playlist_id)


# Helper Functions
def search_results(query):
    """Search for tracks and display results."""
    try:
        results = sp.search(q=query, type="track", limit=10)
        tracks = results.get('tracks', {}).get('items', [])
        if tracks:
            for track in tracks:
                st.write(f"**{track['name']}** by {track['artists'][0]['name']}")
                col1, col2 = st.columns(2)
                with col1:
                    if st.button(f"Play '{track['name']}'", key=f"play_{track['id']}"):
                        play_song(track['uri'])
                with col2:
                    if st.button(f"Add to Playlist", key=f"add_{track['id']}"):
                        add_to_playlist(track['uri'])
        else:
            st.warning("No tracks found. Try another search.")
    except Exception as e:
        st.error(f"Error during search: {e}")


def fetch_user_playlists():
    """Fetch the user's playlists."""
    try:
        playlists = sp.current_user_playlists(limit=10)
        return {p['name']: p['id'] for p in playlists['items']}
    except Exception as e:
        st.error(f"Error fetching playlists: {e}")
        return {}


def play_song(uri):
    """Play a specific song using the Spotify API."""
    try:
        sp.start_playback(uris=[uri])
        st.success("Playing song!")
    except Exception as e:
        st.error(f"Error playing song: {e}")


def add_to_playlist(uri):
    """Add a track to the user's selected playlist."""
    try:
        playlists = fetch_user_playlists()
        selected_playlist = st.selectbox("Select a Playlist to Add", options=list(playlists.keys()))
        playlist_id = playlists.get(selected_playlist)

        if playlist_id:
            sp.playlist_add_items(playlist_id, [uri])
            st.success(f"Track added to playlist '{selected_playlist}'!")
    except Exception as e:
        st.error(f"Error adding track to playlist: {e}")


def show_playlist(playlist_id):
    """Show the tracks in the selected playlist."""
    try:
        playlist = sp.playlist_tracks(playlist_id)
        for item in playlist['items']:
            track = item['track']
            st.write(f"**{track['name']}** by {track['artists'][0]['name']}")
    except Exception as e:
        st.error(f"Error showing playlist: {e}")


def play_playlist(playlist_id):
    """Play a playlist using the Spotify API."""
    try:
        sp.start_playback(context_uri=f"spotify:playlist:{playlist_id}")
        st.success("Playing playlist!")
    except Exception as e:
        st.error(f"Error playing playlist: {e}")


if __name__ == "__main__":
    main()
