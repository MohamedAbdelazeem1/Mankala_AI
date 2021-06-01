def do_step(current_state, pocket_number, is_stealing=False):
    """
    Aya
    move stones from pocket_number to the next pockets handling:
     1. the player mancala.
     2. handles if stealing mode is on.
     3. set the next player.
     4. check if all 6 pockets of a user is empty then empty the other user pockets and fill his mancala with it.

    :param is_stealing:
    :param pocket_number: from 0 to 5
    :param current_state: {
        "player": 0,
        "mancala_state":[4, 4, 0, 2, 5, 0]
    }
    :return: new_state: {
        "player": 1,
        "mancala_state":[0, 5, 1, 2, 5, 0]
    }
    """
    new_state = {
        "player": 1,
        "mancala_state": [0, 5, 1, 2, 5, 0]
    }
    return new_state


def calculate_tree(current_state, depth):
    """
    belal
    calculate depth number of future steps, and also calculating current score
    :param current_state: {
        "option": 1,
        "player": 0,
        "score": 2,
        "mancala_state":[2, 4, 0, 2, 5, 0],
        "steps": []
    }
    :param depth: number of steps to be planned
    :return: {
        "option": 1,
        "player": 0,
        "score": 2,
        "mancala_state":[2, 4, 0, 2, 5, 0],
        "steps": [
            {
                "player": 0,
                "score": 2,
                "mancala_state":[2, 4, 0, 2, 5, 0],
                "steps": [

                ]
            },
            {
                "player": 0,
                "score": 2,
                "mancala_state":[2, 4, 2, 2, 5, 0],
                "steps": [

                ]
            }
        ]
    }
    """
    current_state = {
        "player": 0,
        "score": 2,
        "mandala_state": [2, 0, 0, 2, 5, 0],
        "steps": []
    }
    if current_state['mancala_state'][0] > 0:
        new_state = do_step(current_state, 0, is_stealing=True)
        current_state['steps'].append(new_state)
    if current_state['mancala_state'][1] > 0:
        new_state = do_step(current_state, 1, is_stealing=True)
        current_state['steps'].append(new_state)


def apply_min_max_algorithm(tree, player):
    """
    khwas
    traverse the tree, apply min max algorithm and return the next step
    :param player:
    :param tree:
    :return: new state after updating the min_max variable
    """
    pass


def think_of_move(current_state):
    """
    Esraa
    1. calculate tree
    2. apply min max algorithm
    3. do_step
    :param current_state:
    :return: new_state {
        "player": 0,
        "score": 2,
        "mancala_state":[4, 4, 0, 4, 4, 0],
        "steps": []
    }
    """
    new_state = {
        "player": 0,
        "score": 2,
        "mancala_state": [4, 4, 0, 4, 4, 0],
        "steps": []
    }
    return new_state


def winner(current_state):
    """
    Esraa
    check if the game is finished by looking at each user six pockets (if all is empty then the game is finished)
    :param current_state:
    :return: 0 for player0, 1 for player1, None if the game is still running
    """
    return None


def main():
    game_state = {
        "player": input('enter 0 if you want to start'),
        "score": 2,
        "mancala_state": [4, 4, 0, 4, 4, 0],
        "steps": []
    }
    is_stealing = input('enter 1 for stealing mode')

    while winner(game_state) is None:
        if game_state['player'] == 0:
            # read user input:
            user_input = input('Enter number from 0 to 5')
            step_output = do_step(game_state, user_input, is_stealing)
            game_state['mancala_state'] = step_output['mancala_state']
            game_state['player'] = step_output['player']
        else:
            new_state = think_of_move(game_state)
            game_state = new_state

    print(game_state)
