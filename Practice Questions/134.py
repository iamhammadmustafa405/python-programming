# 134: 1. Custom Length (Dunder Method)
# Create a class Playlist:

# Attribute: songs (list)
# Implement __len__() so that len(obj) returns number of songs

class Playlist:
    def __init__(self, songs):
        self.songs = songs
    
    def __len__(self):
        return len(self.songs)
    
playlist= Playlist(["Psl10", "Psl11", "Psl12"])
print(len(playlist)) # it means playlist.__len__()