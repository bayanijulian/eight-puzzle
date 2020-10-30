


# Eight Puzzle Solver

  

This is a python console app to visually show search algorithms solving an eight puzzle.

## How To Run
This project uses version 3.8.1 🐍 Python.

```bash
    git clone https://github.com/bayanijulian/eight-puzzle.git
    cd eight-puzzle
    python puzzle.py
```

  

## What is an eight puzzle?
The puzzle is a 3x3 grid with eight numbered tiles and an empty space. A tile can be moved up, down, left, and right into the empty space. To solve the puzzle, the tiles must moved from the initial start state to the goal state. The start and goal states may be arbitrary. It's important to note that there are 9! = 362,880 possible states. But, exactly half of these states are unreachable based on the initial start state. So, the total number of reachable states is 9!/2 = 181,440 possible states. This constraint is true for any and every initial start state due to math/parity - see more [here](https://stackoverflow.com/questions/11923566/how-many-possible-states-does-the-8-puzzle-have#:~:text=The%20classical%208%2Dpuzzle%20belongs,9!%2F2%20possible%20states.)

### Simple Example
##### Start State -> Goal State
```markdown
| 1 | 2 | 3 |               | 1 | 2 | 3 |
| 4 | 8 | 5 |       ->      | 4 | 5 | 6 |
| 7 | 6 |   |               | 7 | 8 |   |
```
##### Move Tile 6 Right
```markdown
| 1 | 2 | 3 |
| 4 | 8 | 5 |
| 7 |   | 6 |
```

##### Move Tile 8 Down
```markdown
| 1 | 2 | 3 |
| 4 |   | 5 |
| 7 | 8 | 6 |
```
##### Move Tile 5 Left
```markdown
| 1 | 2 | 3 |
| 4 | 5 |   |
| 7 | 8 | 6 |
```
##### Move Tile 6 Up
```markdown
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 |   |
```
#### Winner! 
This was solved in 4 moves. This project implements the a-star search algorithm to find the optimal solution that solves the puzzle in the least amount of moves as possible.
