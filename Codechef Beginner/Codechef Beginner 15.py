""" 
Codechef Beginner :
Problem :  Chef and Operators.
"""

T = int(input())
for t in range(T):
    x = input()
    L = x.split()
    A = int(L[0])
    B = int(L[1])
    if A > B:
        print('>')
    elif A < B:
        print('<')
    else:
        print('=')
