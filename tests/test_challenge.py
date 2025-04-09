from lib.challenge import *

def test_empty_playlist():
    music_tracker = MusicTracker()
    assert music_tracker.playlist == []

def test_add_songs():
    music_tracker = MusicTracker()
    music_tracker.add_song("Song1 by Artist1")
    assert music_tracker.playlist == ["Song1 by Artist1"]