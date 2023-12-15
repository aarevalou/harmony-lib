from enum import Enum

class CamposSong(Enum):
    NAME = "Nombre"
    DATE = "Fecha lanzamiento"
    DURATION = "Duracion"
    ARTISTS = "Colaboradores"

class CamposLabel(Enum):
    NAME = "Nombre"
    ARTISTS = "Artistas"

class CamposArtist(Enum):
    NAME = "Nombre"
    GENRE = "Generos"
    SONGS = "Canciones"

class CamposAlbum(Enum):
    NAME = "Nombre"
    PUBLISH_DATE = "Fecha lanzamiento"
    ARTIST = "Artistas"
    SONGS = "Canciones"
