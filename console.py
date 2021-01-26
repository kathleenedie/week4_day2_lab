import pdb
from models.artist import Artist
from models.album import Album

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

album_repository.delete_all()
artist_repository.delete_all()

artist1 = Artist("Queens of the Stone Age")
artist_repository.save(artist1)

artist2 = Artist("The Vaselines")
artist_repository.save(artist2)

album1 = Album("Villains", artist1, "Grunge")
album_repository.save(album1)

album2 = Album("V for Vaselines", artist2, "Indie")
album_repository.save(album2)

album3 = Album("Enter the Vaselines", artist2, "Indie")
album_repository.save(album3)

pdb.set_trace()
