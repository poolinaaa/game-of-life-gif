from cells import Board

#create board for the game
tab = Board(30,30)

#generate cells with random state
tab.cellsGenerating()

#turn the board into gif with selected number of frames (iterations of dying and birth)
tab.creatingGif(numOfFrames=100)