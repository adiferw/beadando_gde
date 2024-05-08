from abc import ABC, abstractmethod

class Room(ABC):
    def __init__(self, price, room_no):
        self.price = price
        self.room_no = room_no

        @abstractmethod
        def description(self):
            pass