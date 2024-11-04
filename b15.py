"""PROBLEM STATEMENT: Write a python program to store second year percentage 
of students in array. Write function for sorting array of floating point numbers in ascending 
order using
a) Insertion sort
b) Shell Sort and display top five scores

Name: Diya Rade
Class: SE Comp 2
Batch: R
Clg PRN: F24122005
Seat no: """


def insertion(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def shell(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr


def top(arr):
    print("Top 5 scores: ")
    for i in range(-1, -6, -1):
        print(arr[i])


arr = [93.50, 90.70, 89.89, 91.03, 90.40]
while True:
    print("1. Insertion sort")
    print("2. Shell sort")
    print("3. Top 5 scores")
    print("4. Exit")
    ch = int(input("Enter choice: "))
    if ch == 1:
        print(f"Using Insertion sort: {insertion(arr)} ")
    elif ch == 2:
        print(f"Using Shell sort: {shell(arr)} ")
    elif ch == 3:
        top(shell(arr))
    elif ch == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice")
