"""
The universe of the Game of Life is an infinite two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, alive or dead, or "populated" or "unpopulated".
Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent.

At each step in time, the following transitions occur:
******************************************************************************************************
   1. Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
   2. Any live cell with two or three live neighbours lives on to the next generation.
   3. Any live cell with more than three live neighbours dies, as if by overpopulation.
   4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
*******************************************************************************************************

The initial pattern constitutes the seed of the system.

The first generation is created by applying the above rules simultaneously to every cell in the seed—births and deaths occur simultaneously,
and the discrete moment at which this happens is sometimes called a tick (in other words, each generation is a pure function of the preceding one).

The rules continue to be applied repeatedly to create further generations.
"""

import tkinter as tk
import random


class Square:
    """
        A cell which can either be off or on.
        This cell is the representation of a civilisation or a person.
        Is a spot on a grid.
    
        :ivar tuple  coords:        The coordinates of the square. (Needs x, y attributes)
        :ivar int    length:        The length of the window
        :ivar bool   state:         The state of the square (On or Off)
        :ivar string active_col:    The colour to be displayed if the square is on
        :ivar string inactive_col:  The colour to be displayed if the square is off
    """

    def __init__(self, coords, length, size, state=False, active_col='black', inactive_col='white'):

        self.length = length                   # Size of map
        self.coords = coords                   # Top left corner
        self.size = size                       # Length of one side
        self.state = state                     # Alive or dead
        self.active_colour = active_col        # Colour if alive
        self.inactive_colour = inactive_col    # Colour if dead

    def rect(self):
        """
            Gives the bottom right values of the square
    
            :return: (x+size, y+size)
            :rtype:  tuple
        """
        return (self.coords[0]+self.size, self.coords[1]+self.size)

    def inbounds_square(self, coord):
        """
            Deprecated function.
            
            Returns if a coordinate is within the square. 
            
            :param   tuple coord: The coordinate of the point to test whether it is within the square. 
            :return: Whether the given coordinate is within the square
            :rtype:  bool
        """

        (x, y) = coord
        (t_l_x, t_l_y) = self.coords
        (b_l_x, b_l_y) = self.rect()

        return (t_l_x < x < b_l_x) and (t_l_y < y < b_l_y)

    def _inbounds_map(self, coord):
        """
            Test whether a point is within the map.
    
            :param   Entity coord: The coordinate to test. (Needs x, y attributes)
            
            :return: True if square in map False if square outside of map
            :rtype:  bool
        """
        (x, y) = coord

        #  Checks if x value is >= 0 and if the right side of the square is not off the board as x value is top left
        #  Checks if y value is >= 0 and if the bottom side of the square is not off the board as y value is top left
        return (0 <= x <= self.length-self.size) and (0 <= y <= self.length-self.size)

    def neighbours(self):
        """
            Neighbours around the square within the map.
            
            :return:  Neighbour coordinates which are within the map
            :rtype:   list
        """

        (x, y) = self.coords
        #  filter(func, iterable) loops over each value and keeps the value if the function called per value is true.
        #  I convert back to list as filter object isn't easy to deal with in my program
        #  Each item in the list is dictated by the current x or y +/- size.
        return list(filter(self._inbounds_map,
                           [(x-self.size, y+self.size), (x, y+self.size), (x+self.size, y+self.size),
                            (x-self.size, y),                                       (x+self.size, y),
                            (x-self.size, y-self.size), (x, y-self.size), (x+self.size, y-self.size)]
                           )
                    )

    def get_colour(self):
        """
            Returns the colour that should be displayed for the square
            
            :return: active_colour if alive else inactive_colour
            :rtype:  string
        """

        return self.active_colour if self.state else self.inactive_colour

    def rules(self, squares_dict):
        """
            Alters the Square due to rules of the game.
        """
        alive_neighbours = 0
        #  Looping through each neighbouring square
        for n in self.neighbours():
            #  Getting the object from the dictionary of objects
            neighbour = squares_dict[n]
            #  If the neighbour is alive
            if neighbour.state:
                #  Increment the counter of alive neighbours
                alive_neighbours += 1

        # If the square is alive
        if self.state:
            #  RULE 1.
            if alive_neighbours < 2:
                #  Kill the square
                self.state = False
            # RULE 3.
            elif alive_neighbours > 3:
                #  Kill the square
                self.state = False
            # RULE 2.
            else:
                #  Keep it alive
                pass

        # If the square isn't alive
        else:
            #  RULE 4.
            if alive_neighbours == 3:
                #  Bring the square to life
                self.state = True


class Grid:
    """
        The grid for which all squares lie upon. Squares are created, destroyed and manipulated within this class
        
        :ivar int    length:        The length of the side of the map
        :ivar int    size:          The size of the side of each square
        :ivar float  tolerance:     The minimum for a random float to be to set a square to alive
        :ivar string active_col:    The colour set for an active square
        :ivar string inactive_col:  The colour set for an inactive square
    """

    def __init__(self, length, size, tolerance, active_col='black', inactive_col='white'):

        self.length = length
        self.tolerance = tolerance
        self.active_col = active_col
        self.inactive_col = inactive_col
        self.square_size = size

        self.squares = self.make_squares(self.square_size)

    def make_squares(self, size):
        """
            Creates a dictionary of squares, setting them on or off. The state is determined by self.tolerance.

            :param    int size: The size to make each square. Passes into the Square object
            
            :return:  dictionary of {coordinates: Square} so as to speed up search for each square later on
            :rtype:   dict
        """

        squares = {}
        #  (Rows) Loop through the 'length' in steps of 'size' (so as to get the right top left corner each time)
        for y in range(0, self.length, size):
            #  (Cells) Loop through the 'length' in steps of 'size' (so as to get the right top left corner each time)
            for x in range(0, self.length, size):
                squares[(x, y)] = Square((x, y),
                                         self.length,
                                         size,
                                         active_col=self.active_col,
                                         inactive_col=self.inactive_col)

        return squares

    def _set_squares(self, on_coordinates):
        """
            Sets squares to on or off. Need to run after __init__ has run so as to not run into any errors.
            Not used
            
            :param list on_coordinates: A list of coordinates to set on. 
        """
        #  Loops through the dictionary of squares
        for coord, square in self.squares:
            #  If the square is in the list of coordinates
            if coord in on_coordinates:
                #  Square is alive
                square.state = True

    def enforce_rules(self):
        """
            Enforces the rules in each square.
        """

        for coords, square in self.squares.items():
            square.rules(self.squares)


class App:
    """
        Essentially the main function of the script. Creates a tkinter window and displays the images.
        
        :ivar int    length:          The length of the window
        :ivar int    size:            The size of each square. NEEDS TO BE A FACTOR OF LENGTH.
        :ivar float  tolerance:       The random float minimum to set a square to active
        :ivar int    refresh_speed:   (Millisecs) The speed at which to refresh the screen: Fast pc for speeds < 100
        :ivar string active_col:      The colour set for active squares
        :ivar string inactive_col:    The colour set for inactive squares
    """

    def __init__(self, length, size, tolerance=0.8, refresh_speed=50, active_col='#3380FF', inactive_col='#FF33FF'):

        self.length = length
        self.size = size
        self.tolerance = tolerance
        self.refresh_speed = refresh_speed
        self.started = False  # To stop start button being pressed multiple times
        self.generation = 0  # To show the generation

        #  If the size of the boxes isn't a factor of the window size
        if not self.length % self.size == 0:
            #  The boxes don't fit evenly.
            raise Exception("The squares don't fit evenly on the screen." +
                            " Box size needs to be a factor of window size.")

        self.grid = Grid(self.length, self.size, tolerance, active_col=active_col, inactive_col=inactive_col)

        self.root = tk.Tk()
        self.root.title("Aditya's: Conway's Game of Life")

        # You can drag the mouse over the grid
        self.root.bind("<B1-Motion>", self.on_mouse_click)
        # And click
        self.root.bind("<Button-1>", self.on_mouse_click)

        # Create the canvas
        self.canvas_frame = tk.Frame(self.root).grid(row=0, column=0, rowspan=4)
        self.canvas = tk.Canvas(self.canvas_frame, height=self.length, width=self.length)
        self.canvas.grid(row=0, column=0, rowspan=4)

        # Generation label
        self.text_frame = tk.Frame(self.root).grid(row=0, column=1)
        self.generation_label = tk.Label(self.text_frame, text=("Gen: %d" % self.generation))
        self.generation_label.grid(row=0, column=1, sticky='N')

        # All the buttons
        self.buttons_frame = tk.Frame(self.root).grid(row=1, column=1, rowspan=3)
        self.start_button = tk.Button(self.buttons_frame, text="Start", command=self.start)
        self.start_button.grid(row=0, column=1, sticky='SW')
        self.clear_button = tk.Button(self.buttons_frame, text="Clear grid", command=self.clear_grid)
        self.clear_button.grid(row=1, column=1, sticky='W')
        self.stop_button = tk.Button(self.buttons_frame, text="Random grid", command=self.random_generation)
        self.stop_button.grid(row=2, column=1, sticky='NW')

        # Create the boxes
        self.items = self.update_canvas()

        self.root.mainloop()

    def on_mouse_click(self, event_origin):
        """
            Actions performed every click on the board
            
            Checks how many square_sizes go into mouse_x & mouse_y to get the number of squares horizontal and vertical.
            Then multiplies by the square_size to get its coordinates.
            This is used as it is faster than looping through each square each click.
            
            :param tkinter Event event_origin: Automatically gives the event. Mouse click.
        """

        mouse_x = event_origin.x
        mouse_y = event_origin.y
        try:
            if self.grid.squares[(((mouse_x//self.grid.square_size)*self.grid.square_size),
                                  ((mouse_y//self.grid.square_size)*self.grid.square_size))].state:

                self.grid.squares[(((mouse_x // self.grid.square_size) * self.grid.square_size),
                                   ((mouse_y // self.grid.square_size) * self.grid.square_size))].state = False
            else:
                self.grid.squares[(((mouse_x // self.grid.square_size) * self.grid.square_size),
                                   ((mouse_y // self.grid.square_size) * self.grid.square_size))].state = True

            self.update_canvas(canvas_done=True, canvas_items=self.items, generation_update=False)
        except KeyError:
            #  If click is off the grid
            pass

    def start(self):
        """
            Function called when at the start of the game. 
        """

        # Restricts the press of this button to run once.
        if not self.started:
            self.started = True
            #  Creates a loop within the mainloop
            self.root.after(self.refresh_speed, self.refresh_screen)
            #  Mainloop in tkinter, run the code and loop it until exit called

    def random_generation(self):
        """
            Function called to generate a random grid. 
        """
        for _, square in self.grid.squares.items():
            if random.random() > self.tolerance:
                square.state = True
            else:
                square.state = False

        self.generation = 0
        self.update_canvas(canvas_done=True, canvas_items=self.items)

    def clear_grid(self):
        """
            Function called to clear the grid. 
        """
        for _, square in self.grid.squares.items():
            square.state = False

        self.update_canvas(canvas_done=True, canvas_items=self.items)

    def refresh_screen(self):
        """
            Alters square states then updates canvas. Runs in an internal loop (separate loop from mainloop) 
        """

        self.grid.enforce_rules()
        self.update_canvas(canvas_done=True, canvas_items=self.items)

        # Reruns the loop
        self.root.after(self.refresh_speed, self.refresh_screen)

    def update_canvas(self, canvas_done=False, canvas_items=None, generation_update=True):
        """
            Draws to the canvas if just run program. Otherwise updates each square colour.

            :param    bool canvas_done:       Whether the canvas has already run once or not
            :param    dict canvas_items:      ONLY REQUIRED IF canvas_done == True; 
                                              Each canvas.create_rectangle object with coordinates 
                                              {coordinates: canvas.create_rectangle object}
            :param    bool generation_update: Decides whether or not to increase generation
                                         
            :return:  dictionary of {coordinates: canvas.create_rectangle object}
                                    so as to get reference to each square. Only return if run once
            :rtype:   dict
        """
        # So that clicking the mouse doesn't increase generation
        if generation_update:
            # Updates generation
            self.generation += 1
            self.generation_label.config(text='Gen: %d' % self.generation)

        # Make sures the argument isn't mutable. Just initializes canvas_items
        canvas_items = {} if not canvas_items else canvas_items

        square_items = self.grid.squares

        #  If the canvas hasn't already been populated with the .create_rect()
        if not canvas_done:
            #  Loop through the squares
            for coords, square in square_items.items():
                (b_r_x, b_r_y) = square.rect()  # The bottom right coordinates
                (t_l_x, t_l_y) = coords         # Top left coordinates

                #  Draws a rectangle and stores the data in a dict corresponding to the rectangle drawn
                #  Need this to update the rectangles' colours later
                canvas_items[coords] = self.canvas.create_rectangle(t_l_x, t_l_y,
                                                                    b_r_x, b_r_y,
                                                                    fill=square.get_colour()
                                                                    )

            return canvas_items

        # The canvas has already been populated with squares
        # Need this as tkinter doesn't draw on top.
        else:
            #  If canvas_items has been specified
            if canvas_items:
                # Loop through the canvas items
                for coords, item in canvas_items.items():
                    # Update the canvas to the new colour
                    self.canvas.itemconfig(item, fill=square_items[coords].get_colour())
            #  No canvas_items so raise a value error
            else:
                raise ValueError("No canvas_items given for re-iterating over canvas squares.")


# If running of the base script and not imported
if __name__ == '__main__':
    #  Cell Size: higher it is the faster the computer updates canvas (doesn't matter about amount of cells, just size)
    #  ^I don't know why
    app = App(150, 10, tolerance=0.8, refresh_speed=125)
