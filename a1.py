def removeDuplicate(d):
    l3 = []
    for i in d:
        if i not in l3:
            l3.append(i)
    return l3


def intersection(l1, l2):
    l3 = []
    for val in l1:
        if val in l2:
            l3.append(val)
    return l3


def union(l1, l2):
    l3 = []
    l3 = l1.copy()
    for val in l2:
        if val not in l3:
            l3.append(val)
    return l3


def diff(l1, l2):
    l3 = []
    for val in l1:
        if val not in l2:
            l3.append(val)
    return l3


def sym_diff(l1, l2):
    l3 = []
    d1 = diff(l1, l2)
    d2 = diff(l2, l1)
    l3 = union(d1, d2)
    return l3


def cnb(l1, l2):
    l3 = intersection(l1, l2)
    return l3


def corbnotboth(l1, l2):
    l3 = sym_diff(l1, l2)
    return l3


def ncnb(l1, l2, l3):
    l3 = diff(l1, union(l2, l3))
    return l3


def candfnotb(l1, l2, l3):
    l3 = diff(intersection(l1, l2), l3)
    return l3


all = []
n = int(input("Enter total no of student: "))
for i in range(n):
    print(f"Enter name of student {i+1}")
    ele = input()
    all.append(ele)
print("Students are: ")
for i in all:
    print(i)

c = []
n = int(input("Enter no of student who play cricket: "))
for i in range(n):
    print(f"Enter name of student {i+1}")
    ele = input()
    c.append(ele)
c = removeDuplicate(c)
print("Students who play cricket are: ")
for i in c:
    print(i)

b = []
n = int(input("Enter no of student who play badminton: "))
for i in range(n):
    print(f"Enter name of student {i+1}")
    ele = input()
    b.append(ele)
b = removeDuplicate(b)
print("Students who play badminton are: ")
for i in b:
    print(i)

f = []
n = int(input("Enter no of student who play football: "))
for i in range(n):
    print(f"Enter name of student {i+1}")
    ele = input()
    f.append(ele)
f = removeDuplicate(f)
print("Students who play football are: ")
for i in c:
    print(i)

while True:
    print("1. List of students who play both cricket and badminton")
    print("2. List of students who play either cricket or badminton but not both")
    print("3. Number of students who play neither cricket nor badminton")
    print("4. Number of students who play cricket and football but not badminton")
    print("5. Exit")
    ch = int(input("Enter choice: "))
    if ch == 1:
        l3 = cnb(c, b)
        print(f"Students who play both cricket and badminton{l3}")
    elif ch == 2:
        l3 = corbnotboth(c, b)
        print(f"students who play either cricket or badminton but not both{l3}")
    elif ch == 3:
        l3 = ncnb(all, c, b)
        print(f"students who play neither cricket nor badminton{len(l3)}")
    elif ch == 4:
        l3 = candfnotb(c, f, b)
        print(
            f"Number of students who play cricket and football but not badminton{len(l3)}"
        )
    elif ch == 5:
        print("Exiting....")
        break
    else:
        print("Invalid choice")
