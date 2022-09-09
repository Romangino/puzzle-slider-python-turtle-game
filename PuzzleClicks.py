"""
    Gino Romanello
    CS5001 - Fall 2021
    Final Project - Puzzle Clicks

    This program is the puzzle file reader, puzzle creator, thumbnail
    creator, and move counter
"""
import time
import glob

from Leaderboard import Leaderboard
from BoardLayout import BoardLayout
import turtle
import random


class PuzzleClicks:
    """
    Class: PuzzleClicks
    Attributes: player_name, moves
    Methods: puzzle_data, update_puzzle, moves_number, check_moves,
    puzzle_thumbnail, create_turtle_pieces, puzzle_pieces, click_controller,
    swap_tiles, check_win, reset_button, load_button, click_coordinates
    """
    def __init__(self, player_name, moves):
        """
        Constructor -- creates puzzle and thumbnail for puzzle game
        Parameters:
           player_name - Player's name
           moves - Moves the player has to complete the puzzle
        """
        self.wn = turtle.Screen()
        self.puzzle_error_turtle = turtle.Turtle()
        self.puzzle_error_turtle.hideturtle()
        self.puzzle_dict = self.puzzle_data()
        self.moves_total = moves
        self.moves_turtle = turtle.Turtle()
        self.moves_completed = 0
        self.player_name = player_name
        self.thumbnail_gif = self.puzzle_dict["thumbnail"]
        self.total_pieces = int(self.puzzle_dict["number"])
        self.rows_columns = int(self.total_pieces ** 0.5)
        self.piece_size = int(self.puzzle_dict["size"])
        self.turtle_dict = {}
        self.ordered_numbers = list(range(1, self.total_pieces + 1))
        self.shuffle_numbers = self.ordered_numbers.copy()
        random.shuffle(self.shuffle_numbers)

    def puzzle_data(self, puzzle_file="mario.puz"):
        """
        Method -- Trys to open the puzzle file if none exist or file isn't
        in the right format an error screen will display.
        Parameters:
            puzzle_file -- The name of the puzzle file that will be used.
            Set to mario by default
        Returns:
            puz_dict -- A dictionary containing the information from the
            puzzle file
        """
        try:
            #  Opens the puzzle file and extracts the data
            with open(puzzle_file, mode="r") as infile:
                file_data = infile.read()
                file_data = file_data.split("\n")

                #  Creates a dictionary of the puzzle information
                puz_dict = {}
                for line in file_data:
                    if line != "":
                        line = line.split(": ")
                        for i in range(len(line)):
                            puz_dict[line[0]] = line[1]
                    else:
                        continue

            # Checks to make sure file has a perfect square of pieces
            total_pieces = int(puz_dict["number"])
            square_number = total_pieces ** 0.5
            if int(square_number + 0.5) ** 2 == total_pieces:
                return puz_dict
            else:
                self.wn.addshape("Resources/file_error.gif")
                self.puzzle_error_turtle.shape("Resources/file_error.gif")
                self.puzzle_error_turtle.showturtle()
                time.sleep(4)
                self.puzzle_error_turtle.hideturtle()
                print("Puzzle is in an invalid format!")

        except FileNotFoundError:
            self.wn.addshape("Resources/file_error.gif")
            self.puzzle_error_turtle.shape("Resources/file_error.gif")
            self.puzzle_error_turtle.showturtle()
            time.sleep(4)
            self.puzzle_error_turtle.hideturtle()
            print("Invalid Puzzle Name!")

    def update_puzzle(self, new_file):
        """
        Method -- Will be used when user loads a new puzzle. Loads the new
        puzzle into puzzle_data, clears the puzzle, updates the puzzle and
        thumbnail to match user's selection
        Parameters:
            new_file -- A string that will correlate to the new puzzle file
            name.
        Returns:
        """
        # Loads in new puzzle
        self.puzzle_dict = self.puzzle_data(new_file)
        self.thumbnail_gif = self.puzzle_dict["thumbnail"]

        #  Clears Puzzle and updates puzzle
        for i in range(1, self.total_pieces + 1):
            self.turtle_dict[i].hideturtle()
        self.total_pieces = int(self.puzzle_dict["number"])
        self.rows_columns = int(self.total_pieces ** 0.5)
        self.piece_size = int(self.puzzle_dict["size"])
        self.ordered_numbers = list(range(1, self.total_pieces + 1))
        self.shuffle_numbers = self.ordered_numbers.copy()
        random.shuffle(self.shuffle_numbers)
        self.turtle_dict = {}
        self.create_turtle_pieces()
        self.puzzle_pieces(self.shuffle_numbers)

        # Updates Thumbnail
        self.thumbnail.hideturtle()
        self.puzzle_thumbnail()

    def moves_number(self):
        """
        Method -- Writes the moves a player has completed and the total
        moves they have. Will be updated everytime the player makes a legal
        play
        Parameters:
        Returns:
        """
        self.moves_turtle.clear()
        self.moves_turtle.hideturtle()
        self.moves_turtle.speed("fastest")
        self.moves_turtle.up()
        self.moves_turtle.goto(-125, -280)
        self.moves_turtle.write(f"{self.moves_completed} / {self.moves_total}",
                                font=("helvetica", 30, "normal"))

    def check_moves(self):
        """
        Method -- Will be used to check if the user has used up all their
        remaining moves
        Parameters:
        Returns:
        """
        if self.moves_completed > self.moves_total:
            BoardLayout().lose()

    def puzzle_thumbnail(self):
        """
        Method -- Creates the thumbnail of the puzzle near the top of the
        leaderboard. Also gets updated when a new puzzle is loaded in
        Parameters:
        Returns:
        """
        self.wn.addshape(self.thumbnail_gif)
        #  Stamps the thumbnail
        self.thumbnail = turtle.Turtle()
        self.thumbnail.speed("fastest")
        self.thumbnail.up()
        self.thumbnail.goto(315, 330)
        self.thumbnail.shape(self.thumbnail_gif)

    def create_turtle_pieces(self):
        """
        Method -- Creates a turtle for each piece with the blank as the last
        piece
        Parameters:
        Returns:
        """
        for i in range(1, self.total_pieces + 1):
            self.turtle_dict[i] = turtle.Turtle()
            self.turtle_dict[i].speed("fastest")
            self.turtle_dict[i].hideturtle()
            self.wn.addshape(self.puzzle_dict[str(i)])
            self.turtle_dict[i].shape(self.puzzle_dict[str(i)])
            self.turtle_dict[i].up()

    def puzzle_pieces(self, list_of_numbers):
        """
        Method -- Creates the board by using the sqrt of the total pieces to
        set the length of the columns and rows
        Parameters:
            list_of_numbers -- The sequence of the puzzle pieces. a shuffled
            list is used to provide the shuffled puzzle and an ordered list
            is used when reset button is pushed
        Returns:
        """
        self.create_turtle_pieces()
        piece = 0
        y_cord = 250
        for row in range(self.rows_columns):
            x_cord = -270
            for col in range(self.rows_columns):
                self.turtle_dict[list_of_numbers[piece]].goto(x_cord, y_cord)
                self.turtle_dict[list_of_numbers[piece]].showturtle()
                piece += 1
                x_cord += self.piece_size + 3
            y_cord -= self.piece_size + 3

    def click_controller(self, x, y):
        """
        Method -- will act as the main controller for the clicks. If user
        clicks the control box buttons the appropriate method will be
        executed. If the user clicks on a puzzle that is within a certain
        distance that piece will be swapped with the blank, the moves
        completed will +1, move number will be updated, the amount of moves
        will be checked, and if the puzzle has been completed will be checked
        Parameters:
            x -- The x coordinate of the click
            y -- The y coordinate of the click
        Returns:
        """
        #  Load Button
        if (43 <= x <= 117) and (-305 <= y <= -235):
            self.load_button()
        #  Reset Button
        elif (x - 180) ** 2 + (y - -270) ** 2 <= 39 ** 2:
            self.reset_button()
        #  Quit Button
        elif (242 <= x <= 320) and (-295 <= y <= -250):
            BoardLayout().quit_button()

        else:
            for i in range(1, len(self.turtle_dict) + 1):
                if abs(x - self.turtle_dict[i].xcor()) ** 2 + \
                        abs(y - self.turtle_dict[i].ycor()) ** 2 \
                        <= (self.piece_size / 2) ** 2:
                    if self.turtle_dict[i].distance(self.turtle_dict[
                                                        self.total_pieces]) \
                            == self.piece_size + 3:

                        original_tile = self.turtle_dict[i].pos()
                        blank_tile = self.turtle_dict[self.total_pieces].pos()
                        self.swap_tiles(i, original_tile, blank_tile)
                        self.moves_completed += 1
                        self.moves_number()
                        self.check_moves()
                        self.check_win()

    def swap_tiles(self, original_turtle, original_tile, blank_tile):
        """
        Method -- if legal move is made the tile that is clicked and the
        blank tile will swap positions. Also, the list associated with the
        tiles order changed to show the correct order
        Parameters:
            original_turtle -- The number of the turtle that will be swapped
            with the blank tile
            original_tile -- The positions of the tile that will be swapped
            with blank
            blank_tile -- The position of the blank tile
        Returns:
        """
        # Swaps turtle positions
        self.turtle_dict[original_turtle].setpos(blank_tile)
        self.turtle_dict[self.total_pieces].setpos(original_tile)

        # Changes list positions
        blank = self.shuffle_numbers.index(self.total_pieces)
        other_tile = self.shuffle_numbers.index(original_turtle)
        self.shuffle_numbers[blank], self.shuffle_numbers[other_tile] = \
            self.shuffle_numbers[other_tile], self.shuffle_numbers[blank]

    def check_win(self):
        """
        Method -- Checks to see if the shuffle list matches the ordered list to
        declare a win. If win is established Leaderboard will be updated and
        board layout will change to win screen.
        Parameters:
        Returns:
        """
        if self.shuffle_numbers == self.ordered_numbers.copy():
            Leaderboard([self.moves_completed,
                         self.player_name]).update_leaderboard()
            BoardLayout().win()

    def reset_button(self):
        """
        Method -- Executed if reset button is pushed on board. Sets puzzle
        pieces in order and updates list to reflect current arrangement
        Parameters:
        Returns:
        """
        self.create_turtle_pieces()
        self.puzzle_pieces(self.ordered_numbers)
        self.shuffle_numbers = self.ordered_numbers.copy()

    def load_button(self):
        """
        Method -- Displays window for user to enter the puzzle they want
        to load. If puzzle file entered is correct and exist board will be
        updated and moves will be reset and updated
        Parameters:
        Returns:
        """
        avaliable_puzzles = glob.glob("*.puz")
        avaliable_puzzles = "\n".join(avaliable_puzzles)
        load_file = turtle.textinput(f"Load Puzzle",
                                     "Enter name of puzzle to load. Choices "
                                     f"are:\n {avaliable_puzzles}")
        self.update_puzzle(load_file)
        self.moves_completed = 0
        self.moves_number()

    def click_coordinates(self):
        """
        Method -- Used to feed x and y coordinated to click_controller and
        used to be called in main driver
        Parameters:
        Returns:
            x and y coordinated to click controller when left mouse button
            is clicked
        """
        return turtle.onscreenclick(self.click_controller, 1)
