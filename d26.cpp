/*PROBLEM STATEMENT: In any language program mostly syntax error occurs due to 
unbalancing delimiter such as (), {}, []. Write C++ program using stack to check whether 
given expression is well parenthesized or not. 

Name: Diya Rade
Class: SE Comp 2
Batch: R
Clg PRN: F24122005
Seat no: */
#include <iostream>
#include <stack>
using namespace std;
bool isWellParenthesized(string expression) {
 stack<char> s;
 for (char ch : expression) {
 if (ch == '(' || ch == '{' || ch == '[') {
 s.push(ch);
 }
 else if (ch == ')' || ch == '}' || ch == ']') {
 if (s.empty()) return false;
 char top = s.top();
 s.pop();
 
 if ((ch == ')' && top != '(') || 
 (ch == '}' && top != '{') || 
 (ch == ']' && top != '[')) {
 return false;
 }
 }
 }
 return s.empty();
}
int main() {
 string expression;
 cout << "Enter an expression: ";
 cin >> expression;
 if (isWellParenthesized(expression)) {
 cout << "The expression is well parenthesized." << endl;
 } else {
 cout << "The expression is not well parenthesized." << endl;
 }
 return 0;
}

