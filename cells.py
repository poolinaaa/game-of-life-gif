import random
import numpy as np
import copy
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import matplotlib as mpl
from svgpathtools import svg2paths
from svgpath2mpl import parse_path


class Cell():
    '''class to represent each cell in the grid'''
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

        # initialize the cell's state randomly
        generatedState = random.uniform(0, 100)

        #it is possible to manipulate with probability of cell's survival
        if generatedState >= 50:
            self.state = 'alive'

        else:
            self.state = 'dead'

        self.nextState = None

    def __str__(self):

        if self.state == 'alive':
            return '0'

        elif self.state == 'dead':
            return ' '

        else:
            return 'X'


class Board():
    '''board class to manage the grid of cells'''
    
    def __init__(self, width, height):

        self.width = width
        self.height = height
        self.board = np.zeros(shape=(self.height, self.width), dtype=Cell)

    # generate the initial state of cells in the board
    def cellsGenerating(self):

        for i in range(self.height):
            for j in range(self.width):

                self.board[j, i] = Cell(j, i)

        return self.board
    
    # check neighbors and update cell states for one generation
    def checkingNeighbors(self):

        for i in range(self.height):
            for j in range(self.width):

                aliveNeighbors = 0
                # define neighbor coordinates based on cell's position
                if i == 0 and j == 0:
                    toCheck = [(self.width-1, i+1), (j, i+1), (j+1, i+1), (j+1, i), (self.height-1,
                                                                                     j+1), (j, self.height-1), (self.width-1, self.height-1), (self.width-1, i)]

                if i == 0 and j != 0:
                    toCheck = [(j-1, i+1), (j, i+1), ((j+1) % self.width, i+1), ((j+1) % self.width, i), ((
                        j+1) % self.width, self.height-1), (j, self.height-1), (j-1, self.height-1), (j-1, i)]

                if i != 0 and j == 0:
                    toCheck = [(self.width-1, (i+1) % self.height), (j, (i+1) % self.height), (j+1, (i+1) %
                                                                                               self.height), (j+1, i), (j+1, i-1), (j, i-1), (self.width-1, i-1), (self.width-1, i)]

                else:
                    toCheck = [((j-1) % self.width, (i+1) % self.height), ((j) % self.width, (i+1) % self.height), ((j+1) % self.width, (i+1) % self.height), ((j-1) % self.width, (i) % self.height),
                               ((j+1) % self.width, (i) % self.height), ((j-1) % self.width, (i-1) % self.height), ((j) % self.width, (i-1) % self.height), ((j+1) % self.width, (i-1) % self.height)]
                
                # count alive neighbors
                for k in range(8):

                    if self.board[toCheck[k]].state == 'alive':
                        aliveNeighbors += 1

                if self.board[j, i].state == 'dead':

                    if aliveNeighbors == 3:
                        self.board[j, i].nextState = 'alive'
                    else:
                        self.board[j, i].nextState = 'dead'

                elif self.board[j, i].state == 'alive':

                    if aliveNeighbors == 2 or aliveNeighbors == 3:
                        self.board[j, i].nextState = 'alive'
                    else:
                        self.board[j, i].nextState = 'dead'

        # update the cell's next state based on the rules of the game
        for i in range(self.height):
            for j in range(self.width):
                self.board[j, i].state = copy.deepcopy(
                    self.board[j, i].nextState)

    # display the current state of the board
    def showBoard(self):

        for i in range(self.height):
            print()
            for j in range(self.width):
                print(self.board[j, i], end='')
    
    # create an animated GIF to visualize the simulation
    def creatingGif(self, numOfFrames):

        fig, ax = plt.subplots()
        cell_path, attributes = svg2paths('ImageCell.svg')
        cell_marker = parse_path(attributes[0]['d'])
        cell_marker.vertices -= cell_marker.vertices.mean(axis=0)
        cell_marker = cell_marker.transformed(
            mpl.transforms.Affine2D().rotate_deg(180))
        cell_marker = cell_marker.transformed(
            mpl.transforms.Affine2D().scale(-1, 1))

        def generatingData(frames):

            x = []
            y = []

            for i in range(self.height):
                for j in range(self.width):

                    if self.board[j, i].state == 'alive':
                        x.append(j)
                        y.append(i)
            ax.clear()
            ax.scatter(x, y, marker=cell_marker, color='green', s=80)
            plt.title("Conway's game of life\nauthor: Pola Borkowska")
            plt.axis('off')

            self.checkingNeighbors()

        self.total_frames = numOfFrames
        animationBoard = FuncAnimation(
            fig, generatingData, frames=self.total_frames, interval=200)
        animationBoard.save('gameOfLifeConway1.gif',
                            dpi=80, writer='imagemagick')
        plt.close()
