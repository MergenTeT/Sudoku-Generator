import random
import copy


sudoku =[
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
	]


counters = []



def control_row(i,sudoku,selNumber):#Control row
    for j in range(0,9):
        if sudoku[i][j] == selNumber:
            return False
    return True

def control_col(j,sudoku,selNumber):#Control row
    for i in range(0,9):
        if sudoku[i][j] == selNumber:
            return False
    return True

def control_cell(i,j,sudoku,selNumber):#Control cell
    x1,x2,y1,y2 = for_control_cell(i, j)
    for k in range(x1,x2+1):
        for l in range(y1,y2+1):
            if sudoku[k][l] == selNumber :
                return False
    return True



def for_control_cell(i,j):#parameter values ​​of row and column are determine for control cell
      
    if i<3 : 
        x1,x2 = 0,2
        
    elif i<6 and i>=3 :
        x1,x2 = 3,5
    elif i<9 and i>=6 :
        x1,x2 = 6,8
    
    if j<3 : 
        y1,y2 = 0,2
    elif j<6 and j>=3 :
        y1,y2 = 3,5
    elif j<9 and j>=6 :
        y1,y2 = 6,8 
    
    return x1,x2,y1,y2

def generate_number(i,j,sudoku):
    numbers = [1,2,3,4,5,6,7,8,9]
    
    
    while True :
        
        if len(numbers) == 0 :
            counters.append(1)
            numbers = [1,2,3,4,5,6,7,8,9]
            for a in range(9) :
                sudoku[i][a] = 0
                sudoku[i-1][a] = 0
            j = 0 
            i=i-1
            #problem 
        indisSec = random.randrange(len(numbers))
        selNumber = numbers[indisSec]
        numbers.remove(selNumber)
        
        if control_cell(i, j, sudoku, selNumber) and control_col(j, sudoku, selNumber) and control_row(i, sudoku, selNumber) :
            #print("confirmed number {}".format(selNumber))
            
                
            return i,j,selNumber
            break
        #print("The number {} in column {} of row {} is not confirmed.".format(selNumber,j,i))
        #print(numbers)
        
def generater_sudoku():
    i,j = 0,0
    numbers = [1,2,3,4,5,6,7,8,9]
    while sudoku[8][8]==0:
        
        if j == 9 :
            j = 0
            i +=1
        i,j,sudoku[i][j] = generate_number(i, j, sudoku)
        j +=1
        



def selected_level():#%25 very hard, %30 hard, %40 middle, %50 easy, %70 very easy
    probablity = random.randint(0, 10)
    if probablity <4:#probability of number to be deleted in index
        return True
    return False

def sudoku_upgrade():#second list is creating(there are values of 0)
    counter = 0
     
    for i in range(9):
        for j in range(9):
            if selected_level():
                sudokuUpgrade[i][j] = 0
                counter =counter + 1
    print(" {} numbers assigned. {} numbers deleted and  backtraking applied {} times".format(81-counter,counter,len(counters)))


generater_sudoku()
print(sudoku)
sudokuUpgrade = copy.deepcopy(sudoku)# no change first list with this method copy.deepcopy

sudoku_upgrade()
print(sudokuUpgrade)










