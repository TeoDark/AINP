sudo = {'B3': '1256789', 'B1': '26789', 'F4': '359', 'E2': '15679', 'H7': '69', 'H2': '6789', 'E9': '12379', 'D6': '4579', 'B7': '12679', 'I8': '23589', 'A9': '5', 'F1': '36789', 'F6': '25679', 'E7': '4', 'I5': '579', 'C8': '12349', 'H9': '4689', 'I6': '5789', 'I7': '23569', 'B4': '14589', 'E4': '359', 'D5': '34579', 'A3': '12679', 'B6': '245689', 'C4': '7', 'D8': '6', 'H4': '2', 'H5': '479', 'E6': '25679', 'C9': '123469', 'C6': '245689', 'H1': '5', 'H8': '489', 'G1': '289', 'F8': '23589', 'G8': '7', 'G6': '3', 'I2': '6789', 'I4': '589', 'G5': '459', 'C1': '2689', 'G3': '289', 'G9': '12489', 'D2': '2', 'B2': '3', 'A5': '2369', 'A2': '1679', 'I3': '4', 'A4': '139', 'D4': '3459', 'H6': '1', 'A6': '269', 'G7': '1259', 'E8': '12359', 'I1': '1', 'C2': '15689', 'G2': '89', 'F3': '56789', 'D9': '13789', 'B5': '24569', 'D7': '13579', 'C3': '125689', 'E1': '3679', 'B9': '124679', 'F9': '23789', 'C5': '234569', 'I9': '23689', 'G4': '6', 'B8': '1249', 'F5': '1', 'E5': '8', 'D3': '15789', 'F2': '4', 'A8': '1239', 'C7': '12369', 'D1': '3789', 'H3': '3', 'A7': '8', 'A1': '4', 'F7': '23579', 'E3': '15679'}
print(sudo)

from utils import *

def search(values):
    "Using depth-first search and propagation, create a search tree and solve the sudoku."
    # First, reduce the puzzle using the previous function
    reduced = reduce_puzzle(values)
    if reduced == False:
        return False
    if all(len(values[s]) == 1 for s in boxes):
        print(list(len(values[s])==1 for s in boxes))
        print(all(len(values[s]) == 1 for s in boxes))
        return values
    else:
        # Choose one of the unfilled squares with the fewest possibilities
        min = 10
        here = None
        for i in values:
            if(len(values[i])<min and len(values[i])>1):
                min = len(values[i])
                here = i
        # Now use recursion to solve each one of the resulting sudokus, and if one returns a value (not False), return that answer!
        if here != None:
            for i in values[here]:
                copy = values.copy()
                copy[here] = i
                copyResult = search(copy)
                if copyResult:
                    return copyResult

        #smtos=0
        #for i in values:
        #    if(len(values[i])>1):
        #        smtos+=1
        #if(smtos>0):
        #    search(values)
        #else:
        #    return False

        #search(values)
        # If you're stuck, see the solution.py tab!

print(search(sudo))