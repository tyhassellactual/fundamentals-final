# "1) What is Python, and what are its key features?",
def q1():
    answer = "Python is a high-level programming language capable of many things. Supporting data types like floats, integers, strings, and booleans Python can manipulate conditional statements to control the flow of a program quickly after being interpreted. Yes, interpreted not compiled. Functions perform a task that can utilize 'for' or 'while' loops, conditional 'if-else' 'if-elif-else' statements, or complete an iterated list of tasks."
    return answer
# "2) What is the difference between a local variable and a global variable in Python?"
def q2():
    answer = "A global variable is defined outside of any function and is accessible throughout the entire program. A local variable is defined within a function and can only be accessed within that function's scope. When the function finishes executing, its local variables are destroyed and are no longer accessible. To modify a global variable from within a function, you need to use the 'global' keyword."
    return answer
# "3) Demonstrate declaring three variables in Python using your name."
def q3():
    answer = "3 ways to appropriately use my name as a variable are:\n\n tylerJamesHassell = 'camelCase' \nTylerJamesHassell = 'PascalCase' \ntyler_james_hassell = 'underscore usage' \n Using lowercase with underscores or camelCase is assumed best practice and constants are typically UPPERCASE_WITH_UNDERSCORES by convention "
    return answer
# "4) Define at least three different data types available in Python."
def q4():
    answer = "1) Numeric: \n\tint: Interger values \n\tfloat: Decimal values \n\tcomplex: numeration of complex numbers like 5+3x \n2) Sequences: \n\tstr: Text strings ('hello' and 'Python') \n\tlists: Ordered and mutables arrays ([1, 2, 3]) \n\ttuples: ordered immutable collection of elements ((3, 2, 1)) \n3) Booleans: True or False values also equal to 1 or 0 respectively"
    return answer
# "5) Write a conditional statement (if-else) in Python using something that relates to you."
def q5():
    answer = "if employed == True: \n\tprint('Congrats, you can pay your bills') \nelse: \n\tprint('Don't worry you got this!')"
    return answer
# "6) Provide an example of lists, tuples, and dictionaries in Python. How are they different from each other?"
def q6():
    answer = "lists are ordered mutable data types \n\tmyList = [apples, oranges, bananas]\n\tThese can be added to or changed easily i.e. \n\tmyList.append(pears) # adds 'pears' to the end of my list \n\tprint(myList) # Output apples, oranges, bananas, pears\n\ntuples are immutable. This means that their data cannot be changed once defined. \n\tmyTuple = (Glock, Sig, Colt) # What is listed inside of myTuple and the order cannot be changed\n\ndictionaries are are used to store data in pairs using 'key:value' pairing structure.\n\tmyDict = {\n\t\t'brand':'Ford'\n\t\t'model':'F-150'\n\t\t'year':1986 \n\t}"
    return answer
# "7) Explain the concept of a function in Python. Write a coding example defining and calling a function using your name as the function."
def q7():
    answer = "Functions are simply a block of code that only runs when it is called. You may pass parameters or arguments into a function, functions can call other functions, return data or display information to a UI.\n\nCreating a function:\n\ntylerHassell():\n\tuName = input('please enter your name') #receives input from user\n\tprint(f'Hello, {uName}!') # Outputs 'Hello, 'uname'\n\nTo call a defined fucntion simply put the function in your code:\n\ntylerHassell() # This will call the function."
    return answer
# "8) How do you handle exceptions (errors) in Python?"
def q8():
    answer = "Handling exceptions is done through 'try' and 'except' blocks of code. The 'try' block lets you test a block of code for a potential error. \n\nIn this example you will see a 'try' block of code. The print() function being called produces an error, more namely a NameError because the parameter is not defined.\n\n\ttry:\n\t\tprint(x)\n\texcept NameError:\n\t\tprint('Variable is not defined')\n\texcept:\n\t\tprint('something else went wrong)\nAs you can see catching these error is not difficult. Raising an exception is also an option.\n\n\tresult(num1, num2):\n\t\ttry:\n\t\t\t print(num 1 / num2)\n\t\t\tif num2 == 0:\n\t\t\t\traise ZeroDivisionError('Cannot divide by zero')"
    return answer
# "9) What is a loop in Python? Provide an example of the difference between a 'for loop' and a 'while loop' using your name as a variable."
def q9():
    answer = "Loops in Python allow for a block of code to run until a certain condition is met. \nA 'for' loop is perfect to run a known number of times or through a certain number of iterations defined by the program:\n\ntyler_james = [apple, orange, banana]\nfor item in myList\n\tprint(item) # output:\n\napple\norange\nbanana\n\nA while loop will run until a boolean condiation, 'while True' is met.\n\ntyler_hassell_age = 0\nwhile tyler_hassell_age <= 38:\n\tprint(tyler_hassell_age)\n\ttyler_hassell_age += 1"
    return answer
# "10) What is the purpose of the 'range()' function in Python?"
def q10():
    answer = "range() is commonly used in loops to iterate a specific number of times.\nrange(stop) goes from 0 up to but not including 'stop'\nrange(start, stop) goes from (including) 'start' up to, but not including 'stop'\nrange(start, stop, step) generates a sequence that includes 'start', goes up to but doesn't include 'stop', with a defined 'step' in iteration"
    return answer
# "11) How do you read data from a file in Python?"
def q11():
    answer = "To open a file, simply use the built in open() function and pass either the file name, or the file's path if it is located in a different location.\nThis would look somthing like this for a file named tyler_hassell.txt in the 'workload' folder following the path /users/tyjaha/Desktop/workload/tyler_hassell.txt\n\nmyFile = oper('/users/tyjaha/workload/tyler_hassell.txt', 'r')\nprint(myFile.read()) # open() returns a file object which has a read() method for reading the context of the file."
    return answer
# "12) How do you comment your code in Python? Why is it important to write comments?"
def q12():
    answer = "There are two accepted methods to comment in the Python language.\n\n'''\nOne is like this\nused for multiple line of comments\nand longer explanations, perhaps\nin Libraries or first instance of functions\n'''\n\nThe next way to comment is single line. Single line comments can be place in the line preceding the code, or in line with the code.\n# This is a comment\nprint('Hello, world!) # This is also a comment"
    return answer
# "13) Describe the concept of object-oriented programming (OOP) in Python. What are classes and objects?"
def q13():
    answer = "OOP is a style of programming that allows the develop to create objects and manipulate how those objects interact, relate, or are shown with each other. Classes are like a blueprint for creating these objects.\nTo give an example of this we'll use the __init__() function to help up create a blueprint for out classes attrubutes.\n\nclass Gun:\n\tdef __init__(self, brand, model, caliber):\n\t\tself.brand = brand\n\t\tself.model = model\n\t\tself.caliber = caliber\n\ngun1 = Gun('Remington', 700, '.308')\n\nprint(gun1.brand) #output Remington\nprint(gun1.caliber) #output .308"
    return answer
