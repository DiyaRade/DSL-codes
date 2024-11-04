"""PROBLEM STATEMENT: Write a Python program to store marks scored in subject 
“Fundamental of Data Structure” by N students in the class. Write functions to compute 
following:
a) The average score of class
b) Highest score and lowest score of class
c) Count of students who were absent for the test
d) Display mark with highest frequency

Name: Diya Rade
Class: SE Comp 2
Batch: R
Clg PRN: F24122005
Seat no: """


def getStudentMarks():
    n = int(input("Enter total no of students: "))
    marks = []
    for i in range(n):
        ele = input(f"Enter marks of student {i+1} or A if absent")
        if ele.upper() == "A":
            marks.append(None)
        else:
            marks.append(int(ele))
    return marks


def average(marks):
    valid = [mark for mark in marks if mark is not None]
    if valid:
        return sum(valid) / len(valid)
    return 0


def highestLowest(marks):
    valid = [mark for mark in marks if mark is not None]
    if valid:
        return max(valid), min(valid)
    return None, None


def absent(marks):
    return marks.count(None)


def frequency(marks):
    valid = [mark for mark in marks if mark is not None]
    if not valid:
        return None

    fd = {}
    for mark in marks:
        if mark in fd:
            fd[mark] += 1
        else:
            fd[mark] = 1
    maxf = 0
    hf = None

    for mark, f in fd.items():
        if f > maxf:
            maxf = f
            hf = mark
    return hf


marks = getStudentMarks()
while True:
    print("1. The average score of class")
    print("2. Highest score and lowest score of class")
    print("3. Count of students who were absent for the test")
    print("4. Display mark with highest frequency")
    print("5. Exit")
    ch = int(input("Enter choice: "))
    if ch == 1:
        print(f"Average Score{average(marks)}")
    elif ch == 2:
        mx, mn = highestLowest(marks)
        print(f"Highest score is {mx} and lowest acore is {mn}")
    elif ch == 3:
        print(f"Number of absent student {absent(marks)}")
    elif ch == 4:
        print(f"Marks with highest frequency {frequency(marks)}")
    elif ch == 5:
        print("Exiting....")
        break
    else:
        print("Invalid Choice")
