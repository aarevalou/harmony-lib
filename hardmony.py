from utils.utils import Utils
from utils.enums import CamposSong, CamposLabel, CamposArtist, CamposAlbum


class Hardmony:
    def __init__(self):
        self.artists = Utils.from_json('artists.json')
        self.songs = Utils.from_json('songs.json')
        self.albums = Utils.from_json('albums.json')
        self.labels = Utils.from_json('labels.json')

    def add_artist(self, artist):
        self.artists.append(artist)

    def add_song(self, song):
        self.songs.append(song)

    def add_album(self, album):
        self.albums.append(album)

    def add_label(self, label):
        self.labels.append(label)

    def search_artist(self, name):
        for artist in self.artists:
            if artist.name.lower() == name.lower():
                return artist
        return None
    
    def show_artists(self):
        Utils.show_table(self.artists, CamposArtist)

    def show_songs(self):
        Utils.show_table(self.songs, CamposSong)

    def show_albums(self):
        Utils.show_table(self.albums, CamposAlbum)

    def show_labels(self):
        Utils.show_table(self.labels, CamposLabel)

    def show_artist_data(artist_name):
        if artist_name:
            print(f"Datos '{artist_name.name}' ")
            print(f"ID: {artist_name.id}")
            print("Songs :")
            for song in artist_name.songs:
                print(f"- {song.name}")
            print("Albums ")
            for albums in artist_name.albums:
                print(f"- {albums.name} ({albums.publish_date})")
        else:                  
            print("El artista no se encontro")

    def show_artist_song(artist_name):
       if  artist_name: 
            print(f"Canciones de {artist_name.name}")
            for song in artist_name.songs:
                print(f"- {song.name}")
                print(f"- {song.date}")
                print(f"- {song.duration}")
       else:
                print("No se encontro al artista")

    def show_artist_album(artist_name):
        if  artist_name:
            print(f"Albumes de {artist_name.name}")
            for album in artist_name.albums:
                print(f" -{album.name} {album.publish_date}")
        else:
            print("Artista no econtrado")

    def find_artists_by_genre(self,genre):
        match_artist=[]
        for artist in self.artists:
            if artist.genre.lower() == genre.lower():
                match_artist.append(artist)
        return match_artist
    
    def show_all_artists(self):
        print("Lista de todos los artistas:")
        for artist in self.artists:
            print(f"- {artist.name}")

   
        