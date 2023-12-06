import random 

#Shane Whitmore 20098910

lotto = [] #creating a list for the users lotto numbers
rndLottoWinning = [] #craeting a list for the winning lotto numbers
lottoWinningPlusOne = [] #creating a list for the winning plus one numbers

def main():
    print("-------------------------------")
    print("|     Welcome to the Lotto    |")
    print("-------------------------------")
    print("")
    print("1. Quick Pick") #print funciton
    print("2. Users Choice")
    print("")

    input1 = int(input("Please select a menu option: ")) #creating a variable based on an input
    while input1 < 1 or input1 > 2: #if the input is less than 1 or greater than 2
        input1 = int(input("Invalid Menu Option, Please try again: ")) # run a loop intul it is
    if input1 == 1: #if the input is = to 1 then run the quickPick function
        quickPick()
    elif input1 == 2: #if the input is = to 2 then run the userChoice function
        userChoice()
        

def generateWinningNumbers(): #function for generating the winning numbers and adding them to a list
    input1 = input("Would you like to enter Lotto Plus? [Y/N] ") #creating a variable for an input
    input1 = input1.upper() #change the variable to upper case

    while input1 != "Y" and input1 != "N": #if the input is not Y and not N :
        input1 = input("Incorrect option, Would you like to enter Lotto Plus? [Y/N] ") #ask the user again to input a value
        input1 = input1.upper() #change the variable to upper case

    if input1 == "Y": #if the input is Y
        while len(lottoWinningPlusOne) < 7: #while the length of the list is less than 7 
            n = random.randint(1,45)    #choose a random number between 1 and 45 inclusive
            if n not in lottoWinningPlusOne: #if the random number is not already in list then add it to the end
                lottoWinningPlusOne.append(n)
    
    while len(rndLottoWinning) < 7: #while the length of the list is less than 7 
        n = random.randint(1,45) #choose a random number between 1 and 45 inclusive
        if n not in rndLottoWinning: #if the random number is not already in list then add it to the end
            rndLottoWinning.append(n)
    
    print("Winning lotto numbers" + str(rndLottoWinning)) #print the winning lotto numbers on screen

    if lottoWinningPlusOne: #if there are items in the lottoPlusOne winning numbers list
        print("Winning lotto plus 1 numbers" + str(lottoWinningPlusOne)) #then print it on screen



def quickPick():#quickPick function
    while len(lotto) < 7: #while the length of the lotto list is less than 7
        n = random.randint(1,45) #create a random number between 1 and 45 inclusive
        if n not in lotto: #if that random number is not already in the lotto list
            lotto.append(n) #add the new random number to the end of the list
    print("Your Quick Pick Numbers " + str(lotto)) #print the quick pick numbers on screen

    generateWinningNumbers() #call on the generateWinningNumbers function
    checkWinningNumbers() #call on the checkWinningNummbers function


def userChoice(): #userChoice function
    while len(lotto) < 7: #while the length of the lotto list is less than 7
        input1 = int(input("Please enter your number: ")) #ask the user to choose a number
        while input1 < 1 or input1 > 45: #if the number is less than 1 or greater than 45
            input1 = int(input("Number must be between 1 and 45, please try again: ")) #ask the user to choose another number
        while input1 in lotto: #if the number is already in the lotto list 
            input1 = int(input("You cannot pick the same number twice, please select another number: ")) #ask the user to choose another number
            while input1 < 1 or input1 > 45: #if the number is less than 1 or greater than 45
                input1 = int(input("This is also an invalid option, please select a number between 1 and 45: ")) #ask the user to choose another number
        lotto.append(input1) #add the number to the end of the lotto list
    print("Selected numbers:", lotto) #show the use the numbers they selected.
    print("Best of Luck") #wish the user best of luck
    generateWinningNumbers() #call on the generateWinningNumbers function
    checkWinningNumbers() #call on the checkWinningNummbers function


def checkWinningNumbers(): #checkWinningNumbers function
    trueCount = 0 #created a variable to store the number of times there is a match between the users numbers and the lotto winning numbers

    for i in lotto: #for every index in lotto lists (users numbers)
        for j in rndLottoWinning: #for every index in the winning numbers list
            if i == j: #if i and j are the same numbers
                trueCount += 1 #add 1 to the trueCount
    
    print("Lotto Results:") 

    if trueCount == 6: #if the matching numbers count is equal to 6
        print("JackPot !!!") #tell the user they got the jackpot
    elif trueCount == 5: #else if the matching numbers count is equal to 5
        print("Congratulations, You won a cash prize") #tell the user they won the cash prize
    elif trueCount == 4: #else if the matching numbers count is equal to 4
        print("Congratulations, You won a cash prize") #tell the user they won the cash prize
    elif trueCount == 3: #else if the matching numbers count is equal to 3
        print("Congratulations, you won a lottery scratch card") #tell the user they won a scratch card
    else: #else tell the user they lost
        print("Not a winner") #tell the user they are not a winner

    if lottoWinningPlusOne: #if there are items in the lottoWinningPlusOne list
        print("Lotto Plus 1 Results:") 
        trueCount = 0 #user another trueCount
        for i in lotto: #for every index in lotto lists (users numbers)
            for j in lottoWinningPlusOne: #for every index in the winning lotto plus one numbers list
                if i == j: #if i and j are the same numbers
                    trueCount += 1 #add 1 to the trueCount

        if trueCount == 6: #if the matching numbers count is equal to 6
            print("JackPot !!!") #tell the user they got the jackpot
        elif trueCount == 5: #else if the matching numbers count is equal to 5
            print("Congratulations, You won a cash prize") #tell the user they won the cash prize
        elif trueCount == 4: #else if the matching numbers count is equal to 4
            print("Congratulations, You won a cash prize") #tell the user they won the cash prize
        elif trueCount == 3: #else if the matching numbers count is equal to 3
            print("Congratulations, you won a lottery scratch card") #tell the user they won the cash prize
        else: #else tell the user they lost
            print("Not a winner") #tell the user they are not a winner


if __name__ == '__main__':
    main()          #start by running the main function