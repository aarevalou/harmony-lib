import json
from tabulate import tabulate
from models.album import Album
from models.artist import Artist
from models.song import Song
from models.label import Label

class Utils:

    @staticmethod
    def to_json(data, filename):
        with open('resources/' + filename, 'w') as json_file:
            json.dump(data, json_file, indent=4, default=lambda obj: obj.__dict__)

    @staticmethod
    def from_json(filename):
        with open('resources/' + filename, 'r') as json_file:
            data = json.load(json_file)

        if filename == 'artists.json':
            return [Utils.data_to_artist(entry) for entry in data]
        elif filename == 'songs.json':
            return [Utils.data_to_songs(entry) for entry in data]
        elif filename == 'albums.json':
            return [Utils.data_to_albums(entry) for entry in data]
        elif filename == 'labels.json':
            return [Utils.data_to_labels(entry) for entry in data]
        else:
            return None

    @staticmethod
    def data_to_artist(data):
        artist = Artist(**data)
        return artist

    @staticmethod
    def data_to_songs(data):
        songs = Song(**data)
        return songs

    @staticmethod
    def data_to_albums(data):
        albums = Album(**data)
        return albums

    @staticmethod
    def data_to_labels(data):
        labels = Label(**data)
        return labels

    @staticmethod
    def show_table(lista, campos_enum):
        if not lista:
            print("La lista está vacía.")
            return

        # Obtén los nombres de los campos en español directamente
        nombres_campos = [campo.name for campo in campos_enum]
        nombre_clase = lista[0].__class__.__name__.upper()

        # Crear una lista de listas con los datos de la tabla
        data = []
        for objeto in lista:
            valores = []
            for campo in nombres_campos:
                if campo.lower() != "id":
                    valor = getattr(objeto, campo.lower())
                    if isinstance(valor, list) and all(isinstance(item, dict) for item in valor):
                        # Si el campo es una lista de objetos, muestra el atributo 'name'
                        valor = ", ".join(item.get('name', 'vacio') for item in valor) or 'vacio'
                    elif isinstance(valor, Artist):
                        # Si el campo es una instancia de la clase 'Artist', muestra solo el nombre
                        valor = valor.name if hasattr(valor, 'name') else 'vacio'
                    elif isinstance(valor, dict):
                        # Si el campo es un diccionario, intenta mostrar el atributo 'name' o muestra 'vacio'
                        valor = valor.get('name', 'vacio') or 'vacio'
                    else:
                        # Para otros tipos de atributos, muestra el valor normal o 'vacio'
                        valor = str(valor) or 'vacio'
                else:
                    valor = ""
                valores.append(valor)

            data.append(valores)

        # Imprime la tabla usando tabulate
        print()
        print(f"LISTADO DE {nombre_clase}S :")
        print(tabulate(data, headers=nombres_campos, tablefmt="grid"))
