import assignmentLessonLib as reflect
import techInterviewLib as techInt

# Custom choice exceptions
class makeGoodChoices(Exception):
	pass

def mainMenu():
    mainMenu = [
        "1) Lesson Reflection Menu",
        "2) Technical Python Questions",
        "3) Exit Program"
    ]
    for item in mainMenu:
        print(item)
    print()

def mainChoice():
    while True:
        try:
            mainMenu()
            choice = int(input("Please enter what you would like to open. Enter 1-3: "))

            if choice == 3:
                print("Thanks for viewing my program.")
                break
            elif choice == 1:
                lessonChoice()
                break
            elif choice == 2:
                techIntChoice()
                break
            else:
                raise ValueError
        except ValueError:
            print("Please enter a choice 1-3.")

# Lesson Review List
def lessonMenu():
    lessonMenu = [
        "1) Assignment 1",
        "2) Assignment 2", 
        "3) Assignment 3", 
        "4) Assignment 4", 
        "5) Assignment 5", 
        "6) Assignment 6",
        "7) Assignment 7",
        "8) Final Project",
        "9) Main Menu",
        "10) Exit Program"
    ]
    for item in lessonMenu:
        print(item)
    print()

# Lesson choice function
def lessonChoice():
    while True:
        # Make choices
        try:
            lessonMenu()
            choice = int(input("Select the lesson you would like to see my reflections on, \nReturn to the main menu or \nExit the program: "))
            
            if choice == 10:
                print("Thanks for viewing my final project")
                break
            elif choice == 9:
                mainChoice()
                break
            elif choice == 1:
                result = reflect.lesson1()
                print(result)
            elif choice == 2:
                result = reflect.lesson2()
                print(result)
            elif choice == 3:
                result = reflect.lesson3()
                print(result)
            elif choice == 4:
                result = reflect.lesson4()
                print(result)
            elif choice == 5:
                result = reflect.lesson5()
                print(result)
            elif choice == 6:
                result = reflect.lesson6()
                print(result)
            elif choice == 7:
                result = reflect.lesson7()
                print(result)
            elif choice == 8:
                result = reflect.finalProject()
                print(result)
            else:
                raise ValueError
            try:
                more = input("Would you like to see other reflections? Please enter Y or N: ").strip().upper()
                if more == "Y":
                    continue
                elif more == "N":
                    mainChoice()
                    break
                else:
                    raise makeGoodChoices
            except makeGoodChoices:
                print("You did not enter Y or N")
                
        except ValueError:
            print("Please choose a number represented in the above menu")

# Technical questions on Python
# Create a function that displays the tecnical questions and calls the techIntChoice function
def techInterviewMenu():
    techIntMenu = [
        "1) What is Python, and what are its key features?",
        "2) What is the difference between a local variable and a global variable in Python?",
        "3) Demonstrate declaring three variables in Python using your name.",
        "4) Define at least three different data types available in Python.",
        "5) Write a conditional statement (if-else) in Python using something that relates to you.",
        "6) Provide an example of lists, tuples, and dictionaries in Python. How are they different from each other?",
        "7) Explain the concept of a function in Python. Write a coding example defining and calling a function using your name as the function.",
        "8) How do you handle exceptions (errors) in Python?",
        "9) What is a loop in Python? Provide an example of the difference between a 'for loop' and a 'while loop' using your name as a variable.",
        "10) What is the purpose of the 'range()' function in Python?",
        "11) How do you read data from a file in Python?",
        "12) How do you comment your code in Python? Why is it important to write comments?",
        "13) Describe the concept of object-oriented programming (OOP) in Python. What are classes and objects?",
        "14) Return to Main Menu",
        "15) Exit Program"
    ]
    for item in techIntMenu:
        print(item)
    print()

def techIntChoice():
    while True:
        try:
            techInterviewMenu()
            choice = int(input("Select the technical question you would like my answer for, \nreturn to the main menu, \nor exit the program 1-15:  "))
            if choice == 15:
                print("Thanks for using my program.")
                break
            elif choice == 14:
                mainChoice()
                break
            elif choice == 1:
                result = techInt.q1()
                print(result)
            elif choice == 2:
                result = techInt.q2()
                print(result)
            elif choice == 3:
                result = techInt.q3()
                print(result)
            elif choice == 4:
                result = techInt.q4()
                print(result)
            elif choice == 5:
                result = techInt.q5()
                print(result)
            elif choice == 6:
                result = techInt.q6()
                print(result)
            elif choice == 7:
                result = techInt.q7()
                print(result)
            elif choice == 8:
                result = techInt.q8()
                print(result)
            elif choice == 9:
                result = techInt.q9()
                print(result)
            elif choice == 10:
                result = techInt.q10()
                print(result)
            elif choice == 11:
                result = techInt.q11()
                print(result)
            elif choice == 12:
                result = techInt.q12()
                print(result)
            elif choice == 13:
                result = techInt.q13()
                print(result)
            else:
                raise ValueError
            try:
                more = input("Would you like to see other reflections? Please enter Y or N: ").strip().upper()
                if more == "Y":
                    continue
                elif more == "N":
                    mainChoice()
                    break
                else:
                    raise makeGoodChoices
            except makeGoodChoices:
                print("You did not enter Y or N")
                
        except ValueError:
            print("Please choose a number represented in the above menu")
            
if __name__ == "__main__":
    mainChoice()