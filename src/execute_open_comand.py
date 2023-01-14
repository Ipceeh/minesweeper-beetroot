from open_field_part import open_field_part
from open_cell import open_cell


def execute_open_command(matrix:list[list], cell:tuple[int,int]) -> list[list]:
    if cell.bombs_near == 0:
        open_cell(matrix, cell)
    else:
        open_field_part(matrix, cell)
    return matrix