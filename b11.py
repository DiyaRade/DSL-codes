"""PROBLEM STATEMENT:
a) Write a Python program to store roll numbers of student in array who attended training 
program in random order. Write function for searching whether particular student 
attended training program or not, using Linear search and Sentinel search.
b) Write a Python program to store roll numbers of student array who attended training 
program in sorted order. Write function for searching whether particular student attended 
training program or not, using Binary search and Fibonacci search

Name: Diya Rade
Class: SE Comp 2
Batch: R
Clg PRN: F24122005
Seat no: """

size = 10
sorted = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
random = [90, 50, 30, 60, 100, 10, 80, 20, 70, 40]
fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


def linear():
    print(f"Student id: {random}")
    key = int(input("Enter stusent id: "))
    index = 0
    for x in random:
        if x == key:
            print("Student attended training program")
            break
        else:
            index += 1
        if index == size:
            print("Student not attended training program")


def sentinel():
    print(f"Student id: {random}")
    key = int(input("Enter student id: "))
    last = random[size - 1]
    random[size - 1] = key
    comp = 0
    index = 0
    for x in random:
        if x == key:
            comp += 1
            break
        else:
            index += 1
            comp += 1
    if comp < size or key == last:
        print("Student attended training program")
    else:
        print("Student not attended training program")


def binary():
    print(f"Student id: {sorted}")
    key = int(input("Enter student id: "))
    low = 0
    high = len(sorted) - 1
    mid = 0
    while low <= high:
        mid = int((low + high) / 2)
        if key == sorted[mid]:
            print("Student attended training program")
            break
        elif key < sorted[mid]:
            high = mid - 1
        else:
            low = mid + 1
    if low > high:
        print("Student not attended training program")


def fibonacci():
    print(f"Student id: {sorted}")
    key = int(input("Enter student id: "))
    k = 0
    while fib[k] < len(sorted):
        k += 1
        offset = -1
        comp = 0
    while k > 0:
        i = min((offset + fib[k - 2]), len(sorted) - 1)
        if key == sorted[i]:
            print("Student attended training program")
            break
        elif key > sorted[i]:
            k = k - 1
            offset = i
        else:
            k = k - 2
        if k <= 0:
            print("Student not attended training program")


while True:
    print("1. Linear search")
    print("2. Sentinel search")
    print("3.Binary search")
    print("4. Fibonacci search")
    print("5. Exit")
    ch = int(input("Enter choice: "))
    if ch == 1:
        linear()
    elif ch == 2:
        sentinel()
    elif ch == 3:
        binary()
    elif ch == 4:
        fibonacci()
    elif ch == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice")
