## 2. Creating a Class and an Instance ##

class MusicArtist():
    pass

ed_sheeran = MusicArtist()
beyonce = MusicArtist()
kanye_west = MusicArtist()

## 3. Defining Variables Within a Class ##

class MusicArtist(object):
    pass

ed_sheeran = MusicArtist()
beyonce = MusicArtist()
ed_sheeran.name = "Ed Sheeran"
ed_sheeran.genre = "Pop"
ed_sheeran.song = "Thinking out Loud"

beyonce.name = "Beyonce"
beyonce.genre = "R&B"
beyonce.song = "Halo"

print(ed_sheeran.name)
print(ed_sheeran.genre)
print(ed_sheeran.song)

print(beyonce.name)
print(beyonce.genre)
print(beyonce.song)

## 4. Defining Attributes Using The __init__() Method ##

class MusicArtist():
    def __init__(self, name, genre, song):
        self.name = name
        self.genre = genre
        self.song = song
        
ed_sheeran = MusicArtist("Ed Sheeran","Pop","Thinking out Loud")
beyonce = MusicArtist("Beyonce", "R&B","Halo")

## 5. Accessing Instance Variables ##

class MusicArtist():
    def __init__(self, name, genre, song):
        self.name = name
        self.genre = genre
        self.song = song
        
ed_sheeran = MusicArtist("Ed Sheeran","Pop","Thinking out Loud")
beyonce = MusicArtist("Beyonce", "R&B","Halo")
print("{name} is singing {song} tonight".format(name = ed_sheeran.name, song = ed_sheeran.song))
print("{name} is singing {song} tonight".format(name = beyonce.name, song = beyonce.song))

## 6. Adding Methods to a Class ##

class MusicArtist():
    def __init__(self, name, genre, song):
        self.name = name
        self.genre = genre
        self.song = song

        
ed_sheeran = MusicArtist("Ed Sheeran","Pop","Thinking out Loud")
beyonce = MusicArtist("Beyonce", "R&B","Halo")

print("{name} is singing {song} tonight".format(name = ed_sheeran.name, song = ed_sheeran.song))
print("{name} is singing {song} tonight".format(name = beyonce.name, song = beyonce.song))
class MusicArtist():
    def __init__(self, name, genre, song):
        self.name = name
        self.genre = genre
        self.song = song
    
    def sing(self):
        return print("{name} will be singing {song} tonight".format(name = self.name, song = self.song))
        
ed_sheeran = MusicArtist("Ed Sheeran","Pop","Thinking out Loud")
beyonce = MusicArtist("Beyonce", "R&B","Halo")

ed_sheeran_sing = ed_sheeran.sing()
beyonce_sing = beyonce.sing()

## 7. Adding More Instance Variables And Methods ##

class MusicArtist():
    def __init__(self, name, genre, song, ):
        self.name = name
        self.genre = genre
        self.song = song
    
    def sing(self):
        return print("{name} will be singing {song} tonight".format(name = self.name, song = self.song))
        
ed_sheeran = MusicArtist("Ed Sheeran","Pop","Thinking out Loud")
beyonce = MusicArtist("Beyonce", "R&B","Halo")
class MusicArtist():
    def __init__(self, name, genre, song, lyrics):
        self.name = name
        self.genre = genre
        self.song = song
        self.lyrics = lyrics
    
    def sing(self):
        return print("{name} will be singing {song} tonight".format(name = self.name, song = self.song))
    
    def write(self):
        return print("{name} wrote: {lyrics}".format(name = self.name, lyrics = self.lyrics))
        
ed_sheeran = MusicArtist("Ed Sheeran","Pop","Thinking out Loud", "When you're lips")
beyonce = MusicArtist("Beyonce", "R&B","Halo", "I can be your Halo")

ed_sheeran_write = ed_sheeran.write()
beyonce_write = beyonce.write()

print(ed_sheeran_write)
print(beyonce_write)