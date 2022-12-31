import random
from typing import Any

# Write a program that simulates minesweeper game. 
# Create a grid with 8X8 with 10 random bombs; 
# print hidden grid; take input coordinates to open; check for a bomb; update hidden grid; etc. 
# Draft code for minesweeper, you can find in the materials folder. 
import numpy as np


## in main.py:
## Asignee: Yevgen Gavryliuk
## Determine and parse all incoming arguments
## FIELD_SIZE, BOMBS_AMOUNT [DIFFICULTY]


def visualize_matrix(field_size:int, matrix:list[list]) -> None:
    print('  ', end='')
    for i in range(field_size):
        print(i, end=' ')
    else:
        print()

    ## TODO: make more beatifull elements
    ## TODO: Add extra titles skins (opened free, opened number, mines marker, bomb exploded)
    ## Assignee: Mike Matvieiev
    for i, row in enumerate(matrix):
        print(i, end=' ')
        print(' '.join([str(element) for element in row]))




def get_user_input() -> tuple[str, tuple[int, int]]:
    move = input('Enter coordinates, separated by \'.\'')
    ## TODO: Check user input
    ## TODO: Add user options: mine and safe
    ## mine 1.2
    ## safe 0.1
    ## m 1.2
    ## s 0.3
    ## Asignee: Maksym Larionenko
    move = tuple([int(coordinate) for coordinate in move.split('.')])
    return move
    # frozendict
    # pip install frozendict
    # {
    #     'type': 'mine',
    #     'coordinates': (1,2)
    # }


def check_if_game_finished(matrix: list[list], bombs:list[tuple], move:tuple[int, int]) -> dict:
    ## Marharyta Himiranova
    if move in bombs:
        is_dead = True
    else:
        is_dead = False
        # TODO: loop moves
    # return is_dead
    # {
    #     'status': Any('continue','end_game'),
    #     'end_game_status': Any('win', 'lose')
    # }
    # 

def init_game(*args):
    ## TODO: change char to actual ceil status
    ## Matrix:
    ## {
    ##        'bomb': True / False
    ##        'bombs_near' : 0-8
    ##        'opened': True / False
    ## }
    ## Bombs:
    ## [(1,2), (0,5) ...]
    ## Asignee: Oksana Stepanova
    matrix = [[SOLID_CHAR for i in range(FIELD_SIZE)] for j in range(FIELD_SIZE)]
    bombs = [(random.randint(0,FIELD_SIZE-1), random.randint(0,FIELD_SIZE-1)) for i in range(BOMBS_AMOUNT)]
    return matrix, bombs, game_status

def open_field_part(*args) -> None:
    ##TODO: DEcide, which ceils should be opened together
    ## Asignee: Oleksandr Deineka
    ...


def execute_open_command(ceil):
    ## Asignee: Denis Zamaratsky
    if ceil.bombs_near == 0:
        open_ceil(ceil)
    else:
        open_field_part()

def open_ceil(matrix, ceil:tuple[int, int]) -> None:
    ## Asignee: Denis Zamaratsky
    ...

def mark_as_mine(matrix, ceil:tuple[int, int]) -> None:
    ## Asignee:  Denis Zamaratsky
    ...

def main_loop(matrix, bombs, game_status) -> dict:
    ## 
    ## Asignee: Alex Johar
    ...
    return game_status


FIELD_SIZE = 8
BOMBS_AMOUNT = 10
# DIFFICULTY = 
EMPTY_HOLE_CHAR = '#'
SOLID_CHAR = 0
BOMB_CHAR = '*'

## Global TODO: Add functions

## TODO: Optional : add high level loop


matrix, bombs, is_dead = init_game()
print(bombs)
while True:
    visualize_matrix(FIELD_SIZE, matrix)
    if is_dead:
        print('Tou are dead!')
        break
    ## TODO: Add alternative game end condition

    move = get_user_input()
    is_dead = check_if_game_finished(matrix, bombs, move)
    matrix[move[1]][move[0]] = BOMB_CHAR if is_dead else EMPTY_HOLE_CHAR



# print(matrix)
# print(bombs)

