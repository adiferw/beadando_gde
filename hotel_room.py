from room import Room

class Hotel_Room(Room):
    def __init__(self, price, room_no, extras):
        super().__init__(price, room_no)