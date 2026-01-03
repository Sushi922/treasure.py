import random

grid=[]

#function to initialize the grid

def initialize():
    for i in range(5):
        row=[]
        for g in range(5):
            row.append("-")
        grid.append(row)
    return grid 

def placetreasure():
    row=random.randint(0,4)
    column=random.randint(0,4)
    return row,column
