class Song:
    def __init__(self, id, name, date, duration, artists=None):
        self.id = id
        self.name = name
        self.date = date
        self.duration = duration
        self.artists = artists or []

    def add_artist(self, artist):
        self.artists.append(artist)