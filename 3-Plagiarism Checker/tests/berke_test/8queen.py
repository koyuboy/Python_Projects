import random
import math


# Creates random state
class State(object):
    def __init__(self):
        self.state = list(random.randrange(8) for i in range(8))

# Finds all possible states and return as list of states
def nearStates(state):
    nearStates = []

    for row in range(8):
        for col in range(8):
            if col != state[row]:
                aux = list(state)
                aux[row] = col
                nearStates.append(list(aux))
    return nearStates

# Counts how many collision on state
def countAttacks(board):
    h = 0
    for i in range(8):
        for j in range(i + 1,8):
            if board[i] == board[j]:
                h += 1

            offset = j - i
            if board[i] == board[j] - offset or board[i] == board[j] + offset:
                h += 1
     
    return h

# picks randomly one of the best state
def bestNearState(state):
    states = nearStates(state)
    index_of_states = dict(zip(range(0,56), map(lambda state: countAttacks(state), states)))
    min_val = min(index_of_states.values())
    res = list(filter(lambda x: index_of_states[x]==min_val, index_of_states))
    random_index = random.choice(res)
    return states[random_index]

# hillclimb algorithm
def hillClimb(state):
    f = open("output.txt", 'a')
    f.write("Initial State: " + str(state) + "\n")
    f.write("Attack Count: " + str(countAttacks(state)) + "\n\n")

    if not countAttacks(state):
        f.write("Initial state is goal state\n")
        print(state)
        return
    nextState = None
    it = 1
    while(countAttacks(state)):
        nextState = bestNearState(state)
        if(countAttacks(nextState) >= countAttacks(state)):
            f.write("NO SOLUTION\n\n")
            f.close()
            return
        f.write("Iteration: " + str(it) + "\n")
        it += 1
        f.write(str(nextState) + "\n")
        f.write("Attack Count: " + str(countAttacks(nextState)) + "\n\n")
        print(nextState)
        print(countAttacks(nextState))
        state = nextState
    f.write("SOLUTION FOUND\n\n")
    f.close()
    return state





if __name__ == "__main__":

    # CREATE FILE FLUSH AND CLOSE
    f = open("output.txt",'w')
    f.flush()
    f.close()

    for i in range(1,11):
        f = open("output.txt", 'a')
        s = State()
        print(s.state)
        f.write("\t\tRandom " + str(i) + "\n")
        f.close()
        print("----------------")
        hillClimb(s.state)       


