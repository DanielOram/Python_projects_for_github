__author__ = 'Daniel Oram'
#this program writes the maze to a text file that is by default 100 lines long.
#it will terminate as opposed to the simple_maze_one_liner..
import random

file = open('maze.txt', 'a+')
file.seek(0)
file.truncate()
def drawMazeToFile():
    for i in range(100):
        file.write("#")
        length = 0
        while length<100:import random;file.write(str(random.choice(' |_'))); length+=1 #this is the one line maze generator
        file.write("#\n")

drawMazeToFile()
file.close()