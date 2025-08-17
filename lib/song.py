class Song:
    songs = []
    count = 0
    genres = set()
    artists = []
    genre_count = {}
    artist_count = {}
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        Song.add_song_to_count()
        Song.add_to_genres(self.genre)
        Song.add_to_artists(self.artist)
        Song.add_to_genre_count(self.genre)
        Song.songs.append(self)
        Song.add_to_artist_count(self.artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        cls.genres.add(genre)

    @classmethod
    def add_to_artists(cls, artist):
        cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count.keys():
            cls.genre_count[f"{genre}"] += 1
        else:
            cls.genre_count[f"{genre}"] = 0
            cls.genre_count[f"{genre}"] += 1

    @classmethod
    def add_to_artist_count(cls, artist):
            if artist in cls.artist_count.keys():
                cls.artist_count[f"{artist}"] += 1
            else:
                cls.artist_count[f"{artist}"] = 0
                cls.artist_count[f"{artist}"] += 1

