""" 
Codechef Beginner :
Problem :  Finding Square Roots

After so many wrong attempts , was able to solve this...
"""

#Solution_1 : (Wrong Attempt)

N = 9
i = 0
while i*i <= N:
    i += 1
print(i-1)

#Drawback : It was working on a few cases only.

#Solution_2 : (Correct Solution...)

T = int(input())
for t in range(T):
    N = int(input())
    i = 0
    while i*i <= N:
        i += 1
    print(i-1)

#Complexity : O(T * n)

#Solution_3 : (Correct Solution)

T = int(input())
for t in range(T):
    N = int(input())
    if N == 0:
        print(0)
    elif N == 1:
        print(1)
    for i in range(N):
        if i*i <= N and (i+1)*(i+1) > N:
            print(i)

#Complexity : O(T * n)

