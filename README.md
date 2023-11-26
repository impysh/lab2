# ET0735 – Lab 2 (Introduction to Python)
[ET0735 Lab 2 - Introduction to Python.docx.pdf](https://github.com/izzaops/lab2/files/13466999/ET0735.Lab.2.-.Introduction.to.Python.docx.pdf)

ET0735 - DEVOPS FOR AIOT
SCHOOL OF ELECTRICAL AND ELECTRONIC ENGINEERING, SINGAPORE POLYTECHNIC

LABORATORY 2: INTRODUCTION TO PYTHON

Objectives

By the end of the laboratory, students will be able to
Implement a basic Python program using the following,
Logical Operators
Mathematical Operators
String processing
Data processing

Activities
Installation of Python 3 interpreter
Installation of PyCharm Professional Edition using “Educational License”
Create a new Python project in PyCharm
Create and Execute Python scripts in PyCharm project
Commit and Push to GitHub
Basic Python programming: Functions, console Input / Output, strings and list data structures, comparison and arithmetic operators.

Review
Successfully installed PyCharm Professional
Created a Python application using basic logical, mathematical operators with string and data processing
Implement basic Python console application to get user input from the terminal console

Equipment:
Windows OS laptop


Procedures:
Installation of Python 3 Interpreter

Before we start to install the PyCharm Professional IDE, we first need to install the Python 3 interpreter which PyCharm will use for running our Python code.

Download the Python 3 interpreter for Windows from the link below. Choose version 3.8.x or later (e.g. 3.8.10 for 64-bit systems)

https://www.python.org/downloads/

Run the installer to start the Python 3 interpreter installation process. During installation, remember to tick “Add Python 3.8 to PATH” and “Disable path length limit”.

Installation of PyCharm Professional Edition using “Educational License”

Download PyCharm version 2021.3.3 or higher from the following link below. Use you SP “iChat” email address to register. Choose PyCharm “Professional Edition”. You will use “educational license” at no cost for 1 year.

https://www.jetbrains.com/shop/eform/students

Install the PyCharm “Professional Edition” using the educational license using your SP “iChat” email address. During the installation, tick the 4 options:

Create Desktop shortcut
Update PATH variable
Update Context Menu
Create associations

Create a new PyCharm project

In your laptop’s C-drive, create a new folder in the Local_Git_Repository folder that you have created in Lab1 “c:\Local_Git_Repository\Lab2”. You will use it to

store your Python codes. Take note that this is just for example and you can create a folder for this lab in any preferred location in your laptop.

Launch the PyCharm software by double-clicking the shortcut on Desktop. A welcome window will pop up. Choose “New Project”.

The “Create Project” dialog box will appear. Make sure that “Pure Python” has been selected. (Note: the colour of your popup window may be different from what is shown in Figure 1 due to different theme chosen for your PyCharm software.)

For the “Location” field, click the folder icon at the far right. Choose the “c:\Local_Git_Repository\Lab2” folder you had created in Step 3.1, then click “OK”. This will set the location for storing your Python project.

Figure 1 – Set the saving location of your Python project.

Click on the “previously configured interpreter”

Since there is no interpreter available, we need to select <Add interpreter> option, and then select “Add local interpreter” (Figure 2)























Figure 2 – Add Local Interpreter in PyCharm


In the “Add interpreter” Select system interpreter and the system should select the python version that you have installed in your laptop (Figure 3).


























Figure 3 – Choose the interpreter for your Python project.


The PyCharm IDE will be launched, showing the newly created project Lab2.

Figure 4 – The PyCharm IDE.

While in the PyCharm IDE, you may click “Help→About” to see your PyCharm software licensing information. Check that you have correctly installed PyCharm “Professional Edition” and the expiry date is at least 1 year from the current date.


Figure 5 – Use “educational license” for the PyCharm (Professional Edition) software.

Create and Execute Python scripts in a PyCharm project

In PyCharm IDE, right-click the “ET0735_Lab2” project, choose “New”, and then select “Python File”.


Figure 6 – Add a new Python file to your PyCharm project “Lab2”.

A popup window will prompt for the file name. Name the file “Lab2.py” and press the ENTER key.

Add the the following Python code in the newly created Lab2.py,


From the “Run” menu, select “Run…” to run Lab2.py code.

Figure 7 – Run the Lap2.py code.

The first time the “Run” option is selected in PyCharm, a dialog box will appear for you to select which Python script should be run and you should select “Lab2.py”.

Subsequently the “Run” option will execute the last run Python script without prompting you to select which script to execute.


Check the console output in PyCharm.

If your project was created correctly you should see the console output based on the initial code in Lab2.py.

Figure 8 – Console output after running the Lab2.py code.

Create a Local Git Repository and Push to GitHub

Now, you will create a new local git repository to track your PyCharm Python project.

Open a Command Prompt window and change to the directory to “c:\Local_Git_Repository\Lab2”.

Enter Git command git init and check that the .git folder has been created in the “c:\Local_Git_Repository\Lab2”

Stage all the contents in the folder “c:\Local_Git_Repository\Lab2” using the git add * command. The ‘*’ represents a wildcard filter that requests git to stage all files within the current repository folder.

After the staging is completed, commit to the local git repository. Write the git command you use in the space provided below.
git commit -m "Initial commit"



Login to GitHub using the account you had created in Lab 1. Create a new repository at GitHub and name it as Lab2. Copy the URL of the GitHub Lab2 repository. Refer to Lab 1 for the steps if necessary.

At your local git repository, specify the URL of the remote GitHub repository. Set up the upstream branch. After that, push the local git repository to GitHub. Write the git commands you use in the space provided below.
git remote add origin https://github.com/izzaops/lab2.git



Notice that not all the files located in the folder “c:\Local_Git_Repository\Lab2” are pushed to GitHub. To understand which files are ignored and not tracked in the local and remote repository, open the file .gitignore in “D:\ET0735_Lab2\.idea” and study it’s contents to understand which files will be “ignored” by Git.

Python Functions and Mathematical Operators

Python User Defined Functions

To develop modular software code that is easy to maintain and extend, we need to decompose our Python code into functions.

Splitting the code into functions are also useful to simplify the coding implementation as well as to simplify the Software Unit Testing which will be covered in Lab 3.

Python is an indentation-based (each indentation is 4 spaces) programming language and functions are defined with the following syntax:



Notice in the above code we define a function starting with the keyword “def” followed by the function name and then a list of comma separated parameters. The code inside the function is indicated to start with a tab space (= 4 spaces), and the function can return some data using the “return” keyword.


Python Arithmetic Operators

The table below list some of the most commonly used Python arithmetic operators.

Mathematical Operator
Python Operator
Example
Addition
+
result = x + y
Subtraction
-
result = x - y
Multiplication
*
result = x * y
Division
/
result = x / y
Exponential
**
result = x ** y
Modulo
%
result = x % y


Table 1

For further information on Python arithmetic operators, refer to the URL below, https://www.w3schools.com/python/gloss_python_arithmetic_operators.asp

Python Conditional Operators

Please refer to the link below for examples of Python conditional operators. https://www.w3schools.com/python/python_conditions.asp

Exercise 1:

Implement a Python application that will calculate the Body Mass Index (BMI) based on the user’s height (in meters) and weight (in kilograms).

In PyCharm, using the project “Lab2” created in step 3, create a new Python file “bmi.py” and define a new function “calculate_bmi” with 2 string parameters for height and weight as shown below


Run the Python code above and observe the console output in PyCharm.

Based on the Python code implemented in (a), modify the code to call the function “calculate_bmi” using floating point values instead of strings. Notice the difference in the weight and height parameters now passed as floating point data type without the quotation marks “”.


Run the Python code with the modifications in bold above and observe the console output which should now result in a runtime error.

Write down the last error observed in PyCharm console in the box below

Traceback (most recent call last):
  File "C:\Local_Git_Repository\lab2\bmi.py", line 5, in <module>
    calculate_bmi(weight=57, height=1.73)
  File "C:\Local_Git_Repository\lab2\bmi.py", line 2, in calculate_bmi
    print("Height = " + height)
          ~~~~~~~~~~~~^~~~~~~~

TypeError: can only concatenate str (not "float") to str


Modify the function “calculate_bmi()” to use the str() function as shown in the code below.


Run the modified Python code passing the weight and height as floating point data types and check the PyCharm console ouput.

In the box below, write down the reason why the “str()” function has helped to fix the error.

The reason the str() function is used to fix the error is that the print() function in Python can only concatenate strings (i.e., it can only combine or concatenate values of the string data type) with other strings. In the original code, the height and weight parameters were provided as floating-point values without converting them to strings. This caused a TypeError because you cannot directly concatenate a string and a float.

By using str(), you are converting the floating-point values height and weight into string representations, allowing you to concatenate them with the "Height = " and "Weight = " strings in the print() statements, thereby fixing the error.


Finally we now need to implement the mathematical formula to calculate BMI based on the formula below,



𝐵𝑀𝐼 =
Weight (𝑘𝑔)


Height (𝑚)  × Height (𝑚)







Modify the code above to implement the Python code to calculate and display the BMI value on the console.

Run your Python file and check that the PyCharm console shows the correct calculated BMI value.

def calculate_bmi(height, weight):
   print("Height = " + str(height))


   print("Weight = " + str(weight))


   # calculate bmi, need to get height and weight from calculate_bmi function
   bmi = (weight / (height * 2))
   print("BMI = " + str(bmi))


calculate_bmi(height=1.73, weight=57)


Based on the table below, implement Python code using conditional operators (eg: if, else, etc) to determine if the user is “Under Weight”, “Normal Weight” or “Over Weight”.

BMI Range
Weight Classification
BMI < 18.5
Under Weight
18.5 ≤ BMI ≤ 25.0
Normal Weight
BMI > 25.0
Over Weight


Table 2

Update your Python code to display on the console the BMI classification and verify that the results are correct based on the BMI ranges defined in Table 2.
def calculate_bmi(height, weight):
   print("Height = " + str(height))


   print("Weight = " + str(weight))


   # calculate bmi, need to get height and weight from calculate_bmi function
   bmi = (weight / (height * 2))
   print("BMI = " + str(bmi))


   if (bmi < 18.5):
       print("Underweight")
   elif (18.5 <= bmi <= 25.0):
       print("Normal weight")
   else:
       print("Overweight")


calculate_bmi(height=1.73, weight=57)

Commit and Push all your local Git repository changes to Github

Create a new Git tag “Lab2_v1.0” and push the tag to Github.



Python Main Entry Point, Console Input and String Processing

Python Main Entry Point

In the previous exercise, we have implemented Python code that calculates the BMI value using a user defined function “calculate_bmi”.

Also notice that we called the function “calculate_bmi()” directly instead of a central “main” function or entry point.

While this works for a simple single Python file application, calling Python functions directly from a file might become messy if the application comprises of several Python files.

In this case it would be better to define a single Python file and “main” function as an entry point to start the entire application.

We should define the main entry point function “main()” which can then be used to call other user defined functions.




In Python, the code below checks if the current script is the main Python file and then calls the function “main()” that we have defined in the step above.


Exercise 2:

For this exercise, we will develop a console application that allows the user to enter several numeric values and the Python code will calculate the average, minimum and maximum values for the list of temperature values.

In the Python file Lab2.py create the functions shown in Table 1 below, with only a single “print” statement to display the name of the function. The actual implementation of the functions in Table 1 will be completed in the next sections.

Example 1: For the function “display_main_menu()”


Example 2: For the function “calc_average()”,




Function Name
Input Parameter/s Type
Return Type
display_main_menu
None
None
get_user_input
None
List of Floats
calc_average
List
Float
find_min_max
List
List of Floats in the format [min_temp, max_temp]
sort_temperature
List
List of Floats sorted in ascending order
calc_median_temperature
List
Float


Table 3 – Functions to be added to Lab2.py file.

Console Input / Output, Strings and List Data Structures Exercise 3:

Based on the functions skeletons created in Table 3, complete the Python code implementation as shown in Table 4. Refer to Table 3 for the expected input parameters and return type for each function.


def display_main_menu():
   print("Enter some numbers separated by commas (e.g. 5, 67, 32)")


def get_user_input():
   get_user_input = input()
   get_user_input = get_user_input.split(",") # split the input string into a list


   # convert the list of STRINGS to a list of FLOATS - basically EVERY num in the list is being converted to float
   num_list = [float(num) for num in get_user_input]


   print(num_list) # print the list of floats
   return num_list  # return the num_list so that all other functions can use in the main funciton



Function name
Python code implementation
display_main_menu(
)
To display the following text:

“Enter some numbers separated by commas (e.g. 5, 67, 32)”
get_user_input()
Read from the terminal console a sequence of numbers entered by the user using the Python system function “input()”

https://www.w3schools.com/python/ref_func_input.asp


Use the Python function “split(“,”)” to split the user entered string into a Python List of strings based on the “,’ comma character.

https://www.w3schools.com/python/ref_string_split.as p


Convert the Python List of strings to a List of floats which can be used later for calculating average, minimum and maximum values

https://www.w3schools.com/python/python_lists.asp


Return the List of floats


Table 4 – Implementation of two functions in Lab2.py file.

Comparison and Arithmetic Operators

In this exercise, you will need to implement some mathematical operations to calculate the average, minimum and maximum values of the list of numbers entered by the user in the previous exercise.

Exercise 4:

Based on the functions created in Table 1, complete the Python code implementation as shown in Table 3. Refer to Table 1 for the expected input parameters and return type for each function.

def calc_average(num_list):
   average = sum(num_list) / len(num_list)
   print("Average: " + str(average))

def find_min_max(num_list):
   maximum_value = max(num_list)
   minimum_value = min(num_list)


   print("Max: " + str(maximum_value))
   print("Min: " + str(minimum_value))

Function name
Python code implementation
calc_average_temperature()
To return a float value of the calculated average value of all temperature readings.
calc_min_max_temperature()
To return an integer list with 2 values for minimum and maximum temperature.


Table 5 – Implementation of two more functions in Lab2.py file.


Commit, Push to GitHub and create Software Release

Exercise 5:

Add and Commit all changes to your local Git repository with appropriate commit messages that describe your code changes

Create a Git tag “Lab2_v1.1” in your local repository.

Push all committed changes in your local git repository to your remote GitHub repository.

Create a new Github release “Lab2_v1.1” based on the corresponding Git tag.


Additional Exercise 6:

Implement the function “calc_median_temperature()” defined in Table 1 which returns the median temperature from the list of numbers entered by the user. (Hint: Before deriving the median value, you will need to first sort all the numbers in the list in ascending order.)

Push all committed changes in your local repository to your remote GitHub repository

Create a new GitHub release “Lab2_v1.2” based on the corresponding Git tag.

lab 2 - https://github.com/izzaops/lab2 


lab2.py


from statistics import median




def main():
   print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
   display_main_menu()
   num_list = get_user_input()


   # uses number list
   calc_average(num_list)
   find_min_max(num_list)
   sorted_values = sort_temperature(num_list) # get sorted values from this function
   # uses sorted numbers list (ascending order)
   calc_median_temperature(sorted_values) # get median using the SORTED VALUES previously taken by previous function





def display_main_menu():
   print("Enter some numbers separated by commas (e.g. 5, 67, 32)")





def get_user_input():
   get_user_input = input()
   get_user_input = get_user_input.split(",") # split the input string into a list


   # convert the list of STRINGS to a list of FLOATS - basically EVERY num in the list is being converted to float
   num_list = [float(num) for num in get_user_input]


   print(num_list) # print the list of floats
   return num_list  # return the num_list so that all other functions can use in the main funciton





def calc_average(num_list):
   average = sum(num_list) / len(num_list)
   print("Average: " + str(average))





def find_min_max(num_list):
   maximum_value = max(num_list)
   minimum_value = min(num_list)


   print("Max: " + str(maximum_value))
   print("Min: " + str(minimum_value))





def sort_temperature(num_list):
   sorted_values = sorted(num_list)


   print("Values in ascending order: " + str(sorted_values))
   return sorted_values





def calc_median_temperature(sorted_values):
   median_value = median(sorted_values)
   print("Median temperature: " + str(median_value))


if __name__ == "__main__":
   main()


bmi.py


def calculate_bmi(height, weight):
   print("Height = " + str(height))


   print("Weight = " + str(weight))


   # calculate bmi, need to get height and weight from calculate_bmi function
   bmi = (weight / (height * 2))
   print("BMI = " + str(bmi))


   if (bmi < 18.5):
       print("Underweight")
       return -1
   elif (18.5 <= bmi <= 25.0):
       print("Normal weight")
       return 0
   else:
       print("Overweight")
       return 1


calculate_bmi(height=1.73, weight=57)
test_lab2.py


import pytest


import lab2.lab2 as lab2


# Test find_min_max()
def test_find_min_max():
   # Test with a list of integers
   num_list = [5, 3, 8, 1, 9]
   max_value, min_value = lab2.find_min_max(num_list)


   assert max_value == 9
   assert min_value == 1


# Test calc_average()
def test_calc_average():
   num_list = [5, 3, 8, 1, 9]
   average = lab2.calc_average(num_list)
   assert average == 5.2


# Test calc_median_temperature()
def test_calc_median_temperature():
   num_list = [5, 3, 8, 1, 9]
   median_value = lab2.calc_median_temperature(num_list)
   assert median_value == 5.0


if __name__ == "__main__":
   pytest.main()
