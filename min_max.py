# if Ai is player 0

def get_heoristic_value(tree):
    return (2*tree["mankala_state"][6] - tree["mankala_state"][6+7])

def min_max(tree):
    if tree["steps"] == []:
        return [get_heoristic_value(tree)  , tree["mankala_state"] ]
    else:
        children_scores = []
        for step_tree in tree["steps"]:
            children_scores.append(min_max(step_tree)[0])
        if tree["player"]== 0:
            max_value = max(children_scores)
            max_index = children_scores.index(max_value)
            return [max_value , tree["steps"][max_index] ]
        else:
            min_value = min(children_scores)
            min_index = children_scores.index(min_value)
            return [min_value , tree["steps"][min_index] ]

tree = {
        "player": 0,
        "score": 0,
        "mankala_state":[4,4,4,4,4,4, 0, 4,4,4,4,4,4, 0],
        "steps": [
            {
                "player": 0,
                "score": 0,
                "mankala_state":[4,4,4,4,4,0, 1, 5,5,5,4,4,4, 0],
                "steps": []
            }
            ,
            {
                "player": 0,
                "score": 0,
                "mankala_state":[0,5,5,5,5,4, 0, 4,4,4,4,4,4, 0],
                "steps": []
            }
        ]
        }

print(min_max(tree)[1])

# min_max(tree)[1] = optimum step state , min_max(tree)[0] = value
