# Oliver Scott
# ITP 115, Fall 2019
# Assignment 9
# oliversc@usc.edu

#List from the Make column of excel file
def carMake(fileName):
    carMakeList = []
    openFile = open(fileName, "r")
    next(openFile)
    for line in openFile:
        line = line.strip()
        dataList = line.split(",")   
        carMake = dataList[1]
        carMakeList.append(carMake)
    openFile.close()

    return carMakeList

#List from the class column of excel file
def carClass(fileName):
    classList = []
    openFile = open(fileName, "r")
    next(openFile)
    for line in openFile:
        line = line.strip()
        dataList = line.split(",")
        carClass = dataList[0]
        classList.append(carClass)
    openFile.close()

    return classList

#List from the model column of excel file
def carModel(fileName):
    carModelList = []
    openFile = open(fileName, "r")
    next(openFile)
    for line in openFile:
        line = line.strip()
        dataList = line.split(",")
        carModel = dataList[2]
        carModelList.append(carModel)
    openFile.close()

    return carModelList

#List from the city mpg column of excel file
def carMPG(fileName):
    mpgList = []
    openFile = open(fileName, "r")
    next(openFile)
    for line in openFile:
        line = line.strip()
        dataList = line.split(",")
        mpg = dataList[8]
        mpgList.append(mpg)
    mpgList = [int(i) for i in mpgList]
    openFile.close()

    return mpgList


def maxMPG(fileName):
    #calculates the highest mpg of all items in list
    mpgList = carMPG(fileName)
    maxMPG = 0
    for num in mpgList:
        if num>maxMPG:
            maxMPG = num
    return maxMPG

def minMPG(fileName):
    #calculates the lowest mpg of all items in list
    mpgList = carMPG(fileName)
    minMPG = 100
    for num in mpgList:
        if num<minMPG:
            minMPG = num
    return minMPG
            
def resultFile(fileOut,fileName, year):

    #function to print results

    #calls functions for max and min mpg and assigns their returns to a variable
    carMaxMPG = maxMPG(fileName) 
    carMinMPG = minMPG(fileName)

    #calls functions for all the lists and assigns them returns to a variable
    carMakes = carMake(fileName) 
    carClasses = carClass(fileName)
    carModels = carModel(fileName)
    mpgList = carMPG(fileName)

    #determines duplicates in milage, if 3 different cars do 6 mpg for instance
    counter = 0
    dupListMax = []
    for item in mpgList:
        counter +=1
        if item == carMaxMPG:
            dupListMax.append(counter-1)
        

    dupListMin = []
    counter = 0
    for item in mpgList:
        counter +=1
        if item == carMinMPG:
            dupListMin.append(counter-1)


    #prints everything to the results file
    fileOut = open("results.txt", "w")
    print("EPA City MPG Calculator", year, "\n---------------------------------\nMaximum milege (city): ", carMaxMPG, file=fileOut) 
    for item in dupListMax: #prints all iterations of that mpg
        print("\n\t", carMakes[item],carModels[item],"(",carClasses[item],")",file=fileOut)
        
    print("\nMinimum milege (city): ", carMinMPG, file=fileOut)
    for item in dupListMin:
        print("\n\t", carMakes[item],carModels[item],"(",carClasses[item],")", file=fileOut)

    
    
#main function, calls all other functions
def main():
    print("Welcome to EPA Milage Calculator")
    year = int(input("Which year would you like to view data for (2008 or 2009)"))

    #makes sure correct options are in place
    while year<2008 or year>2009:
        print("*Invalid input, please try again!") 
        year = int(input("Which year would you like to view data for (2008 or 2009)"))
    

    if year == 2008:
        fileName = "epaVehicleData2008.csv"
        carClass(fileName)
        carModel(fileName)
        carMPG(fileName)
        carMake(fileName)
        fileOut = input("Enter the filename to save results to: ")
        resultFile(fileOut, fileName, year)
        print("Operation success! Milage data has been saved to ", fileName)
        
    if year == 2009:
        fileName = "epaVehicleData2009.csv"
        carClass(fileName)
        carModel(fileName)
        carMPG(fileName)
        carMake(fileName)
        fileOut = input("Enter the filename to save results to: ")
        resultFile(fileOut, fileName, year)
        print("Operation success! Milage data has been saved to ", fileName)

main()