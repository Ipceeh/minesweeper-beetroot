# Matrix visualization function

FIELD_SIZE = 10
BOMBS_AMOUNT = 10
# DIFFICULTY =
EMPTY_HOLE_CHAR = '\U0001F573'
SOLID_CHAR = '\U0001F4A2'
BOMB_CHAR = '\U0001F4A3'

matrix = [[SOLID_CHAR for i in range(FIELD_SIZE)] for j in range(FIELD_SIZE)]

def visualize_matrix(field_size:int, matrix:list[list]) -> None:
    print('    ', end='')
    for i in range(field_size):
        print(i, end='  ')
    else:
        print()
    for i, row in enumerate(matrix):
        print(i, end='  ')
        print(' '.join([str(element) for element in row]))

visualize_matrix(FIELD_SIZE, matrix)
