import copy
from pprint import pprint




def open_cell(matrix, cell:tuple[int, int]) -> list[list]:
    cell_values = matrix[cell[1]][cell[0]]
    if cell_values['opened']:
        raise ValueError(f'')
    cell_values.update({'opened':True})
    return matrix

def mark_as_mine(matrix, cell:tuple[int, int]) -> list[list]:
    ...


if __name__ == '__main__':
    cell = {
        'bomb': False,
        'bombs_near': 1,
        'opened': False,
        'is_marked_bomb':False
    }

    matrix = [
        [copy.copy(cell) for j in range(3)] for i in range(3)
    ]

    pprint(open_cell(matrix, (1,0)))
    pprint(open_cell(matrix, (1,0)))