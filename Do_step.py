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
############## know Number of stones ###################
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
            

###### finish game #### to test it comment the return none with [0,0,0,0,0,0, 3,4, 4, 4, 4, 4, 4, 0]
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

game_state = {
    "player": 0 ,
    "score": 2,
    "mancala_state":[4, 4, 4, 4, 4, 0, 0,
                     4, 4, 4, 4, 4, 4, 0],
    "steps": [],
    "end_game": 0
}
# is_stealing = input('enter 1 for stealing mode')

print(do_step(game_state, 1 ,True))



