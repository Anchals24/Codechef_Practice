""" 
Codechef Beginner :
Problem :  Chef and Remissness
"""

#After so many wrong attempts , finally I was able to solve it.

mini = 0 
maxi = 0
T = int(input())
for t in range(T):
    E = input()
    Entry = E.split()
    A = int(Entry[0])
    B = int(Entry[1])
    if A >= B:
        mini = A
    else:
        mini = B
    maxi = A+B
    print(mini, maxi)

