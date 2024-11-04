"""PROBLEM STATEMENT: Write a Python program to store first year percentage of 
students in array. Write function for sorting array of floating point numbers in ascending 
order using
a)Selection Sort
b)Bubble sort and display top five scores.

Name: Diya Rade 
Class: SE Comp 2
Batch: R
Clg PRN: F24122005
Seat no: """


def selection(arr):
    for i in range(len(arr)):
        mini = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[mini]:
                mini = j
        arr[i], arr[mini] = arr[mini], arr[i]
    return arr


def bubble(arr):
    n = len(arr)
    for i in range(n):
        for j in range(1, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def top(arr):
    print("Top 5 scores: ")
    for i in range(-1, -6, -1):
        print(arr[i])


arr = [93.50, 90.70, 89.89, 91.03, 90.40]
while True:
    print("1. Selection sort")
    print("2. Bubble sort")
    print("3. Top 5 scores")
    print("4. Exit")
    ch = int(input("Enter choice: "))
    if ch == 1:
        print(f"Using Selection sort: {selection(arr)} ")
    elif ch == 2:
        print(f"Using bubble sort: {bubble(arr)} ")
    elif ch == 3:
        top(bubble(arr))
    elif ch == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice")
