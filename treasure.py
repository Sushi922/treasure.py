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

def givehints(treasurerow,treasurecolumn,guessrow,guesscolumn):
    if guesscolumn > treasurecolumn:
        return "move left"
    
    if guesscolumn < treasurecolumn:
        return "move right"
    
    if guessrow > treasurerow:
        return "move up"
    
    if guessrow < treasurerow:
        return "move down" 
    
    return "Congratulations! you have found the treasure!"
    
def treasurehunt():
    grid=initialize()
    treasurerow,treasurecolumn=placetreasure()
    print("Welcome to the treasure hunt game!:D")
    attempts=0

    while True:
        print("\nCurrent Grid:")

        for row in grid:
            print(" ".join(row))

        try:
            guessrow=int(input("Enter the row number (0-4)?"))
            guesscolumn=int(input("Enter the column number (0-4)?"))
        
        except ValueError:
            print("Invalid input,please choose a row and column between 0-4")
            continue

        attempts+=1

        if guessrow==treasurerow and guesscolumn==treasurecolumn:
            print("Congratulations, you guessed it right in {} attempts!".format(attempts))
            break

        else:
            hint=givehints(treasurerow,treasurecolumn,guessrow,guesscolumn)
            print("Hint:{}".format(hint))

treasurehunt()
