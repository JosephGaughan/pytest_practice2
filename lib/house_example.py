class House:
    def __init__(self, number, door_colour):
        self.floors = 2
        self.number = number
        self.door_colour = door_colour

    def get_details(self):
        return f"House number {self.number} has 2 floors and a {self.door_colour} door."
    
    def repaint_door(self, new_door_colour):
        self.door_colour = new_door_colour