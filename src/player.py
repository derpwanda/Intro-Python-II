# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, p_name, p_room, p_inventory=[]):
        self.p_name = p_name
        self.p_room = p_room
        self.inventory = p_inventory

    def add_item(self, item):
        pass

