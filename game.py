from board import Board
from car import Car
import helper, sys


class Game:
    """
    Add class description here
    """
    __LEGAL_NAMES = ['Y', 'B', 'O', 'G', 'W', 'R']
    __MOVES = ['u', 'd', 'r', 'l']

    def __init__(self, board):
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        # You may assume board follows the API
        # implement your code here (and then delete the next line - 'pass')
        self.game_board = board

    def __single_turn(self):
        """
        Note - this function is here to guide you and it is *not mandatory*
        to implement it. 

        The function runs one round of the game :
            1. Get user's input of: what color car to move, and what 
                direction to move it.
            2. Check if the input is valid.
            3. Try moving car according to user's input.

        Before and after every stage of a turn, you may print additional 
        information for the user, e.g., printing the board. In particular,
        you may support additional features, (e.g., hints) as long as they
        don't interfere with the API.
        """
        # implement your code here (and then delete the next line - 'pass')
        print(self.game_board)
        inp = input('what color to move and what direction to move it')
        if inp == '!':
            return 'finish'
        color = inp[0]
        direction = inp[2]
        while color not in self.__LEGAL_NAMES or direction not in self.__MOVES:
            print('input is invalid')
            inp = input('what color to move and what direction to move it')
            if inp == '!':
                return 'finish'
            color = inp[0]
            direction = inp[2]
        if color in self.__LEGAL_NAMES and direction in self.__MOVES:
            self.game_board.move_car(color, direction)
        return None

    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        # implement your code here (and then delete the next line - 'pass')
        x = None
        while self.game_board.cell_content(self.game_board.target_location()) is None and x is None:
            x = self.__single_turn()


def __load_json(path):
    data = helper.load_json(path)
    return data


def __get_all_cars(path):
    saved_data = __load_json(path)
    cars = []
    for i in ['Y', 'B', 'O', 'G', 'W', 'R']:
        if i in saved_data:
            item = Car(i, saved_data.get(i)[0], saved_data.get(i)[1], saved_data.get(i)[2])
            cars.append(item)
    return cars


def __load_cars(board, path):
    for car in __get_all_cars(path):
        board.add_car(car)


if __name__ == "__main__":
    inp=sys.argv[1]
    b = Board()
    if inp is None:
        Game(b).play()
    else:
        __load_cars(b, inp)
        Game(b).play()

