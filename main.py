import json
from copy import deepcopy

def sumArray(arr,start,end):
    sumArr = 0
    for i in range (start,end):
        sumArr = sumArr + arr[i]
    return sumArr


def do_step(current_state, pocket_number, is_stealing=False):
    """
    Aya
    move stones from pocket_number to the next pockets handling:
     1. the player mancala in unstealing mode 
     2. handles if stealing mode is on.
     3. set the next player.
     player 0 control the first 8 pockets
     player 1 control the second 8 pockets


    :param is_stealing:
    :param pocket_number: from 0 to 5
    :param current_state: {
        "player": 0,
        "mankala_state":[2, 4, 0, 2, 5, 0],
        "last_pocket" : 0

    }
    :return: new_state: {
        "player": 1,
        "mankala_state":[0, 5, 1, 2, 5, 0]
    }
    """
# know Number of stones
    n_stones = 0 
    current_state = deepcopy(current_state)

    if current_state['player'] == 0:
        start_index = pocket_number
    else:
        start_index = pocket_number + 7

    n_stones = current_state['mancala_state'][start_index]

    if n_stones == 0:
        # empty pocket
        return None

    current_state['mancala_state'][start_index] = 0

    for i in range(n_stones):
        start_index += 1
        if (current_state['player'] == 0 and start_index == 13) or (current_state['player'] == 1 and start_index == 6):
            # skip other player mancalas
            start_index += 1
        start_index = start_index % len(current_state['mancala_state'])

        current_state['mancala_state'][start_index] += 1
    # current_state["last_pocket"] = start_index


#### 0 -> 12 , 1 -> 11 , 2 -> 10 , 3 -> 9 , 4 -> 8 the relation is p1 = 2 * 6-p0 & p0 = p1- 2*(p1-6)
#### start index is the last pocket 

    if (is_stealing):
        if (current_state['player'] == 0) & ( start_index < 6) & ( current_state['mancala_state'][ start_index] == 1) :
            current_state['mancala_state'][6] = current_state['mancala_state'][6] + current_state['mancala_state'][(2*(6 -  start_index)) -  start_index]
            current_state['mancala_state'][(2*(6 -  start_index)) +  start_index] = 0

        elif (current_state['player'] == 1) & ( start_index > 6) & (current_state['mancala_state'][ start_index] == 1) :
            current_state['mancala_state'][13] = current_state['mancala_state'][13] + current_state['mancala_state'][ start_index - (2*(  start_index - 6 ))]
            current_state['mancala_state'][ start_index - (2*(start_index - 6 )) ] = 0
            

###### if the game finished
    if( (current_state['player'] == 0) & (sumArray(current_state['mancala_state'] , 0 , 6) == 0)):
        current_state['mancala_state'][13] = sumArray(current_state['mancala_state'] , 7 , 13) 
        current_state["end_game"] = 1
        for i in range(7,13):
            current_state['mancala_state'][i] = 0
        return current_state
    
    elif (current_state['player'] == 1) & (sumArray(current_state['mancala_state'] , 7, 13) == 0):
        current_state['mancala_state'][6] = sumArray(current_state['mancala_state'] , 0 , 6) 
        current_state["end_game"] = 1
        for i in range(0,6):
            current_state['mancala_state'][i] = 0
        return current_state


    if start_index != 6 and start_index != 13:
        current_state['player'] = (current_state['player'] + 1) % 2
    current_state['pocket_selected'] = pocket_number

    return current_state


def calculate_tree(current_state, depth):
    """
    belal
    calculate depth number of future steps, and also calculating current score
    :param current_state: {
        "player": 0,
        "score": 2,
        "mancala_state": [4, 4, 4, 4, 4, 4, 0,
                          4, 4, 4, 4, 4, 4, 0],
        "steps": []
    }
    :param depth: number of steps to be planned
    :return: {
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
    if depth == 0:
        return current_state
    # print(depth)
    output_state = deepcopy(current_state)

    for i in range(6):
        new_state = do_step(current_state, i)
        if new_state is not None:
            output_state['steps'].append(new_state)
    for i in range(len(output_state['steps'])):
        output_state['steps'][i] = calculate_tree(output_state['steps'][i], depth - 1)
    return output_state


def apply_min_max_algorithm(tree, player):
    """
    khwas
    traverse the tree, apply min max algorithm and return the next step
    :param player:
    :param tree:
    :return: new state after updating the min_max variable
    """
    pass


def get_heoristic_value(tree):
    return (2 * tree["mancala_state"][6] - tree["mancala_state"][6 + 7])


def min_max(tree):
    if tree["steps"] == []:
        return [get_heoristic_value(tree), tree["mancala_state"]]
    else:
        children_scores = []
        for step_tree in tree["steps"]:
            children_scores.append(min_max(step_tree)[0])
        if tree["player"] == 0:
            max_value = max(children_scores)
            max_index = children_scores.index(max_value)
            return [max_value, tree["steps"][max_index]]
        else:
            min_value = min(children_scores)
            min_index = children_scores.index(min_value)
            return [min_value, tree["steps"][min_index]]


def AI_play(current_state):
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
    tree = calculate_tree(current_state, 7)
    min_max_output = min_max(tree)
    try:
        print(f'playing: {min_max_output[1]["pocket_selected"]}')
    except Exception as e:
        print(f'error {e}')
    return do_step(current_state, min_max_output[1]['pocket_selected'])


def winner(current_state):
    """
    Esraa
    check if the game is finished by looking at each user six pockets (if all is empty then the game is finished)
    :param current_state:
    :return: 0 for player0, 1 for player1, None if the game is still running
    """
    for i in range(len(current_state['mancala_state'])):
        if i == 6 or i == 13:
            continue
        elif(current_state['mancala_state'][i]) != 0:
            return None

    if current_state['mancala_state'][6] > current_state['mancala_state'][13]:
        return 0
    else:
        return 1


def main():
    game_state = {
        "player": int(input('enter 1 if you want to start: ')),
        "score": 0,
        "is_stealing": int(input('enter 1 for stealing mode: ')),
        "mancala_state": [4, 4, 4, 4, 4, 4, 0,
                          4, 4, 4, 4, 4, 4, 0],
        "steps": []
    }

    while winner(game_state) is None:
        print(f"\n\nAI mancala: {game_state['mancala_state'][:7]}")
        print(f"your mancala: {game_state['mancala_state'][7:]}")
        if game_state['player'] == 1:
            # read user input:
            user_input = int(input('Enter number from 0 to 5: '))
            new_state = do_step(game_state, user_input)
            if new_state is not None:
                game_state = new_state
        else:
            new_state = AI_play(game_state)
            game_state = new_state


if __name__ == '__main__':
    # main()
    game_state = {
        "player": 0,
        "score": 0,
        "is_stealing": 0,
        'pocket_selected': -1,
        "mancala_state": [4, 4, 4, 4, 4, 4, 0,
                          4, 4, 4, 4, 4, 4, 0],
        "steps": []
    }

    current_state = calculate_tree(deepcopy(game_state), 2)
    x = min_max(current_state)
    print(x)
    with open('state.json', 'w') as f:
        json.dump(x, f, indent=4)
