Codio Coding Assignment 9.1: GitHub and Advanced Python Functions
Learning Outcomes Addressed

        Use GitHub for version control.
        Implement Python classes.
        Write code using advanced Python functions.
        Utilize Python decorator and wrappers.

Index:

    Question 1
    Question 2
    Question 3
    Question 4
    Question 5
    Question 6
    Question 7
    Question 8
    Question 9
    Question 10
    Question 11
    Question 12
    Question 13

Python Classes
Question 1

5 points

Write a Python class, Student, with no attributes assigned to it.

Assign the type of Student to ans1a. Assign the __module__ attribute of the Student class to ans1b.

HINT: Because Student does not have any attributes, you can end its definition with the keyword pass.

### GRADED

​

### YOUR SOLUTION HERE

ans1a = type(Student)

ans1b = Student.__module__

​

# YOUR CODE HERE

class Student:

def__init__(self)

__module__

pass

​

Question 2

5 points

Modify the Python class, Student so that it has two attributes, student_name and grade, with values John Smith and 86, respectively.

Assign the member student_name of the class Student to ans2a.

### GRADED

​

### YOUR SOLUTION HERE

ans2a = None

​

​

# YOUR CODE HERE

class Student:

    def __init__(self, student_name, grade)

    self.name = John Smith

    self.grade = 86

    p1 = Person("John Smith", 86)

    

    print(p1.name)

    print(p1.grade)

​

Question 3

7 points

The Python function setattr can be used to modify the attributes of a class. It basic syntax reads as follow:

setattr = (class_name, attribute_name, updated_value)

Use the function setattr to modify the Python class, Student so that student_name and grade are equal to Angela Brooks and 87, respectively. Assign these operations to ans3a and ans3b, respectively.

### GRADED

​

### YOUR SOLUTION HERE

ans3a = setattr(Student, 'student_name', 'Angela Brooks')
setattr(Student, 'grade', 87)

# Assign to ans3a and ans3b
ans3a = Student.student_name
ans3b = Student.grade

​

# YOUR CODE HERE

class Student:

    def __init__(self.Student_name, grade)

    self.Student_name = Angela Brooks

    self.grade = 87

    p1= Student1()

    Angela Brooks

    settatr(p1. 'Student.name', 'Angela Brooks', 'grade', 87)

    print("After modification, p.name, p.grade")

    

​

Question 4

6 points

Use a constructor to define a Python class, Student, with attributes student_name, student_id, grade, and email.

Construct a student, ans4, with name equal to Francis Green, student ID equal to 475895, grade equal to 56, and email address equal to francisgreen@mit.edu.

### GRADED

​

### YOUR SOLUTION HERE

ans4 = Student("Francis Green", 475895, 56, "francisgreen@mit.edu")

​

​

# YOUR CODE HERE

class Student:

    def __init__(self, self.student_name, self.student_id, self.grade, self.email.)

    self.student_name = Francis Green

    self.student_name = 475895

    self.grade = 56

    self.email = francisgreen@mit.edu

    print("student_name", "student_id", "grade", "email")

    

​

Question 5

7 points

Add a function, curved_average, to the Student class defined above that takes the value stored in grade and multiplies it by 1.2. This function should return a value updated_grade.

Compute the updated average of the student ans4 computed in the previous questions and assign the result to ans5.

### GRADED

​

### YOUR SOLUTION HERE

ans5 = def curved_average(self):
        updated_grade = self.grade * 1.2
        return updated_grade

# Construct a student
ans4 = Student("Francis Green", 475895, 56, "francisgreen@mit.edu")

# Compute the updated average
ans5 = ans4.curved_average()
​

​

# YOUR CODE HERE

class Student class:

def __init__(self.student_class,self.grade):

    self.Student class=student class

    self.grade=grade

    def curved_average(self, self.Student class, self.grade)

    updated_grade = grade=self.grade*1.2

    print("updated_grade")

​

Advanced Functions
Question 6

7 points

Define a function, my_sum, that computes the sum of a variable number of elements.

Assign the result of the sum of the elements 1,3,5,6, and 10 to ans6a. Assign the result of the sum of the elements 10,4,6, and 2 to ans6b.

### GRADED

​

### YOUR SOLUTION HERE

ans6a = ef my_sum(args):
    return sum(args)

# Compute the sum of elements
ans6a = my_sum(1, 3, 5, 6, 10)
ans6b = my_sum(10, 4, 6, 2)



​

# YOUR CODE HERE

def__init__(self, 1,3,5,6)

     def my_sum(self)

    return sum(self)

​

​

Question 7

8 points

Define a function, my_average, that computes the average of a variable number of elements.

Assign the result of the sum of the elements 78,82,91,66 to ans7a. Assign the result of the sum of the elements 56, 89,76, and 100 to ans6b.

### GRADED

​

### YOUR SOLUTION HERE

def my_average(*args):
    if not args:
        return 0
    return sum(args) / len(args)

# Compute the averages of elements
ans7a = my_average(78, 82, 91, 66)
ans7b = my_average(56, 89, 76, 100)
​

# YOUR CODE HERE

def __init__(self)

numbers = [78,82,91,66]

def my_average= for number in numbers:

    total+= number

    number / len(numbers)

return my_average

​

Question 8

7 points

Suppose an invidual, say person1, has Name equal to Rosie, Age equal to 33, and Profession equal to Data Scientist.

Next, suppose that another person, say person2*, has Name equal to Kyle, Age equal to 28, and Profession equal to Data Engineer. and phone number equal to 4659874982.

Finally, define a function, print_last_info(), that unpacks the given entries and returns the string in the format:

<key_n> is <value_n>.

Note that in the pseudocode above, n represents the index for the last elements of the arguments passed to the function.

Call the function with person1, and person2 and assign the results to ans8a and ans8b, respectively.

### GRADED

​

### YOUR SOLUTION HERE

# Define persons
person1 = {"Name": "Rosie", "Age": 33, "Profession": "Data Scientist"}
person2 = {"Name": "Kyle", "Age": 28, "Profession": "Data Engineer", "phone number": 4659874982}

# Call the function with persons and assign the results
ans8a = print_last_info(**person1)
ans8b = print_last_info(**person2)
​

​

# YOUR CODE HERE

class Data Scientist:

def__init__(self.Name, Age, Profession)

person1 = self.Name = Rosie, self.Age = 33, self.Profession = Data Scientist

​

person2 = self.Name = Kyle, self.Age = 28, self.Profession = Data Engineer, self.phone_number = 4659874982

def__init__print_last_info()

print_last_info=[-1]

​

                           

​

​

​

Question 9

7 points

Define a dictionary, movie, with keys Title, Director, and Year and corresponding values Inception, Nolan, and 2010.

Define a function, print_movie(), that unpacks the entries of a provided dictionary and returns the string in the format:

<title_name_key>: <title_name_value>

Call the function with the dictionary movie and assign the result to ans9a.

What happens if you also pass the argument Music = "Zimmer" after movie? Assign the resulting string to ans9b

### GRADED

​

### YOUR SOLUTION HERE


# Call the function with movie dictionary and assign the result
ans9a = print_movie(**movie)

# Add 'Music' key-value pair to movie dictionary
movie["Music"] = "Zimmer"

# Call the function with updated movie dictionary and assign the result
ans9b = print_movie(**movie)
​

​

​

# YOUR CODE HERE

Film = {"Title": "Inception", "Director": "Nolan", "Year": 2010}

def__init__print_movie()

prin_movie = title_name_key>: <title_name_value>

​

​

​

Decorators and Wrappers
Question 10

6 points

Define a function, plus_one, that takes an integer as input. Within this function, define another *function, add_one that takes the same integer as input. This function should add 1 to the integer and return the result.

Finally, the function, plus_one should call the *function, add_one, and return the result.

Test your functions with the number 7 and assign the result to ans10.

### GRADED

​

### YOUR SOLUTION HERE

ans10 = plus_one(7)
# YOUR CODE HERE



​

Question 11

7 points

Define a function, uppercase_decorator, that takes a function as an input. This function will contain a wrapper function, wrapper, that will convert a string to uppercase.

Define another function, say_hello(), that takes no argument and returns the string hello there!. Pass the function, say_hello() to uppercase_decorator and assign the result to ans11.

### GRADED

​

### YOUR SOLUTION HERE

ans11 = uppercase_decorator(say_hello)()

def say_hi():

    pass

# YOUR CODE HERE

raise NotImplementedError()

​

Question 12

9 points

Define a function, decorator_with_arguments, that takes a function as an input. This function will contain a wrapper function, wrapper_accepting_arguments that will take two strings as input and will print the string My arguments are: <arg1>, <arg2>.

This last step can be accomplished via the command:

print("My arguments are: {0}, {1}".format(arg1,arg2))

The function, decorator_with_arguments should return the function, wrapper_accepting_arguments.

Define another function, cities, that takes two arguments and print the string Cities I love are: <arg1>, <arg2>.

This last step can be accomplished via the command:

 print("Cities I love are {0} and {1}".format(city_one, city_two))

Test your functions with the cities Paris and New York and assign the result to ans12.

### GRADED

​

### YOUR SOLUTION HERE

ans12 = None

def cities(city_one, city_two):

    pass

​

# YOUR CODE HERE

raise NotImplementedError()

​

Question 13

9 points

Define a function, decorator_passing_arbitrary_arguments, that takes a function as an input. This function will contain a wrapper function, wrapper_accepting_arbitrary_arguments that will take a variable number of arguments as input and will print the string The positional arguments are (<arg1, arg2, arg3...>).

This last step can be accomplished via the command:

print('The positional arguments are', args)

The function, decorator_passing_arbitrary_arguments should return the function, wrapper_accepting_arbitrary_arguments.

Define another function, function_with_arguments, that takes three arguments and returns them as a tuple.

Test your functions with the arguments 1, 2 and 3 and assign the result to ans13.

### GRADED

​

### YOUR SOLUTION HERE

ans13 = None

def function_with_arguments(arg1, arg2, arg3):

    pass

​

# YOUR CODE HERE

def decorator_passing_arbitrary_arguments(func):
    def wrapper_accepting_arbitrary_arguments(*args):
        print('The positional arguments are', args)
        return func(*args)
    return wrapper_accepting_arbitrary_arguments

def function_with_arguments(arg1, arg2, arg3):
    return arg1, arg2, arg3

raise NotImplementedError()

​