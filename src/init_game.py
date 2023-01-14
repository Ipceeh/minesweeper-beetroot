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

FIELD_SIZE = 8
BOMBS_AMOUNT = 10


# lower case arguments for functions
def init_game(FIELD_SIZE: int, BOMBS_AMOUNT: int): 
    # No need in solid_char, we don't track visualizing config
    
    matrix = [[0 for i in range(FIELD_SIZE)] for j in range(FIELD_SIZE)]
    bombs = []
    neirbourhood_cells = []
    
    for i in range (BOMBS_AMOUNT):

        duplicate = True
        while duplicate:
             x = random.randint(0,FIELD_SIZE-1)
             y = random.randint(0,FIELD_SIZE-1)  
             bomb = (y,x)
             duplicate = bomb in bombs
        
        bombs.append(tuple((y, x)))
        matrix[y][x] = '*' 
        
        neirbourhood_cell = [
         (y-1,x-1), (y-1,x), (y,x-1), (y+1,x+1), (y+1,x), (y,x+1), (y+1,x-1), (y-1,x+1)
        ]

        neirbourhood_cell = [
            (x,y) for x,y in neirbourhood_cell if x >= 0 and x <= FIELD_SIZE-1 and y >= 0 and y <= FIELD_SIZE-1
            ]
        
        for i,j in neirbourhood_cell:
            if matrix[i][j] != matrix[y][x]:
             matrix[i][j] += 1
            
        neirbourhood_cells.append(neirbourhood_cell)


        
       


        # Save in declared format
      

        # Create function `count_neirbohood_bombs`
        





    for i in matrix:
        print("\t ".join(str(cell) for cell in i))
        print("")
    # for i in matrix:
    #     print("\t ".join(str(cell) for cell in i))
    #     print("")



    return matrix, print(bombs), print(neirbourhood_cells)
    return matrix, bombs


if __name__ == '__main__':
    FIELD_SIZE = 8
    BOMBS_AMOUNT = 10
    

init_game(8,10)


