"""Function to check if the game is finished."""
from frozendict import frozendict


def check_if_game_finished(matrix:list[list], bombs:list[tuple], move:frozendict[str:str,tuple]) -> dict:
    game_status = {
                    'status': 'continue',
                    'end_game_status': None,
                  }

    if move['type'] == 'safe' and move['coordinates'] in bombs:
        game_status['status'] = 'end_game'
        game_status['end_game_status'] = 'lose'

    if move['type'] == 'safe' and move['coordinates'] not in bombs:
        open_safe_cells = 0
        for row in matrix:
            for cell in row:
                if cell['opened']:
                    open_safe_cells += 1

        if open_safe_cells == (len(matrix) * len(matrix[0]) - len(bombs)):
            game_status['status'] = 'end_game'
            game_status['end_game_status'] = 'win'

    return game_status
