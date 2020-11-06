"""
mathQuizGen.py: This program will generate a 10 question math quiz and will grade the user's answers.

author: Mario Medel

7/30/20
"""
import random

# Introduction

print('              Math Quiz Generator')
print('================================================')
print('~Only two quiz types: addition and subtraction')
print('~3 difficulty levels:')
print(" 1) 1 digit"
      " 2) 2 digits"
      " 3) 3 digits")
print("=" * 50)

user_correct = 0


# main function with a loop after selecting difficulty and quiz type
def main():
    qType = select_Qtype()
    user_diff = select_difficulty()
    nums = random_nums(user_diff)
    # Adding question number counter
    questionNum = 0
    for i in range(10):
        questionNum += 1
        user_ans = startQuiz(qType, nums, questionNum)
        user_correct = grader(user_ans, qType, nums)
        nums = random_nums(user_diff)
    grade = user_correct * 10
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(f'Final Grade: {grade}%'
          f'\n{user_correct} out of 10 correct!')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# function to select the type of quiz
def select_Qtype():
    userQuizType = int(input('\nSelect a quiz type- 1) Addition or 2) Subtraction: '))

    while userQuizType > 3 or userQuizType <= 0:
        print("Invalid Quiz Type.")
        userQuizType = int(input('1 for addition or 2 for subtraction: '))

    else:
        return userQuizType


# selecting difficulty to determine amount of random nums
def select_difficulty():
    user_difficulty = int(input('\nSelected Quiz Difficulty - 1) 1-Digit 2) 2-Digit 3) 3-Digit: '))

    while user_difficulty <= 0 or user_difficulty > 4:
        user_difficulty = int(input('Selected Quiz Difficulty - 1) 1-Digit 2) 2-Digit 3) 3-Digit: '))
        if user_difficulty == 1 or 2 or 3:
            break
    return user_difficulty


# generating random numbers which takes the parameter of the user inputted difficulty
def random_nums(user_difficulty):
    if user_difficulty == 1:
        for i in range(10):
            a = random.randint(0, 9)
            b = random.randint(0, 9)

    elif user_difficulty == 2:
        for i in range(10):
            a = random.randint(10, 99)
            b = random.randint(10, 99)

    elif user_difficulty == 3:
        for i in range(10):
            a = random.randint(100, 999)
            b = random.randint(100, 999)
    return a, b


# Letting the user input their answer choice
def startQuiz(Type, nums, q_num):

    (num1, num2) = nums
    if Type == 1:
        user_ans = int(input(f'\nQ{q_num}) {num1} + {num2} = '))
    elif Type == 2:
        user_ans = int(input(f'\nQ{q_num}) {num1} - {num2} = '))
    return user_ans


# maintaining the amount the user has correct
def grader(user_ans, type, nums):
    global user_correct
    (num1, num2) = nums
    if type == 1:
        answer = addInt(num1, num2)
    elif type == 2:
        answer = subInt(num1, num2)

    if answer == user_ans:
        user_correct += 1
        print('Correct')
    elif answer != user_ans:
        print('Incorrect')
    return user_correct

# adding function
def addInt(a, b):
    ans = a + b
    return ans

# subtracting function
def subInt(a, b):
    ans = a - b
    return ans

# starting the program
main()

# end prompt
input('\nEnter to close window:')
