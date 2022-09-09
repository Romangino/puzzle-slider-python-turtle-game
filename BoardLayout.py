"""
    Gino Romanello
    CS5001 - Fall 2021
    Final Project - Board Layout

    This program is the graphics for the puzzle slider game. It draws the
    splashscreen, board, buttons, lose, win, and quit screens
"""
import time
import turtle


class BoardLayout:
    """
    Class: BoardLayout
    Attributes:
    Methods: splash_screen, window_setup, puzzle_box, leaderboard_box,
    control_box, player_moves, control_buttons, run_graphics, lose, win,
    quit_button.
    """
    def __init__(self):
        """
        Constructor -- Creates new instances of wn and pen.
        Parameters:
        """
        self.wn = turtle.Screen()
        self.pen = turtle.Turtle()
        self.pen.speed("fastest")
        self.pen.hideturtle()
        self.pen.pensize(5)

    def splash_screen(self):
        """
        Method -- Creates splashscreen.
        Parameters:
        Returns:
        """
        self.wn = turtle.Screen()
        self.wn.bgpic("Resources/splash_screen.gif")
        self.wn.update()
        time.sleep(1)
        self.wn.bgpic("")

    def window_setup(self):
        """
        Method -- Creates title for window and sets dimensions and color of
        window.
        Parameters:
        Returns:
        """
        self.wn.setup(800, 800)
        self.wn.title("Puzzle Game! by Gino Romanello")
        self.wn.bgcolor("purple")

    def puzzle_box(self):
        """
        Method -- Creates the box outline for the puzzle section.
        Parameters:
        Returns:
        """
        self.pen.up()
        self.pen.goto(-330, 330)  # top left corner
        self.pen.down()
        self.pen.goto(-330, -150)  # bottom left corner
        self.pen.goto(100, -150)  # bottom right corner
        self.pen.goto(100, 330)  # top right corner
        self.pen.goto(-330, 330)  # Home top left corner
        self.pen.up()

    def leaderboard_box(self):
        """
        Method -- Creates the outline for the leaderboard section and writes
        leaderboard at the top.
        Parameters:
        Returns:
        """
        self.pen.color("red")
        self.pen.up()
        self.pen.goto(125, 330)  # top left corner
        self.pen.down()
        self.pen.goto(125, -150)  # bottom left corner
        self.pen.goto(330, -150)  # bottom right corner
        self.pen.goto(330, 330)  # top right corner
        self.pen.goto(125, 330)  # Home top left corner
        self.pen.up()
        self.pen.goto(130, 330)
        self.pen.write("Leaderboard:", font=("helvetica", 20, "normal"))

    def control_box(self):
        """
        Method -- Creates outline for the control box section.
        Parameters:
        Returns:
        """
        self.pen.pensize(5)
        self.pen.color("black")
        self.pen.up()
        self.pen.goto(-330, -180)  # top left corner
        self.pen.down()
        self.pen.goto(-330, -350)  # bottom left corner
        self.pen.goto(330, -350)  # bottom right corner
        self.pen.goto(330, -180)  # top right corner
        self.pen.goto(-330, -180)  # Home top left corner
        self.pen.up()

    def player_moves(self):
        """
        Method -- Writes out player moves in control box.
        Parameters:
        Returns:
        """
        self.pen.up()
        self.pen.goto(-320, -280)
        self.pen.write(f"Player Moves:", font=("helvetica", 30, "normal"))
        self.pen.up()

    def control_buttons(self):
        """
        Method -- Uses turtle to stamp control buttons for Load, Reset,
        and Quit.
        Parameters:
        Returns:
        """
        load_button_gif = "Resources/loadbutton.gif"
        reset_button_gif = "Resources/resetbutton.gif"
        quit_button_gif = "Resources/quitbutton.gif"
        self.wn.addshape(load_button_gif)
        self.wn.addshape(reset_button_gif)
        self.wn.addshape(quit_button_gif)
        #  Load Button
        self.pen.up()
        self.pen.goto(80, -270)
        self.pen.shape(load_button_gif)
        self.pen.stamp()
        #  Reset Button
        self.pen.goto(180, -270)
        self.pen.shape(reset_button_gif)
        self.pen.stamp()
        #  Quit Button
        self.pen.goto(280, -270)
        self.pen.shape(quit_button_gif)
        self.pen.stamp()

    def run_graphics(self):
        """
        Method -- Used to condense board graphics and will make the game board.
        Parameters:
        Returns:
        """
        self.puzzle_box()
        self.leaderboard_box()
        self.control_box()
        self.player_moves()
        self.control_buttons()

    def lose(self):
        """
        Method -- Creates screen that will be used on player loss.
        Parameters:
        Returns:
        """
        self.wn.clear()
        self.wn.bgcolor("red")
        self.wn.bgpic("Resources/Lose.gif")
        self.wn.update()
        time.sleep(3)
        turtle.bye()

    def win(self):
        """
        Method -- Creates screen that will be used on player win.
        Parameters:
        Returns:
        """
        self.wn.clear()
        self.wn.bgcolor("green")
        self.wn.bgpic("Resources/winner.gif")
        self.wn.update()
        time.sleep(3)
        turtle.bye()

    def quit_button(self):
        """
        Method -- Creates screen that will be used when player presses quit
        button.
        Parameters:
        Returns:
        """
        self.wn.clear()
        self.wn.bgcolor("purple")
        self.wn.bgpic("Resources/quitmsg.gif")
        self.wn.update()
        time.sleep(3)
        turtle.bye()
