'''
The universe of the Game of Life is an infinite two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, alive or dead, or "populated" or "unpopulated".
Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent.
At each step in time, the following transitions occur:

******************************************************************************************************
   • Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
   • Any live cell with two or three live neighbours lives on to the next generation.
   • Any live cell with more than three live neighbours dies, as if by overpopulation.
   • Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
*******************************************************************************************************

The initial pattern constitutes the seed of the system.
The first generation is created by applying the above rules simultaneously to every cell in the seed—births and deaths occur simultaneously,
    and the discrete moment at which this happens is sometimes called a tick 
        (in other words, each generation is a pure function of the preceding one).
The rules continue to be applied repeatedly to create further generations.
'''

import time  # So user can actually see each generation
import random  # For randomly generated worlds
import os  # For terminal only

# COMPLETED
# @name         Conway's Game Of Life Unix -- Aditya
# @namespace    /Python/GameOfLifeUnixSystems.py
# @version      1.0.17654
# @description  My own take into Conway's Game of life... It isn't the same as cells aren't deleted/born simultaneously
# @author       Aditya Putravu

# To clear the screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Randomly generated list for coordinates
def randomly(x, y, tolerance=0.5):
    list = []
    for x in range(x):
        for y in range(y):
            # The higher the tolerance, the less likely it is to be in the list
            if random.random() > tolerance:
                list.append([y,x])
                
    # Return randomly generated coordinates
    return list


def check_upper_boundaries(value, upper):
    if value >= upper:
        return True
    # else:
    return False


def check_lower_boundaries(value, lower):
    if value < lower:
        return True
    # else:
    return False

# The thing that makes this UNIX systems only as windows can't handle these codes
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Board:

    def __init__(self,
                 x,  # Size of x
                 y,  # Size of y
                 delay=0.8,  # To print on to screen
                 alive_cell='@',  # What to represent alive cells
                 dead_cell="'",  # What to represent dead cells
                 random_tolerance=0.6,  # For randomly generating the cells
                 dead_colour=bcolors.WARNING,  # Colour for dead cells
                 alive_colour=bcolors.OKBLUE):  # Colour of alive cells
            
        # Setting up variables
        self.x = x
        self.y = y
        self.alive_cell = alive_cell
        self.dead_cell = dead_cell
        self.alive_colour = alive_colour
        self.dead_colour = dead_colour
        self.tolerance = random_tolerance
        self.delay = delay
        self.generation = 0

        # Runs the game
        self.game()

    def setup(self):

        # List for all the alive cells
        alivecells = []

        gameOver = False
        finished = False  
        
        # For inputing alive cells
        print("Please specify the alive cells.\n")
        a = input("Are there any alive cells?\n<y>\n<n>\n")
        # If no cells are alive then game finish
        if a == 'n':
            finished = True
            gameOver = True

        type_of_input = input("Would you like to input:\n<1> Seperately\n<2> As a list ( ADVANCED )\n<3> Randomly generated\n")
        if type_of_input == '1':
            while not finished:
                try:

                    # X and Y coordinates validation and input
                    xcoord = int(input("What is its X co-ordinate?\n"))-1
                    # If it is bigger or smaller than board dimensions then make them re-select
                    while check_lower_boundaries(xcoord, 0) or check_upper_boundaries(xcoord, self.y):
                        print("The value given is invalid. Pick again\n")
                        xcoord = int(input("What is its X co-ordinate?\n"))-1

                    ycoord = int(input("What is its Y co-ordinate?\n"))-1
                    # If it is bigger or smaller than board dimensions then make them re-select
                    while check_lower_boundaries(ycoord, 0) or check_upper_boundaries(ycoord, self.x):
                        print("The value given is invalid. Pick again\n")
                        ycoord = int(input("What is its Y co-ordinate?\n"))-1

                    # Add to the list [x, y] so it will become nested list i.e [ [x1,y1], [x2,y2] ...]
                    alivecells.append([xcoord, ycoord])

                    # Checks how many
                    b = input("Is that it?\n<y>\n<n>\n")
                    if b == 'y':
                        finished = True

                # Incase letters or not numbers are inputted
                except TypeError:
                    print("Please enter numbers.\n")
                
                except ValueError:
                    print("Please enter numbers.\n")
            
            
            # Creates the board
            board = self.create_board(alivecells)
            self.print_board(board)

        elif type_of_input == '2':
            lists = input("Please enter all the coodinates in this format: [x1, y2], [x2, y2]...\n" +
                          "    TIP: Take into consideration that the coordinates start at 0\n"+
                          "    TIP 2: If you mess up the format the program won't run properly. In that case, choose the other method of inputting the coordinates.\n"+
                          "<1> Take me back\n")

            if lists != '1':
                try:
                    alivecells = list(eval(lists))
                except Exception as e:
                    print("\nWell you're stupid. Try the other method.\n")
                    print(e)
                    quit()
            elif lists == '1':
                self.setup()
            else:
                print('You pressed something wrong...\n Oh well I\'m going to assume that you wanted to press 1 because I warned you.\n')

            # Creates the board
            board = self.create_board(alivecells)
            self.print_board(board)
           
        # Random board
        elif type_of_input == '3':
            alivecells = randomly(self.x, self.y, tolerance=self.tolerance)
            
            # Creates the board
            board = self.create_board(alivecells)
            self.print_board(board)
            
        else:
            print("Something went wrong...\n")
            time.sleep(0.3)
            self.setup()


        return alivecells, gameOver

    def game(self):
        # Quick built board for user to see
        board = {(i, j): self.dead_cell for i in range(self.x) for j in range(self.y)}
        self.print_board(board, generation=False)

        print("PLEASE CONSIDER RUNNING IN TERMINAL FOR REFRESH AND ON UNIX DESTRIBUTION TO NOT TRY AND EDIT CODE!")
        print("IF THAT ISN'T POSSIBLE ATLEAST TRY PYCHARM IDE FOR JUST COLOURS!\n")
        
        
        # Run the setup
        alive, gameEnd = self.setup()
        #  Incase board is empty
        if gameEnd:
            # print quickly built board
            self.print_board(board)

            quit()

        # # For testing
        # alive = [[0, 0],
        #          [0, 1],
        #          [0, 2],
        #          [0, 3],
        #          [1, 0]
        #          ]
        
        # Length to run program
        hm_gens = input("How many generations would you like to run it for?\n<number>\n<F> Forever\n")

        # If set amount of generations
        if hm_gens.lower() != 'f':
            #  Define start of the board up here
            self.boarddict = self.create_board(alive)
            #  Define counter
            n = 0

            #  Try catch
            try:
                while n < int(hm_gens):
                    #  Increase generations
                    self.generation += 1
                    #  New line
                    print()
                    # Print board
                    self.print_board(self.boarddict)
                    #  Update the positions
                    self.boarddict = self.move(self.boarddict)
                    #  Let user see it visually
                    time.sleep(self.delay)

                    #  Increase counter
                    n += 1
            except Exception as e:
                print('You did not enter <F> or a number.\n Or you messed with the advanced settings.\n')
                print(e)
                print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                self.game()
        else:  # Run until stopped
            self.boarddict = self.create_board(alive)
            while True:
                # Check line 163-180 for comments
                self.generation += 1
                print()
                self.print_board(self.boarddict)
                self.boarddict = self.move(self.boarddict)

                time.sleep(self.delay)


        # d = self.create_board(alive)
        # self.print_board(d)
        # self.generation +=1
        # self.print_board(self.move(d))

    def create_board(self, alivelist):
        
        # Loop through the alivelist and set the coord to alive if alive or dead otehrwise
        board_dict = {(x,y): self.dead_cell for y in range(self.y) for x in range(self.x)}

        for coords in alivelist:
            # Y is first and then X coordinate
            board_dict[(coords[1], coords[0])] = self.alive_cell
        # print(board_dict)

        return board_dict

    def print_board(self, boarddict, generation=True):

        clear()
        if generation:  # Prints Generation
            print("Generation: ", self.generation)


        # Loops through the board and prints one by one
        for x in range(self.x):
            for y in range(self.y):
                if boarddict[(x,y)] == self.alive_cell:
                    print(self.alive_colour + boarddict[(x, y)] + bcolors.ENDC, end=' ')  # Print the colour with codes
                else:
                    print(self.dead_colour + boarddict[(x, y)] + bcolors.ENDC, end=' ')  # Print the colour with codes
            print()
        print()

    def move(self, boarddict):
        for x in range(self.x):
            for y in range(self.y):
                # If the cell is alive
                # Rules
                
                # For dead cells
                if boarddict[(x, y)] == self.dead_cell:
                
                    x_alive = x
                    y_alive = y
                    neighbours = [
                        # Shaped to be where they would be
                        # The gap is the cell itself
                        [x_alive - 1, y_alive - 1], [x_alive, y_alive - 1], [x_alive + 1, y_alive - 1],

                        [x_alive - 1, y_alive],                                 [x_alive + 1, y_alive],

                        [x_alive - 1, y_alive + 1], [x_alive, y_alive + 1], [x_alive + 1, y_alive + 1]
                    ]

                    #  Remove the neighbours which are outside the board
                    #  Its bad practice to remove whilst iterating over it so I am using another list
                    neighbours_remove = []
                    for pos in neighbours:
                        if pos[0] < 0 or pos[0] > self.x - 1:  # -1 as it starts at 0
                            neighbours_remove.append(pos)
                        elif pos[1] < 0 or pos[1] > self.y - 1:  # -1 as it starts at 0
                            neighbours_remove.append(pos)

                    # Remove the corresponding neighbours which are in the remove list

                    for object in neighbours_remove:
                        neighbours.remove(object)
                    # To not waste memory
                    neighbours_remove.clear()

                    # Counting the alive cells next to it
                    alive = 0

                    for neighbour in neighbours:
                        # If the neighbours coordinates are self.alive_cell then
                        if boarddict[(neighbour[0], neighbour[1])] == self.alive_cell:
                            alive += 1


                    # If it has exactly 3 alive next to it, it lives
                    if alive == 3:
                        boarddict[(x,y)] = self.alive_cell

                else:
                    # If the cell is alive
                    
                    x_alive = x
                    y_alive = y
                    neighbours = [
                        # Shaped to be where they would be
                        # The gap is the cell itself
                        [x_alive - 1, y_alive - 1], [x_alive, y_alive - 1], [x_alive + 1, y_alive - 1],

                        [x_alive - 1, y_alive],                                 [x_alive + 1, y_alive],

                        [x_alive - 1, y_alive + 1], [x_alive, y_alive + 1], [x_alive + 1, y_alive + 1]
                    ]

                    #  Remove the neighbours which are outside the board
                    #  Its bad practice to remove whilst iterating over it so I am using another list
                    neighbours_remove= []
                    for pos in neighbours:
                        if pos[0] < 0 or pos[0] > self.x - 1:  # -1 as it starts at 0
                            neighbours_remove.append(pos)
                        elif pos[1] < 0 or pos[1] > self.y - 1:  # -1 as it starts at 0
                            neighbours_remove.append(pos)

                    # Remove the corresponding neighbours which are in the remove list

                    for object in neighbours_remove:
                        neighbours.remove(object)
                    # To not waste memory
                    neighbours_remove.clear()

                    # Counting the alive cells next to it
                    alive = 0

                    for neighbour in neighbours:
                        # If the neighbours coordinates are self.alive_cell then
                        if boarddict[(neighbour[0], neighbour[1])] == self.alive_cell:
                            alive += 1

                    # Get number of alive next to them
                    # print(alive)
                    if alive < 2:
                        # For checking if it has less then 2 alive neighbours
                        # print("{} is going to die...".format((x,y)))
                        boarddict[(x, y)] = self.dead_cell
                    elif alive == 2 or alive == 3:
                        # boarddict[(x, y)] = self.alive_cell
                        # Don't really need to say it is going to be staying alive
                        pass
                    elif alive > 3:
                        # For checking if it has more than 3 alive neighbours
                        # print("{} is going to die...".format((x,y)))
                        boarddict[(x, y)] = self.dead_cell

        return boarddict

if __name__ == '__main__':
    gameBoard = Board(40, 70, delay=0.2, random_tolerance=0, dead_colour=bcolors.FAIL, alive_colour=bcolors.OKBLUE)


# If colours not showing, set the colour options to ''

#  Cool patterns:
#  a square --> isolated colony

#  Cool tolerance levels for 30 by 70:
#  0.9 --> shows how to world started -- ends with an isolated colony being engulfed then the world being taken over
#  0.8 --> Several small colonies merge
#  0.1 --> shows what happened ages ago when humanity was almost wiped to almost nothing but then became what we are now
#  0   --> mixture of 0.1 and 0.9 analysis
