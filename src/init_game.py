
import random
from typing import Any
import random
from typing import Any


def init_game(field_size: int, bombs_amount: int):

    status_game = {

            'status' : 'continue',
            'end_game_status' : None
            
        }

    cell = {

             'bomb': False ,
             'bombs_near' : 0,
             'opened': False

           }

    copy_cell = cell.copy()
    
    matrix = [[copy_cell for i in range(field_size)] for j in range(field_size)]

    bombs = []
        
    for i in range (bombs_amount):

        duplicate = True

        while duplicate:

            x = random.randint(0,field_size-1)
            y = random.randint(0,field_size-1)  
            bomb = (y,x)
            duplicate = bomb in bombs

        
        bombs.append(tuple((y, x)))
        matrix[y][x]['bomb'] = True
        
 
        neirbourhood_cell = [
         (y-1, x-1), (y-1, x), (y, x-1), (y+1, x+1), (y+1, x), (y, x+1), (y+1, x-1), (y-1, x+1)
        ]

        neirbourhood_cell = [
            (x, y) for x, y in neirbourhood_cell if x >= 0 and x <= field_size-1 and y >= 0 and y <= field_size-1
            ]
        
        for i,j in neirbourhood_cell:

            if not matrix[i][j]['bomb'] :
                matrix[i][j]['bombs_near'] += 1
        

    return matrix, bombs, neirbourhood_cell, status_game


if __name__ == '__main__':
    
    

 init_game(8,10)


