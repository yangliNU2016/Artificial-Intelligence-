import copy

def hanoi(num):
    # Stack disks on the 1st peg
    first = []
    i = 0
    while num > i:
        first.append(num)
        num -= 1
    # 2nd Peg
    second = []
    # 3rd Peg
    third = []
    # Track record of states
    states = [[copy.deepcopy(first), copy.deepcopy(second), copy.deepcopy(third)]]

    # Termination state
    term = [[], [], copy.deepcopy(first)]

    # Moves (Breath-First-Search)
    states = move(states, term)

def move(states, term):
    # Open a file and write the states and progress to it
    f = open('Hanoi.txt', 'w')

    # BFS on states track
    i = 0
    while i < len(states):
        state = copy.deepcopy(states[i])
        f.write('The current state is ' + str(state) + '\n')
        j = 0
        while j < len(state):
            # The peg to unstack a disk
            peg = state[j]
            # If the peg is Not an empty stack to unstack
            if peg:
                # Top disk on the peg
                disk = peg[-1]
                k = 0
                while k < len(state):
                    # The other peg to stack on
                    anotherPeg = state[k]
                    # Not to unstack and stack on a disk on the same peg
                    # If the other peg is empty OR the other peg is "valid" to stack on
                    if (anotherPeg != peg and not anotherPeg) or (anotherPeg != peg and anotherPeg and disk < anotherPeg[-1]):
                        stateBackup = copy.deepcopy(state)
                        # Unstack the disk from the peg
                        peg.pop()
                        # Stack the disk on the other peg
                        anotherPeg.append(disk)
                        if state not in states:
                            states.append(state)
                            f.write('After a move, now game states track adds a new state ' + str(states) + '\n')
                        if state == term:
                            f.write('I found it!\n')
                            return states
                        # Recover to the current state for the rest of moves on the current state
                        state = stateBackup
                        # Recover the peg because of its change on "peg.pop()" line
                        peg = state[j]
                    k += 1
            j += 1
        i += 1
        f.write('\n')
    f.close()

if __name__ == '__main__':
    hanoi(3)
