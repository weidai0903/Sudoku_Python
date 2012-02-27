# Wei Dai
# CIT591 Assignment 4:Sudoku

def read_sudoku(file):
    stream = open(file)
    data = stream.readlines()
    stream.close()
    return eval("".join(data))

def convertToSets(problem): 
    newLine=[]
    newArray=[]
    for i in range(0,len(problem)):
        newLine=[] #create a new line array each time one line is through
        for j in range(0,len(problem[0])):
            if problem[i][j]==0:  #append 1 to 9 set to newLine where 0 appears
                newLine.append({1,2,3,4,5,6,7,8,9})
            else: #append the one element set of integer to the newLine
                newLine.append({problem[i][j]}) #
        newArray.append(newLine) #append the newLine of sets to 2D newArray 

    return(newArray)

def convertToInts(problem):
    newLine=[]
    newArray=[]
    for i in range(0,len(problem)):
        newLine=[] #create a new line array each time one line is through
        for j in range(0,len(problem[0])):
            if len(problem[i][j])>1 or len(problem[i][j])==0:
                newLine.append(0)# append 0 to every none single set and empty set
            elif len(problem[i][j])==1:
                newLine.append(list(problem[i][j])[0]) #append the integer to newLine array
        newArray.append(newLine)#append the newLine Array to the 2D newArray

    return(newArray)
                
def getRowLocations(rowNumber):
    locationsRow=[]
    for i in range (0,9): 
        locationsRow.append((rowNumber,i)) #get the locations of a certain row
    return locationsRow #return a listOfLocations

def getColumnLocations(columnNumber):
    locationsColumn = []
    for i in range (0,9):
        locationsColumn.append((i,columnNumber))#get the locations of a certain column
    return locationsColumn# return a listOfLocations

def getBoxLocations(location):
    boxOriginRow=(location[0]//3)*3 #set the origin of each box to the upper left coner of the box
    boxOriginCol=(location[1]//3)*3
    boxLocations=[]

    for i in range(0,3):
        for j in range(0,3):
            boxLocations.append((boxOriginRow+i,boxOriginCol+j))
    return boxLocations #return a listOfLocations

def eliminate(problem,location,listOfLocations):
    removeCount=0 #count the times removals are made
    setToList=list(problem[location[0]][location[1]])
    numToRemove=setToList[0] #find the number to remove
    for locationToRemove in listOfLocations:
        row=locationToRemove[0]
        column=locationToRemove[1]
        if (numToRemove in problem[row][column]) and (row!=location[0] or column!=location[1]):
        # remove the number in "location" from the set in each of the location in listOfLocations
            problem[row][column].remove(numToRemove)
            removeCount+=1 #count the number of eliminations
    return removeCount

def isSolved(problem):
    for row in problem:
        for eachSet in row:
            if len(eachSet)!=1:#to check if each set is singleton
                return False
    return True

def solve(problem):
    removeCountRow=1  #initialize the removeCount 
    removeCountColumn=1
    removeCountBox=1
    while removeCountRow!=0 or removeCountColumn!=0 or removeCountBox!=0:
    #if removeCount==0 after we go through all the locations,end the loop
        removeCountRow=0 #initialize the removeCount after going through every location 
        removeCountColumn=0
        removeCountBox=0
        for i in range(0,len(problem)):
            for j in range(0,len(problem[0])):
                if len(problem[i][j])==1:
                #when encounter a single integer, remove the same integer in the row,column and box
                    removeCountRow+=eliminate(problem,(i,j),getRowLocations(i)) 
                    removeCountColumn+=eliminate(problem,(i,j),getColumnLocations(j))
                    removeCountBox+=eliminate(problem,(i,j),getBoxLocations((i,j)))

    return isSolved(problem)

def print_sudoku(problem):
    for i in range(0,len(problem)+4):
        for j in range(0,len(problem)+4):
            if i%4==0 and j%4==0 : 
                print('+',end=' ')
            elif i%4==0 and j%4!=0:
                print('-',end=' ')
            elif i%4!=0 and j%4==0:
                print('|',end=' ')
            else:
                elem=problem[i-(i//4+1)][j-(j//4+1)]
                if(elem!=0):
                    print(problem[i-(i//4+1)][j-(j//4+1)],end=' ')
                else:
                    print('.',end=' ')
        print()
        
def main():
    flag=False
    print("Wei Dai, Qing Xie")
    print("CIT591 assaignment 4: Sudoku ! ")
    while(flag==False): #make sure the user do not want to quit
        file=input("Please insert a Sudoku puzzle file:")
        print("The original sudoku puzzle:")
        problemInts=read_sudoku(file) #read in file 
        print_sudoku(problemInts)
        problemSets=convertToSets(problemInts)#convert the ints problem to array of sets
        result=solve(problemSets) #solve it
        solvedInts=convertToInts(problemSets) #convert the solved problem back to ints
        if result:
            print("successfully solved!")
            print_sudoku(solvedInts)
        else:
            print("This sudoku cannot be completely solved!")
            print_sudoku(solvedInts) #print the uncomplete solution
            for i in range(0,len(problemSets)):
                for j in range(0,len(problemSets[0])):
                    if len(problemSets[i][j])>1:
                        print("location (",i,",",j,") might be any of",end=" ")
                        print(problemSets[i][j])#print the unsolved location and the possible numbers
        while(1):
            quitProgram=input("Do you want to solve another puzzle? Please enter yes/no:")
            if quitProgram=="yes":
                break
            elif quitProgram=="no":
                flag=True
                break
                
    
