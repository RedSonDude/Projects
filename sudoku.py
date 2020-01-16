import math
import time

start = time.time()

def importGrid(file):
    '''
    Imports the text file and parses it into a list
    Args:
        file (txt): The imported file
    Returns:
        list: A 2D list of the grid
    '''
    with open(file,"r") as f:
        grid = []
        for line in f:
            row = line.rstrip().split(",")
            while len(row)<9:
                row.append('')
            grid.append(row)
    return grid

def initOptions(grid):
    options = []
    for row in grid:
        for square in row:
            if  square == '':
                options.append([1,2,3,4,5,6,7,8,9])
            else:
                options.append([])
    return options

def testColumn(option, column):
    '''
    Return
        bool: Whether this option is possible in this column
    '''
    return not str(option) in column

def testRow(option, row):
    '''
    Return
        bool: Whether this option is possible in this row
    '''
    return not str(option) in row

def testBox(option, box):
    '''
    Return
        bool: Whether this option is possible in this box
    '''
    return not str(option) in box

def testOption(option, position, grid):
    # Row functions
    row = grid[math.floor(position / 9)]

    rowWorks = testRow(option, row)

    # Column functions
    columnNum = position % 9
    column = [row_i[columnNum] for row_i in grid]

    columnWorks = testColumn(option, column)

    # Box functions: list of 3 in row + list of 3 in row + list of 3 in row
    boxX = (math.floor((position % 9)/3)) * 3
    boxY= (math.floor(position / 27)) * 3
    box = grid[boxY][boxX:boxX+3] + grid[boxY+1][boxX:boxX+3] + grid[boxY+2][boxX:boxX+3]

    boxWorks = testBox(option, box)

    return rowWorks and columnWorks and boxWorks

def refineOptions(grid, options):
    newOptions = []
    # squareNum is the index of the option
    for squareNum in range(len(options)):
        if len(options[squareNum]) > 0:
            newOption = []
            # option is one possible number for that square
            for option in options[squareNum]:
                # position is the index of that square
                position = squareNum
                if testOption(option, position, grid):
                    newOption.append(option)
            newOptions.append(newOption)
        else:
            newOptions.append(options[squareNum])
    return newOptions

def updateGrid(grid, options):
    improved = False
    for optionNum in range(len(options)):
        if len(options[optionNum]) == 1:
            improved = True
            myguess = str(options[optionNum][0])
            grid[math.floor(optionNum / 9)][optionNum % 9] = str(options[optionNum][0])
    return improved

def initTrials(options):
    trials = []
    for squareNum in range(len(options)):
        if len(options[squareNum]) > 0:
            trials.append([squareNum, 0])
    return trials

def printAns(grid):
    answer = []
    for line in grid:
        row = ''
        for square in line:
            row = row + str(square) + ','
        row = row[:-1]
        print(row)

grid = importGrid("grid3.txt")
options = initOptions(grid)

improved = True

while improved:

    options = refineOptions(grid, options)
    improved = updateGrid(grid, options)

trials = initTrials(options)

testNum = 0

while testNum < len(trials):

    squareNum = trials[testNum][0]
    guess = options[squareNum][trials[testNum][1]]

    if testOption(guess, squareNum, grid):
        grid[math.floor(squareNum / 9)][squareNum % 9] = str(guess)
        trials[testNum][1] += 1
        testNum += 1

    else:
        if trials[testNum][1] < len(options[trials[testNum][0]]) - 1:
            trials[testNum][1] += 1
        else:
            while True:
                trials[testNum][1] = 0
                testNum -= 1
                grid[math.floor(trials[testNum][0] / 9)][trials[testNum][0] % 9] = ''
                
                if trials[testNum][1] < len(options[trials[testNum][0]]):
                    break

printAns(grid)

stop = time.time()

print('')
print('Solved in', stop - start, 'seconds')




