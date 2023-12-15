class Label:
    def __init__(self, id, name, artists=None):
        self.id = id
        self.name = name
        self.artists = artists or []

    def add_artist(self, artist):
        self.artists.append(artist)
