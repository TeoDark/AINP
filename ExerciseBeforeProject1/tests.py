rows = 'ABCDEFGHI'
cols = '123456789'

def cross(a, b):
    return [s+t for s in a for t in b]


boxes = cross(rows, cols)

row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
unitlist = row_units + column_units + square_units
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)

def grid_values(grid):
    """Convert grid string into {<box>: <value>} dict with '123456789' value for empties.

    Args:
        grid: Sudoku grid in string form, 81 characters long
    Returns:
        Sudoku grid in dictionary form:
        - keys: Box labels, e.g. 'A1'
        - values: Value in corresponding box, e.g. '8', or '123456789' if it is empty.
    """
    values = []
    all_digits = '123456789'
    for c in grid:
        if c == '.':
            values.append(all_digits)
        elif c in all_digits:
            values.append(c)
    assert len(values) == 81
    return dict(zip(boxes, values))

import numpy as np
s = ''
for i in range(81):
    rand = str(np.random.randint(0,9))
    if rand == '0':
        rand = '.'
    s+=rand

grid = grid_values(s)


def eliminate(values):
    for box in values:
        if len(grid[box]) == 1:
            for peer in peers[box]:
                values[peer] = values[peer].replace(grid[box],'')

    return values

after = eliminate(grid)


def only_choice(values):
    """Finalize all values that are the only choice for a unit.

    Go through all the units, and whenever there is a unit with a value
    that only fits in one box, assign the value to this box.

    Input: Sudoku in dictionary form.
    Output: Resulting Sudoku in dictionary form after filling in only choices.
    """
    # TODO: Implement only choice strategy here
    print(values)

    def checkSubset(values, subset):
        validValues = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for validValue in validValues:
            occurances = 0
            here = -1
            for box in subset:
                if (len(values[box]) > 1):
                    if (str(i) in values[box]):
                        occurances += 1
                        here = box
            if occurances == 1:
                values[here] = validValue

    for i in values:
        thisPeers = peers[i]
        sameLetter = i[0]
        sameNumber = i[1]
        i_rows = cross(sameLetter,cols)
        i_cols = cross(rows,sameNumber)
        i_rows.remove(i)
        i_cols.remove(i)
        i_box = 1
        i_square = []
        for square in square_units:
            for box in square:
                if(box == i):
                    i_square = list(square)
                    i_square.remove(i)
                    break
        #print(i_square)

        checkSubset(values,i_rows)
        checkSubset(values, i_cols)
        checkSubset(values, i_square)

    print(values)

#only_choice(after)

def only_choice(values):
    """Finalize all values that are the only choice for a unit.

    Go through all the units, and whenever there is a unit with a value
    that only fits in one box, assign the value to this box.

    Input: Sudoku in dictionary form.
    Output: Resulting Sudoku in dictionary form after filling in only choices.
    """
    for unit in unitlist:
        for digit in '123456789':

            dplaces = [box for box in unit if digit in values[box]]
            if len(dplaces) == 1:
                values[dplaces[0]] = digit
    print(values)
    return values

only_choice(after)