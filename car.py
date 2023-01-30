class Car:
    """
    Add class description here
    """

    def __init__(self, name, length, location, orientation):
        """
        A constructor for a Car object
        :param name: A string representing the car's name
        :param length: A positive int representing the car's length.
        :param location: A tuple representing the car's head (row, col) location
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL)
        """
        # Note that this function is required in your Car implementation.
        # However, is not part of the API for general car types.
        # implement your code and erase the "pass"
        self.name = name
        self.length = length
        self.location = location
        self.orientation = orientation  # horizontal is 1

    def car_coordinates(self):
        """
        :return: A list of coordinates the car is in
        """
        # implement your code and erase the "pass"

        first_location = self.location
        cords_lst = []
        for i in range(self.length):
            if self.orientation == 1:
                cords_lst.append((first_location[0], first_location[1] + i))
            if self.orientation == 0:
                cords_lst.append((first_location[0] + i, first_location[1]))
        return cords_lst

    def possible_moves(self):
        """
        :return: A dictionary of strings describing possible movements permitted by this car.
        """
        # For this car type, keys are from 'udrl'
        # The keys for vertical cars are 'u' and 'd'.
        # The keys for horizontal cars are 'l' and 'r'.
        # You may choose appropriate strings.
        # implement your code and erase the "pass"
        # The dictionary returned should look something like this:
        # result = {'f': "cause the car to fly and reach the Moon",
        #          'd': "cause the car to dig and reach the core of Earth",
        #          'a': "another unknown action"}
        # A car returning this dictionary supports the commands 'f','d','a'.
        result = {}
        if self.orientation == 0:
            result = {'u': 'move up', 'd': 'move down'}
        if self.orientation == 1:
            result = {'r': 'move right', 'l': 'move left'}
        return result

    def movement_requirements(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order for this move to be legal.
        """
        # For example, a car in locations [(1,2),(2,2)] requires [(3,2)] to
        # be empty in order to move down (with a key 'd').
        # implement your code and erase the "pass"
        empty_cells = []
        if movekey in self.possible_moves():
            if movekey == 'u':
                empty_cells.append((self.location[0] - 1, self.location[1]))
            if movekey == 'd':
                empty_cells.append((self.location[0] + self.length, self.location[1]))
            if movekey == 'r':
                empty_cells.append((self.location[0], self.location[1] + self.length))
            if movekey == 'l':
                empty_cells.append((self.location[0], self.location[1] - 1))
        return empty_cells

    def move(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: True upon success, False otherwise
        """
        # implement your code and erase the "pass"
        for key in movekey:
            move_req = self.movement_requirements(key)
            if move_req == []:
                return False
            else:
                if key == 'u':
                    self.location = (self.location[0] - 1, self.location[1])
                if key == 'd':
                    self.location = (self.location[0] + 1, self.location[1])
                if key == 'r':
                    self.location = (self.location[0], self.location[1] + 1)
                if key == 'l':
                    self.location = (self.location[0], self.location[1] - 1)
                return True

    def get_name(self):
        """
        :return: The name of this car.
        """
        # implement your code and erase the "pass"
        return self.name
