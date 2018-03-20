# Chris Nakovski 2018

# Precision is the number of discrete positions on the numberline.
# Higher number increase precision of results, but also slow down the runtime
# time complexity is O(precision^players)

# The current settings of precision 100 and 4 players takes 5-10 minutes to run on my home pc
precision = 100
players = 4

# Evaluates the value for all players once the bottom of the recursion has been reached
def value(moves):
    ret = {}
    moves = sorted([(i, move) for i, move in enumerate(moves)],key=lambda tup: tup[1])
    for i, move in enumerate(moves):
        if i == 0:
            ret[move[0]] = move[1] + (moves[i+1][1]-move[1])/2
        elif i == len(moves)-1:
            ret[move[0]] = precision - move[1] + (move[1] - moves[i - 1][1]) / 2
        else:
            ret[move[0]] = (moves[i+1][1]-moves[i-1][1])/2
    return ret

def recurse(level, moves):
    if level == players:
        return value(moves), []
    else:
        maxval = -1
        maxidx = -1
        maxpos = []
        vals = None
        for i in range(precision):
            if i not in moves:
                moves.append(i)
                values, positions = recurse(level+1, moves)
                if maxval < values[level]:
                    maxval = values[level]
                    maxidx = i
                    maxpos = positions
                    vals = values
                del moves[-1]
        return vals, [maxidx] + maxpos


if __name__ == '__main__':
    vals, pos = recurse(0, [])
    for i in range(players):
        print("Player " + chr(ord('A')+i) + ": takes position " + str(pos[i] / precision) + " with probability " + str(vals[i] / precision) + " of winning")
