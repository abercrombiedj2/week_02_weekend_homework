class Venue:

    def __init__(self, name, till, entry_fee):
        self.name = name
        self.rooms = []
        self.till = till
        self.entry_fee = entry_fee

    def add_room(self, room):
        self.rooms.append(room)
    
    def take_entry_fee(self, entry_fee):
        self.till += entry_fee
