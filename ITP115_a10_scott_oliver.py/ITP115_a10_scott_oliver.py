# Oliver Scott
# ITP 115, Fall 2019
# Assignment 10
# oliversc@usc.edu

class Animal(object):
    #animal class
    def __init__(self,name,species,energy,hunger,health,happiness,age): #constructor, recieves inputs for animal stats from csv file
        self.name = name
        self.species = species
        self.energy = energy
        self.hunger = hunger
        self.health = health
        self.happiness = happiness
        self.age = age

    def play(self):
        """
        When called, adds happiness from animal's stats and adds hunger
        """
        #happiness
        if (self.happiness+10)>100:
            self.happiness = 100
        else:
            self.happiness += 10
        #hunger
        if (self.hunger+5)>100:
            self.hunger = 100
        else:
            self.hunger+=5
   
    def feed(self):
        """
        When called, hunger from animal's stats
        """
        if (self.hunger-10)<0:
            self.hunger = 0
        else:
            self.hunger -= 10

    def giveMedicine(self):
        """
        When called, removes happiness from animal's stats and adds hunger
        """
        #happiness
        if (self.happiness-20)<0:
            self.happiness = 0
        else:
            self.happiness -= 20
        #health
        if (self.health+20)>100:
            self.health = 100
        else:
            self.health += 20
        
    def sleep(self):
        """
        When called, removes energy from animal's stats
        """
        if (self.energy+20)>100:
            self.energy = 100
        else:
            self.energy += 20
        
        self.age +=1

    def __str__(self): #prints out all the animal's stats in a pretty print
        s = ""
        s+="***********\n"+self.name+" the "+ self.species+"\n"
        s+="Health: "+str(self.health)+"\n"
        s+="Happiness: "+str(self.happiness)+"\n"
        s+="Hunger: "+str(self.hunger)+"\n"
        s+="Energy: "+ str(self.energy)+"\n"
        s+="Age: "+str(self.age)+"\n"
        s+="***********"
        return s

def loadAnimals():
    #places all animals into a list (list is every single element separated)
    animalList = []
    openFile = open("animals.csv","r")
    for line in openFile:
        line = line.strip()
        line = line.split(",")
        for thing in line:
            animalList.append(thing)

    counter = 0

    animalObjects = []

    while counter<5:
        counter+=1
        #variables inputs
        """
        Searches through the list for the right 
        element, adds it to the variable
        """
        energy = int(animalList[(counter*7)-4])
        hunger = int(animalList[(counter*7)-7])
        health = int(animalList[(counter*7)-5])
        happiness = int(animalList[(counter*7)-6])
        age = int(animalList[(counter*7)-3])
        name=animalList[(counter*7)-2]
        species=animalList[(counter*7)-1]

        #constructor, puts every variable into the constructor
        animal = Animal(name, species, energy, hunger, health, happiness, age)
        animalObjects.append(animal)
      
    
    return animalObjects

def displayMenu():
    #makes the menu and asks for input (checks if input is right or wrong)
    print("1) Play\n"
    "2) Feed\n"
    "3) Give Medicine\n"
    "4) Sleep\n"
    "5) Print an Animal's stats\n"
    "6) View All Animals\n"
    "7) Exit\n")
    choice = int(input("Please make a selection: \n"))
    while choice>7 or choice<1:
        print("Invalid input, Try again\n")
        choice = int(input("Please make a selection: \n"))
    return choice

def selectAnimal():
    #prints list of animals, asks for input, determines right or wrong
    print("1) Ollie the Bunny\n"
    "2) Murdock the French Bulldog\n"
    "3) Socks the Cat\n"
    "4) Peewee the Turtle\n"
    "5) Milo the Labrador")
    choice = int(input("Please make a selection: \n"))
    while choice>5 or choice<1:
        print("Invalid input, Try again")
        choice = int(input("Please make a selection: \n"))
    return choice

def main():
    animalObjects = loadAnimals()#loads all animals
    print("Welcome to animal daycare! We can do some things: ")
    first = True
    menu = displayMenu()#calls display

    while first == True or menu!=7:
        first = False
        
        #Play
        if menu == 1:
            animalMenu = selectAnimal()
            if animalMenu == 1:
                animalObjects[0].play()
                print("You played with", animalObjects[0].name,"the",animalObjects[0].species,"!\n")
            if animalMenu == 2:
                animalObjects[1].play()
                print("You played with", animalObjects[1].name,"the",animalObjects[1].species,"!\n")
            if animalMenu == 3:
                animalObjects[2].play()
                print("You played with", animalObjects[2].name,"the",animalObjects[2].species,"!\n")
            if animalMenu == 4:
                animalObjects[3].play()
                print("You played with", animalObjects[3].name,"the",animalObjects[3].species,"!\n")
            if animalMenu == 5:
                animalObjects[4].play()
                print("You played with", animalObjects[4].name,"the",animalObjects[4].species,"!\n")
            menu = displayMenu()

        #Feed
        if menu == 2:
            animalMenu = selectAnimal()
            if animalMenu == 1:
                animalObjects[0].feed()
                print("You fed", animalObjects[0].name,"the",animalObjects[0].species,"!\n")
            if animalMenu == 2:
                animalObjects[1].feed()
                print("You fed", animalObjects[1].name,"the",animalObjects[1].species,"!\n")
            if animalMenu == 3:
                animalObjects[2].feed()
                print("You fed", animalObjects[2].name,"the",animalObjects[2].species,"!\n")
            if animalMenu == 4:
                animalObjects[3].feed()
                print("You fed", animalObjects[3].name,"the",animalObjects[3].species,"!\n")
            if animalMenu == 5:
                animalObjects[4].feed()
                print("You fed", animalObjects[4].name,"the",animalObjects[4].species,"!\n")
            menu = displayMenu()
        
        #Medicine
        if menu == 3:
            animalMenu = selectAnimal()
            if animalMenu == 1:
                animalObjects[0].giveMedicine()
                print("You gave", animalObjects[0].name,"the",animalObjects[0].species,"medicine!\n")
            if animalMenu == 2:
                animalObjects[1].giveMedicine()
                print("You gave", animalObjects[1].name,"the",animalObjects[1].species,"medicine!\n")
            if animalMenu == 3:
                animalObjects[2].giveMedicine()
                print("You gave", animalObjects[2].name,"the",animalObjects[2].species,"medicine!\n")
            if animalMenu == 4:
                animalObjects[3].giveMedicine()
                print("You gave", animalObjects[3].name,"the",animalObjects[3].species,"medicine!\n")
            if animalMenu == 5:
                animalObjects[4].giveMedicine()
                print("You gave", animalObjects[4].name,"the",animalObjects[4].species,"medicine!\n")
            menu = displayMenu()
        
        #Put to Sleep
        if menu == 4:
            animalMenu = selectAnimal()
            if animalMenu == 1:
                animalObjects[0].sleep()
                print("You put", animalObjects[0].name,"the",animalObjects[0].species,"to bed\n")
            if animalMenu == 2:
                animalObjects[1].sleep()
                print("You put", animalObjects[1].name,"the",animalObjects[1].species,"to bed\n")
            if animalMenu == 3:
                animalObjects[2].sleep()
                print("You put", animalObjects[2].name,"the",animalObjects[2].species,"to bed\n")
            if animalMenu == 4:
                animalObjects[3].sleep()
                print("You put", animalObjects[3].name,"the",animalObjects[3].species,"to bed\n")
            if animalMenu == 5:
                animalObjects[4].sleep()
                print("You put", animalObjects[4].name,"the",animalObjects[4].species,"to bed\n")
            menu = displayMenu()
            
        #Prints individual stats
        if menu == 5:
            animalMenu = selectAnimal()
            if animalMenu == 1:
                print(animalObjects[0])
            if animalMenu == 2:
                print(animalObjects[1])
            if animalMenu == 3:
                print(animalObjects[2])
            if animalMenu == 4:
                print(animalObjects[3])
            if animalMenu == 5:
                print(animalObjects[4])
            menu = displayMenu()
        
        #Prints list of all animals
        if menu == 6:
            counter = 0
            for item in animalObjects:
                if counter == 6:
                    break
                counter+=1
                print(item)
            menu = displayMenu()
        
                
    print("Goodbye!")
        
main()