import random

# Write a program that simulates minesweeper game. 
# Create a grid with 8X8 with 10 random bombs; 
# print hidden grid; take input coordinates to open; check for a bomb; update hidden grid; etc. 
# Draft code for minesweeper, you can find in the materials folder. 
import numpy as np


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
    # return 'safe', (1,2)


def check_if_game_finished(matrix: list[list], bombs:list[tuple], move:tuple[int, int]) -> bool:
    ## Marharyta Himiranova
    if move in bombs:
        is_dead = True
    else:
        is_dead = False
        # TODO: loop moves
    return is_dead


def init_game(*args):
    ## TODO: change char to actual ceil status
    ## {
    ##        'bomb': True / False
    ##        'bombs_near' : 1-8
    ##        'opened': True / False
    ## }
    ## Asignee: Oksana Stepanova
    matrix = [[SOLID_CHAR for i in range(FIELD_SIZE)] for j in range(FIELD_SIZE)]
    bombs = [(random.randint(0,FIELD_SIZE-1), random.randint(0,FIELD_SIZE-1)) for i in range(BOMBS_AMOUNT)]
    return matrix, bombs, False

def open_field_part(*args):
    ##TODO: DEcide, which ceils should be opened together
    ## Asignee: Oleksandr Deineka
    ...

def open_ceil():
    ## Asignee: Denis Zamaratsky
    ...

def mark_as_mine():
    ## Asignee:  Denis Zamaratsky
    ...


FIELD_SIZE = 8
BOMBS_AMOUNT = 10
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

