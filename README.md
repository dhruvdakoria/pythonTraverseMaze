# pythonTraverseMaze
The python code generates a maze and efficiently traverses through it.

mazeGenerator.py - Random Maze Generator
    On passing rows and columns the mazeGen function, it creates a random maze string.

mazeTraversal.py - Contains the algorithm for traversal through the maze
    The maze string is passed to createMazeMatrix function which converts it into a 2d array matrix. traverseMaze function then uses this 2d array to figure out the path to the '#' starting at '@'; Start coordinates: (1,0) ; End at '#'; Uses 'X' for the path.
