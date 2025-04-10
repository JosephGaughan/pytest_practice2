class Track:
    def __init__(self, track_name, track_artist):
        self.track_name = track_name
        self.track_artist = track_artist

    def current_track(self):
        return f"Currently playing {self.track_name} by {self.track_artist}."

track1 = Track("Broke In A Minute", "Tory Lanez")

print(track1.current_track())   