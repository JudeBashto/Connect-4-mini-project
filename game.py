
from connect4 import*
import copy


'''
How to play connect four: 
Specify the size of the game: (3,3) creates a 3 by 3 grid. Valid input required here specifically. 
For a (3 by 3) game, valid inputs for column plays are (0,1,2)-> following regular Python indices. 

'''










def main():
    userInput1=input("What is the size of the game? ")
    while userInput1!='quit' or userInput1!='Quit':  #New game loop

        if userInput1=='quit' or userInput1=='Quit': #while condition not executing properly sometimes..

            break
        
        listedInput=userInput1.split(',')
        nRows=int(listedInput[0])
        nCols=int(listedInput[1])
        grid=makeGrid(nRows, nCols)
        fullBoard=False
        turnNumber=0


        for numberOfTurns in range(1,(nRows*nCols)+1): #current game loop 
          

            #Step 2: Checks if there are empty locations in the grid: 


            falseCounter=0
            for number in range(0,len(grid[0])): #iterates for number of columns 
                dumbGrid=copy.deepcopy(grid)     #regular list.copy was not cutting it for some reason. 

                if play(dumbGrid, number, 'red')==True: 
                    pass

                elif play(dumbGrid, number, 'red')==False:
                    falseCounter+=1
        
                    
                if falseCounter==len(dumbGrid[0]):
                    fullBoard=True

            if fullBoard==True:
                print("It's a tie!")
                break
            
            #Step 3: plays red
                
            checker='red'
            column=int(input(f"What column does {checker} (X) want to play?"))
            dumbGrid=copy.deepcopy(grid)
            while column>=len(grid[0]) or column<0 or play(dumbGrid, column,checker)==False:
                print("Invalid Move.")
                column=int(input(f"What column does {checker} (X) want to play?"))
            play(grid,column,checker)
            turnNumber+=1
            print(toString(grid))
            if win(grid, column)==checker:
                print(f"{checker} has won after {turnNumber} moves")  
                break

           
            #STEP 4: checks draw condition
            falseCounter=0
            for number in range(0,len(grid[0])): #iterates for number of columns 
               
                dumbGrid=copy.deepcopy(grid)    


                if play(dumbGrid, number, 'red')==True:   

                    pass                                   #here for testing 

                elif play(dumbGrid, number, 'red')==False:

                    falseCounter+=1

        
                    
                if falseCounter==len(dumbGrid[0]):
                    
                    fullBoard=True

            if fullBoard==True:

                print("It's a tie!")
                break
            
            #STEP 5: plays black

            checker='black'
            column=int(input(f"What column does {checker} (O) want to play?"))
            dumbGrid=copy.deepcopy(grid)

            while column>=len(grid[0]) or column<0 or play(dumbGrid, column,checker)==False:

                print("Invalid Move.")
                column=int(input(f"What column does {checker} (O) want to play?"))

            play(grid,column,checker)
            turnNumber+=1
            print(toString(grid))

            if win(grid, column)==checker:

                print(f"{checker} has won after {turnNumber} moves") #insert moves 
                break




        userInput1=input("What is the size of the game? ")
        if userInput1=='quit' or userInput1=='Quit':
            break

    print("Goodbye")


if __name__=='__main__':
    main()