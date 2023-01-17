#def init_game(*args):
    ## TODO: change char to actual ceil status
import random
from typing import Any

    ## Matrix:
    ## {
    ##        'bomb': True / False
    ##        'bombs_near' : 0-8
    ##        'opened': True / False
    ## }
    ## Bombs:
    ## [(1,2), (0,5) ...]
    ## Asignee: Oksana Stepanova
   # matrix = [[SOLID_CHAR for i in range(FIELD_SIZE)] for j in range(FIELD_SIZE)]
    #bombs = [(random.randint(0,FIELD_SIZE-1), random.randint(0,FIELD_SIZE-1)) for i in range(BOMBS_AMOUNT)]
    #return matrix, bombs, game_status

import random
from typing import Any


def init_game(field_size: int, bombs_amount: int):

    status_game = {

            'status' : 'continue',
            'end_game_status' : None
            
        }

    Matrix = {

             'bomb': True or False,
             'bombs_near' : 0-8,
             'opened':True or False

           }

    
    matrix = [[0 for i in range(field_size)] for j in range(field_size)]
    bombs = []
    neirbourhood_cells = []
    
    for i in range (bombs_amount):

        duplicate = True
        while duplicate:
             x = random.randint(0,field_size-1)
             y = random.randint(0,field_size-1)  
             bomb = (y,x)
             duplicate = bomb in bombs

        
        bombs.append(tuple((y, x)))
        matrix[y][x] = '*'
        
 
        neirbourhood_cell = [
         (y-1, x-1), (y-1, x), (y, x-1), (y+1, x+1), (y+1, x), (y, x+1), (y+1, x-1), (y-1, x+1)
        ]

        neirbourhood_cell = [
            (x, y) for x, y in neirbourhood_cell if x >= 0 and x <= field_size-1 and y >= 0 and y <= field_size-1
            ]
        
        for i,j in neirbourhood_cell:
            if matrix[i][j] != matrix[y][x]:
             matrix[i][j] += 1

        neirbourhood_cells.append(neirbourhood_cell)

    for i in matrix:
            print("\t ".join(str(cell) for cell in i))
            print("")
        # Save in declared format


    # for row in matrix :
    #     for cell in row:
            
    #         if matrix[cell][row] == bomb[y][x] in bombs:
    #             Matrix['bomb'] = True
    #             Matrix['bombs_near'] = 8
    #             Matrix['opened'] = False
    #         if matrix[cell][row] == neirbourhood_cell[y][x] in neirbourhood_cells:
    #             Matrix['bomb'] = False
    #             Matrix['bombs_near'] = (''.join(str(cell) for cell in i in matrix))
    #             Matrix['opened'] = True
    #         else:
    #             Matrix['bomb'] = False
    #             Matrix['bombs_near'] = 0
    #             Matrix['opened'] = True



    
    return matrix, bombs, neirbourhood_cells, status_game, Matrix 


if __name__ == '__main__':
    
    

 init_game(8,10)


