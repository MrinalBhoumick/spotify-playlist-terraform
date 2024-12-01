resource "spotify_playlist" "playlist" {
    name        = "Bollywood"
    description = "My playlist is Automative"
    public      = true

    tracks = [
        data.spotify_track.fear_song.id,
        data.spotify_track.millionaire.id
    ]
}

data "spotify_track" "fear_song" {
    url = "https://open.spotify.com/track/7eExEhh23g4wPOchaK7Vd8"
}

data "spotify_track" "millionaire" {
    url = "https://open.spotify.com/track/78BWCd70D1X6LMkDZm1UoF"
}
