class Album:
    def __init__(self, id, name, publish_date, artist, songs=None):
        self.id = id
        self.name = name
        self.publish_date = publish_date
        self.artist = artist
        self.songs = songs or []

    def add_song(self, song):
        self.songs.append(song)
