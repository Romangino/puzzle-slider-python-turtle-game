"""
    Gino Romanello
    CS5001 - Fall 2021
    Final Project - Puzzle Game

    This program will be the driver for the puzzle game and will run all the
    components necessary to play the game. If there is an error during the
    playing of the game an entry into the 5001_puzzle.err file will be made
    and the game will be closed.
"""
import turtle
from BoardLayout import BoardLayout
from PuzzleClicks import PuzzleClicks
from Leaderboard import Leaderboard


def player_name():
    """
    Function -- player_name
        This function will prompt the user to enter in their name
    Parameters:
    Returns: the name the user enters
    """
    name = turtle.Screen().textinput("Puzzle Slider", "Enter in your name:")
    return name


def player_moves():
    """
    Function -- player_moves
        This function prompts the user to enter the amount of moves they
        want to complete the puzzle. If the number is out of range the
        prompt will be displayed again
    Parameters:
    Returns: The number of moves the user wants to have available
    """
    moves = 0
    while moves < 5 or moves > 200:
        moves = int(turtle.Screen().textinput("Puzzle Slider - Moves",
                                              "Enter the number of moves (5 "
                                              "- 200):"))
    return moves


def main():
    try:
        board_layout = BoardLayout()
        board_layout.window_setup()
        board_layout.splash_screen()

        puzzle_click = PuzzleClicks(player_name(), player_moves())
        leaderboard = Leaderboard()

        board_layout.run_graphics()
        leaderboard.read_leaderboard()
        leaderboard.sort_leaderboard()
        leaderboard.draw_leaderboard()

        puzzle_click.moves_number()
        puzzle_click.puzzle_thumbnail()
        puzzle_click.puzzle_pieces(puzzle_click.shuffle_numbers)
        puzzle_click.click_coordinates()

        turtle.done()

    except Exception as error:
        with open("5001_puzzle.err", mode="a") as outfile:
            outfile.write(f"An error happened - {error}\n")


if __name__ == '__main__':
    main()
