# Tromino-Tiling-Algorithm
## Overview
This repository contains an implementation of the Tromino Tiling algorithm for tiling a 2<sup>n</sup> × 2<sup>n</sup> square grid, leaving exactly one missing square. The program recursively divides the grid, using L-shaped trominoes to cover the area without overlaps, following specific color patterns to ensure no adjacent trominoes share the same color.

## Algorithm Description
The Tromino Tiling algorithm covers a grid of size 2<sup>n</sup> × 2<sup>n</sup> with a single missing square by:
1. Dividing the grid recursively into four quadrants.
2. Placing an L-shaped tromino at the center of the grid to cover one square in three of the quadrants.
3. Recursively tiling each quadrant, ensuring that only one square remains uncovered in the desired location.

## Example Output

### For n = 1:
```markdown
G X 
G G
```
### For n = 2:
```markdown
B B R R 
B G G R 
R G B B
R R B X
```
### For n = 3:
```markdown
B B R R B B R R
B G G R B G G R
R G B B R R G B
R R B X G R B B
B R R B B R R B
G G G G B G G R
R G B G B R B B
G R R B B G G X
```

## Usage
To run the program, use:
```markdown
python tromino_tiling.py <n>
```
n is the exponent for the grid size 2<sup>n</sup> × 2<sup>n</sup>, with possible values being 1, 2, 3, etc.

## Requirements
1. Python 3.x
2. Only built-in Python libraries are permitted (e.g., sys.argv and argparse).

## License
This project is developed as part of an academic assignment for the course in algorithms at the Athens University of Economics and Business.
