class Board:
    """
    Add a class description here.
    Write briefly about the purpose of the class
    """
    __BOARD_SIZE = 7
    __target_location = (3, 7)

    def __init__(self):

        # implement your code and erase the "pass"
        # Note that this function is required in your Board implementation.
        # However, is not part of the API for general board types.
        self.cars = []

    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        # The game may assume this function returns a reasonable representation
        # of the board for printing, but may not assume details about it.
        x = ''
        for i in range(self.__BOARD_SIZE):
            for j in range(self.target_location()[1] + 1):
                cord = (i, j)
                if j < self.__BOARD_SIZE:
                    if self.cell_content(cord) is not None:
                        x += ' ' + str(self.cell_content(cord)) + ' '
                    else:
                        x += ' _ '
                else:
                    if cord == self.target_location():
                        x += ' E '
                    else:
                        x += ' * '
            x += '\n\n'
        return x

    def cell_list(self):
        """ This function returns the coordinates of cells in this board
        :return: list of coordinates
        """
        # In this board, returns a list containing the cells in the square
        # from (0,0) to (6,6) and the target cell (3,7)
        lst = []
        for i in range(self.__BOARD_SIZE):
            for j in range(self.__BOARD_SIZE):
                lst.append((i, j))
                if i == self.target_location()[0] and j == self.target_location()[1] - 1:
                    lst.append((self.target_location()[0], self.target_location()[1]))

        return lst

    def possible_moves(self):
        """ This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,movekey,description) 
                 representing legal moves
        """
        # From the provided example car_config.json file, the return value could be
        # [('O','d',"some description"),('R','r',"some description"),('O','u',"some description")]
        all_moves = []

        for car in self.cars:
            car_moves = car.possible_moves().keys()
            for move in car_moves:
                if car.movement_requirements(move) != []:
                    if not self.__check_out_of_bounds(car.movement_requirements(move)[0]):
                        if self.cell_content(car.movement_requirements(move)[0]) is None:
                            all_moves.append((car.get_name(), move, 'the car ' + car.get_name() + ' can move ' + move))
        return all_moves

    def target_location(self):
        """
        This function returns the coordinates of the location which is to be filled for victory.
        :return: (row,col) of goal location
        """
        # In this board, returns (3,7)
        return self.__target_location

    def cell_content(self, coordinate):
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the car in coordinate, None if empty
        """
        # implement your code and erase the "pass"
        is_full, name = self.__check_cord_is_full(coordinate)
        if is_full:
            return name
        return None

    def add_car(self, car):
        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """
        # Remember to consider all the reasons adding a car can fail.
        # You may assume the car is a legal car object following the API.
        # implement your code and erase the "pass"
        car_name = car.get_name()

        for car_l in self.cars:
            if car_name == car_l.get_name():
                return False
        cords = car.car_coordinates()
        for cord in cords:
            if self.cell_content(cord) is not None:
                return False
            if self.__check_out_of_bounds(cord):
                return False
        self.cars.append(car)

        return True

    def move_car(self, name, movekey):
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param movekey: Key of move in car to activate
        :return: True upon success, False otherwise
        """
        cars = self.cars
        for car in cars:
            if car.get_name() == name:
                if car.movement_requirements(movekey) !=[]:
                    req = car.movement_requirements(movekey)[0]
                    if self.cell_content(req) is None and not self.__check_out_of_bounds(req):
                        return car.move(movekey)
        return False

    def __check_cord_is_full(self, coordinate):
        cars = self.cars
        for c in cars:
            if coordinate in c.car_coordinates():
                return True, c.name
        return False, None

    def __check_car_in_board(self, coordinate):
        size = self.__BOARD_SIZE - 1
        x = coordinate[0]
        y = coordinate[1]
        if x > size or y > size or x < 0 or y < 0:
            return False
        return True

    def get_board_size(self):
        return self.__BOARD_SIZE

    def __check_out_of_bounds(self, cord):
        if cord == self.target_location():
            return False
        if cord[0] >= self.__BOARD_SIZE or cord[1] >= self.__BOARD_SIZE or cord[0] < 0 or cord[1] < 0:
            return True
        return False
