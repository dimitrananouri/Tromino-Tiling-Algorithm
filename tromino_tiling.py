import sys

#user input
n = int(sys.argv[1])

#square
square = []
for i in range(2**n):
    row = ['X'] * 2**n 
    square.append(row)

global flag
flag = 0 

def split(square):  #splits the square in 4 quarters
    size = len(square)
    mid = size // 2
    top_left = [row[:mid] for row in square[:mid]]
    top_right = [row[mid:] for row in square[:mid]]
    bottom_left = [row[:mid] for row in square[mid:]]
    bottom_right = [row[mid:] for row in square[mid:]]

    return top_left, top_right, bottom_left, bottom_right


def merge(top_left, top_right, bottom_left, bottom_right): #merges the four quarters
    merged_square = []
    size = len(top_left) * 2
    for i in range(size):
        if i < size // 2:
            merged_square.append(top_left[i] + top_right[i])
        else:
            merged_square.append(bottom_left[i - size // 2] + bottom_right[i - size // 2])

    return merged_square

def fillSquare(square, n, pattern):

    if n == 1:
        square[0][0], square[1][0], square[1][1] = 'G', 'G', 'G'
        return square
    
    elif n == 2:
        if pattern == 1:
            #green tromino
            square[1][2], square[1][1], square[2][1] = 'G', 'G', 'G'

            #red and blue trominos
            square[0][0], square[1][0], square[0][1] = 'B', 'B', 'B'
            square[0][2], square[0][3], square[1][3] = 'R', 'R', 'R'
            square[2][2], square[2][3], square[3][2] = 'B', 'B', 'B'
            square[2][0], square[3][0], square[3][1] = 'R', 'R', 'R'

            return square
        
        elif pattern == 2:
            #green tromino
            square[1][1], square[1][2], square[2][2] = 'G', 'G', 'G'

            #red and blue trominos
            square[0][0], square[1][0], square[0][1] = 'B', 'B', 'B'
            square[0][2], square[0][3], square[1][3] = 'R', 'R', 'R'
            square[2][3], square[3][3], square[3][2] = 'B', 'B', 'B'
            square[2][0], square[2][1], square[3][1] = 'R', 'R', 'R' 

            return square
        
        elif pattern == 3:
            #green tromino
            square[1][1], square[2][1], square[2][2] = 'G', 'G', 'G'
            
            #red and blue trominos
            square[0][0], square[1][0], square[0][1] = 'B', 'B', 'B'
            square[0][2], square[1][2], square[1][3] = 'R', 'R', 'R'
            square[2][3], square[3][3], square[3][2] = 'B', 'B', 'B'
            square[2][0], square[3][0], square[3][1] = 'R', 'R', 'R'

            return square
        
        elif pattern == 4:
            #green tromino
            square[1][2], square[2][1], square[2][2] = 'G', 'G', 'G'

            #red and blue trominos
            square[0][1], square[1][0], square[1][1] = 'B', 'B', 'B'
            square[0][2], square[0][3], square[1][3] = 'R', 'R', 'R'
            square[2][3], square[3][3], square[3][2] = 'B', 'B', 'B'
            square[2][0], square[3][0], square[3][1] = 'R', 'R', 'R'
            
            return square
        
    else:

        global flag 
        flag = flag + 1
        
        #green tromino in the middle of the square (only once)
        square_size = len(square)
        center_row = square_size // 2
        center_col = square_size // 2
        if flag==1: 
            square[center_row][center_col-1], square[center_row][center_col], square[center_row-1][center_col] = 'G', 'G', 'G'
        
        #split the square in 4 quarters 
        top_left, top_right, bottom_left, bottom_right = split(square)

        quarterSizes = len(top_left)
        center_rowQuarters = quarterSizes // 2
        center_colQuarters = quarterSizes // 2

        #top left green tromino case 
        if top_left[len(top_left)-1][len(top_left)-1] == 'G':
            top_left[center_rowQuarters][center_colQuarters-1], top_left[center_rowQuarters-1][center_colQuarters-1], top_left[center_rowQuarters-1][center_colQuarters] = 'G', 'G', 'G'
        else:
            top_left[center_rowQuarters][center_colQuarters-1], top_left[center_rowQuarters][center_colQuarters], top_left[center_rowQuarters-1][center_colQuarters] = 'G', 'G', 'G'
        
        #top right green tromino case
        if top_right[len(top_right)-1][0] == 'G':
            top_right[center_rowQuarters-1][center_colQuarters-1], top_right[center_rowQuarters-1][center_colQuarters], top_right[center_rowQuarters][center_colQuarters] = 'G', 'G', 'G'
        else:
            top_right[center_rowQuarters-1][center_colQuarters-1], top_right[center_rowQuarters][center_colQuarters-1], top_right[center_rowQuarters][center_colQuarters] = 'G', 'G', 'G'
        
        #bottom left green tromino case
        if bottom_left[0][len(bottom_left)-1] == 'G':
            bottom_left[center_rowQuarters-1][center_colQuarters-1], bottom_left[center_rowQuarters][center_colQuarters-1], bottom_left[center_rowQuarters][center_colQuarters] = 'G', 'G', 'G'
        else:
            bottom_left[center_rowQuarters-1][center_colQuarters-1], bottom_left[center_rowQuarters-1][center_colQuarters], bottom_left[center_rowQuarters][center_colQuarters] = 'G', 'G', 'G'
        
        #bottom right tromino case
        if bottom_right[0][0] == 'G':
            bottom_right[center_rowQuarters][center_colQuarters-1], bottom_right[center_rowQuarters][center_colQuarters], bottom_right[center_rowQuarters-1][center_colQuarters] = 'G', 'G', 'G'
        else: 
            bottom_right[center_rowQuarters][center_colQuarters-1], bottom_right[center_rowQuarters-1][center_colQuarters-1], bottom_right[center_rowQuarters-1][center_colQuarters] = 'G', 'G', 'G'

        
        #choose the right patterns for each quarter
        if top_left[0][0] =='G':
            pattern_topLeft = 4
        else:
            pattern_topLeft = 1

        if top_right[len(top_right)-1][0]== 'G':
            pattern_topRight = 2
        else: 
            pattern_topRight = 3

        if bottom_left[0][len(bottom_left)-1] == 'G':
            pattern_bottomLeft = 3
        else:
            pattern_bottomLeft = 2
        
        if bottom_right[0][0] =='G':
            pattern_bottomRight = 4
        else:
             pattern_bottomRight = 1

        #fill the quarters with retrospective 
        top_left = fillSquare(top_left, n-1, pattern_topLeft)
        top_right = fillSquare(top_right, n-1, pattern_topRight)
        bottom_left = fillSquare(bottom_left, n-1, pattern_bottomLeft)
        bottom_right = fillSquare(bottom_right, n-1, pattern_bottomRight)
       
        filled_square = merge(top_left, top_right, bottom_left, bottom_right)
    
        return filled_square

#output
FilledSquare = []
FilledSquare = fillSquare(square, n, 1)
for row in FilledSquare:
    print(' '.join(row))
