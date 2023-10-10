# Conway's Game of Life

## Description:
This project implements Conway's Game of Life, a cellular automaton devised by mathematician John Conway. The game consists of a grid of cells that can be either alive or dead, and it evolves over generations based on a set of simple rules. The simulation is implemented in Python and includes the generation of an animated GIF to visualize the evolving patterns. You could adjust parameters for your needs (including size of the board, number of frames and probability of cell survival).

Conway's Game of Life Rules:

Conway's Game of Life is a cellular automaton with a simple set of rules that dictate how the state of the grid evolves over time. It was devised by mathematician John Conway and has become a classic example of emergent behavior and complexity in a simple system. The game is played on a two-dimensional grid of cells, and each cell can be in one of two states: alive or dead.

### The rules for Conway's Game of Life are as follows:

1. ### Birth: A dead cell with exactly three live neighbors becomes alive (is "born") in the next generation.

2. ### Survival: A live cell with two or three live neighbors survives to the next generation.

3. ### Death by Loneliness: A live cell with fewer than two live neighbors dies due to loneliness and becomes a dead cell in the next generation.

4. ### Death by Overcrowding: A live cell with more than three live neighbors dies from overcrowding and becomes a dead cell in the next generation.

## Code Overview:
The project consists of two main classes, Cell and Board, which work together to simulate the game.
    
#### Cell Class:

Represents each cell in the grid.
Initializes the cell's state randomly, allowing for manipulation of the probability of cell survival.
Contains a __str__ method to display the cell's state as '0' (alive), ' ' (dead), or 'X' (invalid state).

#### Board Class:

Manages the grid of cells.
Generates the initial state of cells in the board.
Checks neighbors and updates cell states based on the rules for one generation.
Displays the current state of the board.
Creates an animated GIF to visualize the simulation.

### Usage:

   1. Create an instance of the Board class with the desired width and height.
   2. Use the cellsGenerating method to generate the initial state of cells.
   3. Run the simulation using the checkingNeighbors method to evolve the game.
   4. Display the current state of the board with the showBoard method.
   5. Create an animated GIF to visualize the simulation using the creatingGif method, specifying the number of frames.

### Dependencies:

   - Python 3.x
   - NumPy
   - Matplotlib
   - svgpathtools and svgpath2mpl for SVG path parsing


Note:

- The code includes comments and documentation for clarity.
- To run the simulation, ensure you have the required dependencies installed.
- The generated animated GIF will be saved as 'gameOfLifeConway1.gif'

Feel free to explore and modify the code to experiment with different initial configurations and visualizations of Conway's Game of Life.