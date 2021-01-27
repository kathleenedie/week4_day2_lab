from db.run_sql import run_sql

from models.artist import Artist
from models.album import Album
import repositories.album_repository as album_repository


def save(artist):
    sql = "INSERT INTO artists (name) VALUES (%s) RETURNING *"
    values = [artist.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist


def delete_all():
    sql = "DELETE  FROM artists"
    run_sql(sql)


def select(id):
    artist = None
    sql = "SELECT * FROM artists WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        artist = Artist(result['name'], result['id'])
    return artist


def select_all():
    artists = []

    sql = "SELECT * FROM artists"
    results = run_sql(sql)

    for row in results:
        artist = Artist(row['name'], row['id'])
        artists.append(artist)
    return artists


# Extensions


# def albums(artist):
#     albums = []

#     sql = "SELECT * FROM albums WHERE artist_id = %s"
#     values = [id] #select(id)
#     results = run_sql(sql, values)

#     if results is not None:
    
#         for row in results:
#             album = Album(row['id'], row['title'], row['artist_id'], row['genre'])
#             albums.append(album)
#         return albums

# error can't adapt type 'builtin_function_or_method'

def albums(artist):
    albums = []

    sql = "SELECT * FROM albums WHERE artist_id = (SELECT id FROM artists WHERE name = %s)"
    values = [artist.name]
    results = run_sql(sql, values)

    if results is not None:
    
        for row in results:
            album = Album(row['id'], row['title'], row['artist_id'], row['genre'])
            albums.append(album)
        return albums

# *** AttributeError: 'str' object has no attribute 'name'

def delete(id):
    sql = "DELETE  FROM artists WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(artist):
    sql = "UPDATE artists SET (name, id) = (%s, %s) WHERE id = %s"
    values = [artist.name, artist.id]
    run_sql(sql, values)

# *** AttributeError: 'int' object has no attribute 'name'
