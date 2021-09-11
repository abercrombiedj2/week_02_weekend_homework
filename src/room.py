class Room:

    def __init__(self, capacity):
        self.capacity = capacity
        self.songs = []
        self.guests = []
    
    def check_in_guest(self, guest):
        if len(self.guests) == self.capacity:
            pass
        else:
            self.guests.append(guest)
    
    def check_out_guest(self, guest):
        self.guests.remove(guest)
    
    def add_song(self, song):
        self.songs.append(song)

    def check_playlist(self, favourite_song):
        for song in self.songs:
            if song == favourite_song:
                return "Whoop whoop!"
    