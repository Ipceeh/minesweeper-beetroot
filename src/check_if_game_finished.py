"""Function to check if the game is finished."""
from frozendict import frozendict


def check_if_game_finished(matrix:'list[list]', bombs:'list[tuple]', move:'frozendict[str:str,tuple]', empty_hole_char:'str') -> 'dict':
    game_status = {
                    'status': 'continue',
                    'end_game_status': None,
                  }

    if move['move_type'] == 'safe' and move['coordinates'] in bombs:
        game_status['status'] = 'end_game'
        game_status['end_game_status'] = 'lose'

    if move['move_type'] == 'safe' and move['coordinates'] not in bombs:
        open_safe_cells = 0
        for row in matrix:
            open_safe_cells += row.count(empty_hole_char)

        if open_safe_cells == (len(matrix) ** 2 - len(bombs)):
            game_status['status'] = 'end_game'
            game_status['end_game_status'] = 'win'

    return game_status
