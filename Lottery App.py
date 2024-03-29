
# coding: utf-8

# In[2]:


import random

menu_check = True

# 'checker', compares userNums and winningNums to see if they have won or lost
def checker(userNums, winningNums):

    if userNums == winningNums:
        print ("\nCongratulations! You Win $100!\n")
        print ("Your numbers: ", userNums)
        print ("The winning lottery numbers are: ", winningNums, "\n")
    else:

        print ("\nSorry, you lose...\n")
        print ("Your numbers: ", userNums)
        print ("The winning lottery numbers are: ", winningNums, "\n")

# 'getUserNums', gets user numbers and puts into a sorted list    
def getUserNums():
    userNums = []

    for x in range(3):
        nums = int(input("Pick a number 0 through 9: "))
        if 0 <= nums <= 9:
            userNums.append(nums)
        else:
            input("Error! Invalid input. Press any key to continue...")
            nums = int(input("Pick a number 0 through 9: "))
            userNums.append(nums)

    return sorted(userNums)

# 'getWinningNums', creates a sorted list with random nums ranging from 0-9 with a range of 3 values
def getWinningNums():
    return sorted(random.sample(range(0,10), 3)) 

# 'menu', creates the main menu to choose game or exit program
def menu():
    print (30 * "-", "LOTTERY MENU", 30 * "-")
    print ("1. [Play Pick-3]")
    print ("2. Exit")
    print (75 * "-")

# 'main', calls the other functions
def main():
    userNums = getUserNums()
    winningNums = getWinningNums() 
    checker(userNums, winningNums)

#         
while menu_check:
    menu()
    choice = input("\nEnter your choice[1-2]: ")

    if choice == '1':
        print (23 * "-")
        print ("[Play Pick-3] selected!")
        print (23 * "-")
        menu_check = False
        main()

    elif choice == '2':
        print ("\nThanks for playing!\n")
        menu_check = False
    else:
        input("Error! Invalid input. Press any key to continue...\n")


#  
