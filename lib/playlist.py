from track import *

class MusicTracker:
    def __init__(self):
        self.playlist = []

    def add_song(self, song_by_artist):
        self.playlist.append(song_by_artist)

    def show_playlist(self):
        if not self.playlist:
            return "Playlist is empty."
        return "\n".join([f"{i+1}. {track}" for i, track in enumerate(self.playlist)])

class Track:
    def __init__(self, track_name, track_artist):
        self.track_name = track_name
        self.track_artist = track_artist

    def __str__(self):
        return f"{self.track_name} by {self.track_artist}"

# Example usage:
track1 = Track("Broke In A Minute", "Tory Lanez")
playlist = MusicTracker()
playlist.add_song(track1)

print(playlist.show_playlist())  # Now prints: "1. Broke In A Minute by Tory Lanez"
