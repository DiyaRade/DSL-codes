"""PROBLEM STATEMENT: Write a Python program to compute following operations
on String:
a) To display word with the longest length
b) To determines the frequency of occurrence of particular character in the string
c) To check whether given string is palindrome or not
d) To display index of first appearance of the substring
e) To count the occurrences of each word in a given string

Name: Diya Rade
Class: SE Comp 2
Batch: R
Clg PRN: F24122005
Seat no: """


def longestlen(sen):
    words = sen.split()
    longw = max(words, key=len)
    return longw


def charfreq(str, c):
    f = str.count(c)
    return f


def palindrome(str):
    s = str.replace(" ", "").lower()
    return s == s[::-1]


def appear(str, sub):
    i = str.find(sub)
    if i != -1:
        return i
    else:
        return 0


def wordfreq(sen):
    words = sen.split()
    fq = {}
    for word in words:
        if word in fq:
            fq[word] += 1
        else:
            fq[word] = 1
    return fq


s = input("Enter string: ")

while True:
    print("1. To display word with the longest length")
    print(
        "2.To determines the frequency of occurrence of particular character in the string"
    )
    print("3.To check whether given string is palindrome or not")
    print("4.To display index of first appearance of the substring")
    print("5.To count the occurrences of each word in a given string")
    print("6. Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        print(f"Word with longest lenght: {longestlen(s)}")
    elif ch == 2:
        c = input("Enter character")
        print(f"Character {c} occurs {charfreq(s,c)} times")
    elif ch == 3:
        if palindrome(s):
            print("String is palindrome")
        else:
            print("String is not palindrome")
    elif ch == 4:
        sub = input("Enter substring: ")
        print(f"Index of first occurence of {sub} is {appear(s,sub)}")
    elif ch == 5:
        print(f"Occurence of each word {wordfreq(s)}")
    elif ch == 6:
        print("Exiting....")
        break
    else:
        print("Invalid choice")
