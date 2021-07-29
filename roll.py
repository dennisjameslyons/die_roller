import random

#creates empty list to store the value of your rolls
thenums = []

#creates a rolls function that prompts user for
#a number they want to roll through.
#essentially provides the option to roll any sided die they choose
def rolls():

    x = (int(input("please enter the number you would like to roll through. \nfor example if you would like to roll for a number \nbetween 1 and 6, as on a typical die, enter 6: ")))

    #function to take the user's chosen sided-die, and rolls
    def my_roll():
        roll = random.randint(1, x)
        # lets them know the outcome of the roll,
        print("When rolling, the result was: ")
        print(roll)
        #adds the randomly rolled number to empty list [thenums]
        thenums.append(roll)

        #asks player if they would like to continue or stop playing.
        reply = str(input("would you like to continue? y/n ")).lower().strip()

        #continues rolling by calling the my_roll() function if they ansewr "y"
        if reply[0] == "y":
            print(roll)
            return my_roll()
        # if the player elects NOT to continue, the game ends
        # & they are presented with their full list of numbers.
        elif reply[0] == "n":
            print ("your numbers were: ")
            print(thenums)
        elif IndexError:
            return ("invalid entry")
        else:
            print ("your numbers were: ")
            print(thenums)

    #calls the my_roll() function as the second step of the rolls() function,
    #AFTER prompting the player for the sided-die they would like to play with.
    return my_roll()
#calls the roller function
rolls()
