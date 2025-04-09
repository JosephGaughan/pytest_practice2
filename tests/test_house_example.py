# import pytest
# from lib.house_example import *


# # When we build a new house
# # It needs to be given a house number and starting door colour
# # Those and the number of floors are stored in attributes
# house = House(137, "white")
# house.floors # => 2
# house.number # => 137
# house.door_colour # => "white"

# # When we have a house
# # The key details can be got back
# house = House(137, "white")
# house.get_details() # => "House number 137 has 2 floors and a white door"

# # When we have a house
# # And we change its door colour
# # This is reflected in its attribute
# house = House(24, "red")
# house.repaint_door("blue")
# house.door_colour # => "blue"



# # Test 1
# def test_house():
#     house = House(137, "white")
#     assert house.floors == 2
#     assert house.number == 137
#     assert house.door_colour == "white"

# # Test 2
# def test_get_details():
#     house = House(137, "white")
#     assert house.get_details() == "House number 137 has 2 floors and a white door."

# # Test 3
# def test_repaint_door():
#     house = House(24, "red")
#     house.repaint_door("blue")
#     assert house.door_colour  == "blue"