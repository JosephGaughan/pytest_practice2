from house_example import *


class HousingEstate:
    def __init__(self):
        self.houses = []

    def get_house_numbers(self):
        self.house_numbers = []  # Create a fresh list to store house numbers
        for house in self.houses:
            self.house_numbers.append(house.number)  # Access the `number` attribute of each house
        return self.house_numbers  # Return the list of house numbers

housing_estate = HousingEstate()

housing_estate.houses.append(House(101, "red"))
housing_estate.houses.append(House(102, "blue"))
housing_estate.houses.append(House(103, "green"))

print(housing_estate.get_house_numbers())