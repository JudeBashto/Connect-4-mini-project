

def makeGrid(nRows:int=6, nCols:int=7)-> list:

    grid=[]
    for i in range(0,nRows):
        grid.insert(0,['empty']*nCols)
    
    return grid


def play(grid:list, column:int, checker:str)->bool:
    rowNumber=(len(grid)-1)                              
    if column<len(grid[0]) and column>=0:  

        if grid[0][column]=='empty':  
            
            while rowNumber>=0:
                

                if grid[rowNumber][column]=='empty':
                    break
                else:
                    rowNumber-=1
            
            grid[rowNumber][column]=checker #.center(5)
            return True

        else:
            return False

    else:
        print("Column is out of bounds!") #change later
        return False

def lastCheckerPlayed(grid:list, column:int):
    rowNumber=0
    while rowNumber<=len(grid):
        if grid[rowNumber][column]!='empty':
            break
        rowNumber+=1
    return rowNumber, column  #index values, not actual column/row numbers. 

def verticalWinChecker(grid:list, column:int):
    rowNumber, columnNumber=lastCheckerPlayed(grid, column)
    checker=grid[rowNumber][columnNumber]
    counter=0

    while grid[rowNumber][columnNumber]==checker:
        counter+=1
        rowNumber+=1
        if rowNumber>=len(grid):
            break

    return counter, checker

def horizontalWinChecker(grid:list, column:int):
    rowNumber, columnNumber=lastCheckerPlayed(grid, column)
    checker=grid[rowNumber][columnNumber]
    counter=0
    while grid[rowNumber][columnNumber]==checker:
        counter+=1
        columnNumber+=1
        if columnNumber>=len(grid[0]):
            break
    rowNumber, columnNumber=lastCheckerPlayed(grid, column)
    counter-=1                                                   #prevents double counting source location
    while grid[rowNumber][columnNumber]==checker:
        counter+=1
        columnNumber-=1
        if columnNumber<0:
            break

    return counter,checker

def diagonalWinChecker(grid:list, column:int):
    rowNumber, columnNumber=lastCheckerPlayed(grid, column)
    checker=grid[rowNumber][columnNumber]
    counter=0
    counter2=0
    
    while grid[rowNumber][columnNumber]==checker: #bottom right
        counter+=1
        columnNumber+=1
        rowNumber+=1
        if columnNumber>=len(grid[0]):
            break
        elif rowNumber>=len(grid):
            break
    
    rowNumber, columnNumber=lastCheckerPlayed(grid, column)
    counter-=1 

    while grid[rowNumber][columnNumber]==checker: #top left
        counter+=1
        columnNumber-=1
        rowNumber-=1
        if columnNumber<0:
            break
        elif rowNumber<0:
            break

    rowNumber, columnNumber=lastCheckerPlayed(grid, column)


    while grid[rowNumber][columnNumber]==checker: #top right
        counter2+=1
        columnNumber+=1
        rowNumber-=1
        if columnNumber>=len(grid[0]):
            break
        elif rowNumber<0:
            break

    rowNumber, columnNumber=lastCheckerPlayed(grid, column)
    counter2-=1

    while grid[rowNumber][columnNumber]==checker: #bottom left
        counter2+=1
        columnNumber-=1
        rowNumber+=1
        if columnNumber<0:
            break
        elif rowNumber>=len(grid):
            break



    theChamp=max(counter,counter2) 


    return theChamp, checker

def win(grid:list, column:int)-> str: 
    if column<=len(grid[0]):
        counter1, checker1=verticalWinChecker(grid, column)
        counter2, checker2=horizontalWinChecker(grid, column)
        counter3, checker3=diagonalWinChecker(grid, column)
        if counter1>=4:

            return checker1
            
        elif counter2>=4:

            return checker2

        elif counter3>=4:

            return checker3

        else:
            return 'empty'

    else: return 'empty'

def toString(grid)->str:
    x=""
    y=" "
    z="+"
    counter=0
    counter2=0
    for row in grid:
        x+= "|"
        for column in row:
            if column=="red":
                x+="X"
            elif column=="black":
                x+="O"
            else:
                x+=" "
            if counter2<len(grid[0]):
                y+=str(counter2)
                counter2+=1
                z+="-"
        x+="|"+str(counter)+"\n"
        counter+=1
    z+="+\n"
    x+=z+y

    return x
        

def main():
    grid=makeGrid(7 , 7)
    print(toString(grid))

    userInput=""
    while userInput!="no":
        userInput=int(input("What column do you want to to play? Type ''no'' if done. \n"))
        checker=input("red or black?")
        print(play(grid, userInput, checker ))
        print(toString(grid))
        if userInput-1<=len(grid[0]):
            # print(grid)
            if win(grid, userInput)!='empty':
                print(win(grid,userInput) , "has Won!")
                break
    

# if __name__=='__main__':
#     main()