class Artist:
    def __init__(self, id, name, genre, songs=None):
        self.id = id
        self.name = name
        self.genre = genre
        self.songs = songs or []


    def add_single(self, song):
        self.songs.append(song)

