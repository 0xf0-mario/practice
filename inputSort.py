"""
inputSort.py: This program will receive a series of numbers via user input. after the user presses the enter key, the program will output the largest number, the smallest number, and the average.

By: Mario Medel

7/23/2020
"""
print("                                       User Input Sorter")
print("====================================================================================================")
print("Directions: Input any integer number and the program will determine the highest, lowest and average.")
print("*press enter when prompted to enter a number to finish*\n")
# assigning variables

count = 0
sumNums = 0
highNum = -999
lowNum = 999
averageNum = 0
userNum = 0

# User Input

userNum = input("Enter a number or press enter to finish;")
while userNum != "":
    # in order to recieve more than 1000 user inputs: Change range to desired value
    for _ in range(1000):
        userNum = int(userNum)
        count += 1
        sumNums += userNum
# determining the largest value and the smallest value
        if userNum > highNum:
            highNum = userNum
        if userNum < lowNum:
            lowNum = userNum
        userNum = input("Enter a number or press enter to finish;")
        if userNum == "":
            break


# calculating the average
averageNum = sumNums / count

# outputting the results

print(f"\nThe Highest Number: {highNum}")
print(f"The Lowest Number: {lowNum}")
print(f"Average: {averageNum}\n")


input("press any key to close the window")

