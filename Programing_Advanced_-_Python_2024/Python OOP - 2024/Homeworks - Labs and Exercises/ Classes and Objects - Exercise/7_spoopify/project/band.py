# from album import Album
from project.album import Album


class Band:

    def __init__(self, name: str):
        self.name = name
        self.albums: list[str] = []

    def add_album(self, album: Album) -> str:
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."

        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str) -> str:
        for album in self.albums:
            if album.name == album_name:
                if album.published:
                    return "Album has been published. It cannot be removed."
                self.albums.remove(album)
                return f"Album {album_name} has been removed."

        return f"Album {album_name} is not found."

    def details(self) -> str:
        output = [f"Band {self.name}"]
        for album in self.albums:
            output.append(f"{album.details()}")

        return "\n".join(output)



