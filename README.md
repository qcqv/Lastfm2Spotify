# LastFM to Spotify Playlist

This Python script transfers your top tracks from Last.fm to a Spotify playlist.

## Setup

1. **Install Dependencies**: Install the required Python packages using pip:
pip install requests spotipy


2. **Get API Credentials**:
- For Last.fm: [Create an API account](https://www.last.fm/api/account/create) and note down your API key.
- For Spotify: [Create a Spotify Developer account](https://developer.spotify.com/dashboard/applications) to get your client ID and client secret.

3. **Set Up Environment Variables**:
- Create a file named `.env` in the project directory.
- Add the following lines to the `.env` file, replacing placeholders with your actual credentials:
  ```
  LASTFM_API_KEY=YOUR_LASTFM_API_KEY
  LASTFM_USERNAME=YOUR_LASTFM_USERNAME
  SPOTIPY_CLIENT_ID=YOUR_SPOTIFY_CLIENT_ID
  SPOTIPY_CLIENT_SECRET=YOUR_SPOTIFY_CLIENT_SECRET
  SPOTIPY_REDIRECT_URI=https://example.com
  ```

4. **Run the Script**:
- Run the script `Last2Spotify.py`.

5. **Authorize Spotify**:
- The script will open a browser window to authorize the Spotify app.
- Follow the instructions to authorize and paste the URL you're redirected to into the terminal.

6. **Enjoy Your Playlist**:
- Once the script finishes, check your Spotify account for a new playlist named "My Top Tracks" containing your top tracks from Last.fm!

## Disclaimer
This script is provided as-is and may have limitations or require further customization based on your Last.fm and Spotify account settings.
