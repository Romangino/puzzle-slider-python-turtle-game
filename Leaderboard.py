"""
    Gino Romanello
    CS5001 - Fall 2021
    Final Project - Leaderboard

    This program will be the Leaderboard class that is responsible for
    reading, writing, and presenting the players in the leaderboard
"""

import turtle
import time


class Leaderboard:
    """
    Class: Leaderboard
    Attributes: player_info
    Methods: update_leaderboard, read_leaderboard, sort_leaderboard,
    draw_leaderboard
    """

    def __init__(self, player_info=list):
        """
        Constructor -- Creates leaderboard_turtle to be used in writing
        leaderboard names
        Parameters:
            player_info -- a list which will contain only the current user
            that won
        """
        self.player_info = player_info
        self.sorted_leaderboard = []
        self.leaderboard_turtle = turtle.Turtle()
        self.leaderboard_turtle.hideturtle()
        self.leaderboard_turtle.speed("fastest")

    def update_leaderboard(self):
        """
        Method -- Used when player wins game. Takes in the amount of moves
        needed and the name of the player
        Parameters:
        Returns:
        """
        with open("leaderboard.txt", mode="a") as outfile:
            outfile.write(f"{self.player_info[0]}:{self.player_info[1]}\n")

    def read_leaderboard(self):
        """
        Method -- Used to read the leaderboard.txt file to write leaderboard.
        If none exist an error message will pop up and close program
        Parameters:
        Returns:
        """
        try:
            with open("leaderboard.txt", mode="r") as infile:
                self.leaderboard_data = infile.read().split("\n")
                self.leaderboard_data.pop()
        except FileNotFoundError:
            turtle.Screen().addshape("Resources/leaderboard_error.gif")
            self.leaderboard_turtle.shape("Resources/leaderboard_error.gif")
            self.leaderboard_turtle.showturtle()
            time.sleep(4)
            self.leaderboard_turtle.hideturtle()

    def sort_leaderboard(self):
        """
        Method -- Sorted the Leaderboard data that is loaded in from the
        leaderboard.txt. By making a nested list and then using the sorted
        function a new sorted_leaderboard list is made
        Parameters:
        Returns:
        """
        for player in self.leaderboard_data:
            temp = player.split(":")
            self.sorted_leaderboard.append([int(temp[0]), temp[1]])
        self.sorted_leaderboard = sorted(self.sorted_leaderboard, key=lambda
            x: x[0])

    def draw_leaderboard(self):
        """
        Method -- Uses turtle to write each move : name in leaderboard box.
        Will be updated everytime game is relaunched
        Parameters:
        Returns:
        """
        self.leaderboard_turtle.up()
        self.leaderboard_turtle.goto(135, 260)
        self.leaderboard_turtle.right(90)
        for player in self.sorted_leaderboard:
            self.leaderboard_turtle.write(f"{player[0]} : {player[1]}",
                                          font=("helvetica", 15, "normal"))
            self.leaderboard_turtle.forward(20)
