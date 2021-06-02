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
##############know Number of balls
    Noballs = 0 
    new_state = current_state
    mancala = 0 
    if (pocket_number>6):
        mancala = 1


##start from 0 to 13
    for i in range (len(current_state["mankala_state"])):
        if (i == pocket_number):
            Noballs = current_state["mankala_state"][i]

    new_state["mankala_state"][pocket_number] = 0

    for i in range ( Noballs ):
        if (((pocket_number + i + 1 ) == 6+(14*mancala)) & ( current_state["player"] == 1)):
            i+=1
            mancala+=1

        elif (((pocket_number + i + 1) == 13+(14*mancala)) & ( current_state["player"] == 0)):
            i+=1
            mancala+=1

        if (pocket_number + 1 + i  >=len(current_state["mankala_state"])):
            new_state["mankala_state"][(pocket_number + 1 + i - len(current_state["mankala_state"]))] += 1
            new_state["last_pocket"] = pocket_number + i + 1 - len(current_state["mankala_state"])
        else:
            new_state["mankala_state"][pocket_number + i + 1] += 1
            new_state["last_pocket"] = pocket_number + i + 1

    print (new_state["last_pocket"])
##############change player from 1 to 0 or opps.. 
    if current_state["player"] == 0 & new_state["last_pocket"] != 6 :
        new_state["player"] = current_state["player"] + 1
    elif current_state["player"] == 0 & new_state["last_pocket"] != 13 :
        new_state["player"] = current_state["player"] - 1 
    return new_state



game_state = {
    "player": 1 ,
    "score": 2,
    "mankala_state": [2,1,2,5,2,5,0,2,5,2,5,2,5,0],
    "steps": [],
    "last_pocket": 0
}
# is_stealing = input('enter 1 for stealing mode')

print(do_step(game_state, 8 ,True))

### تظبيط لعدد المرات الي بيدخل فيها ويround
### tzbeet my7otsh fe el nos m3 player 1
### in case the pocket = 0
###


