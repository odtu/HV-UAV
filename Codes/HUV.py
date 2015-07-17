import csv
import numpy as np
import matplotlib.pyplot as plt



def import_text(filename, separator):
    #import whole matrix file
    for line in csv.reader(open(filename), delimiter=separator, 
                           skipinitialspace=True):
        if line:
            yield line
def CreateMatrix(row,column,path,delimiter):
    #Create a matrix like double-sized array 
    m=0
    # Creates a list containing 5 lists initialized to 0
    matrix = [[0 for x in range(column)] for x in range(row)] 
    for data in import_text(path, delimiter):
        #print data[0]
        i = 0
        for i in range(100):
            matrix[m][i] = data[i]
            i = i + 1
        #print matrix[0][m]
        m = m + 1
    return matrix
def CoordinateFinder(data, matrix):
    # Use when coordinate necessary (not being used right now!)
    for j in range(100):
        for i in range(42):
            if data == float(matrix[i][j]):
                return i,j          
def WheretoGo(i, j, matrix):
    #Determine where the next stop is.
    leftCoil = float(matrix[i][j-10])
    print leftCoil
    rightCoil = float(matrix[i][j+10])
    print rightCoil
    
    if rightCoil > leftCoil:
        #go right
        j = j + 1

    elif rightCoil < leftCoil:
        #go left
        j = j - 1
       
    else:
        #stand still
        print("waiting...")
    return int(j)
def OutputofPath(i, j, matrix):
    #returns column value and the path which will be followed
    jList, pathList = [], []
    listCounter = 0
    while True:  
        if listCounter >= 2 and (float(matrix[i][j]) == float(pathList[listCounter - 2])):
            break
        else:
            listCounter += 1  
            jList.append(j)
            pathList.append(float(matrix[i][j]))
            j = WheretoGo(i, j, matrix)        

    return jList, pathList   
def PlotSub(x,y,matrix):
    a, b = [], []
    for var in range(100):
        a.append(var)
        b.append(float(matrix[0][var]))

    plt.close('all')

    f, axarr = plt.subplots(3, sharex=True, sharey=True)

    #plot whole MATRIX
    axarr[0].plot(a, b)
    axarr[0].set_title('All Data')

    #plot PATH
    #plotting voltage versus x-axis (bigger the blob closer the solution)  
    ysize = []  
    var = 1
    while var in range(len(x)+1):
        ysize.append(float(var))
        var += 1

    for i in range (0, len(x)):
        axarr[1].plot(x[i], y[i], linestyle="None", marker="o", markersize=ysize[i], color="red")
        axarr[1].set_title('"Bigger the point closer the solution" Graph')

        axarr[2].plot(x[i], y[i], linestyle="None", marker="s", markersize=5, color="green")
        axarr[2].set_title('Same solution above but all points have same size')


    plt.show()

 


# MAIN USER INTERFACE
print("Value should be between 10-90 for column")
myRow = int(raw_input("Enter a value for Row: "))
myColumn = int(raw_input("Enter a value for Column: "))

while myColumn <= 9 or myColumn >= 90:
    print("Wrong choice !! Please select values between 10-90 for column")
    myRow = int(raw_input("Enter a value for Row: "))
    myColumn = int(raw_input("Enter a value for Column: "))

#Create Matrix  rowSize=42, columnSize=100
matrix = CreateMatrix(42, 100, 'Mymatrix.txt', '\t')

jList, pathList = OutputofPath(myRow, myColumn, matrix)
PlotSub(jList, pathList, matrix)