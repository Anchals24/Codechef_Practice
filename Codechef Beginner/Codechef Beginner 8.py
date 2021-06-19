""" 
Codechef Beginner :
Problem : First and Last Digit.

"""
#Solution 1 : Using for loop...

Test = input()
T = int(Test)
for t in range(T):
    Num = input()
    leng = len(Num)
    for n in range(leng):
        N = int(Num[0]) + int(Num[-1])
    print(N)

#Complexity : O(T*n)

#Solution 2 : Optimized Approach....

Test = input()
T = int(Test)
for t in range(T):
    Num = input()
    N = int(Num[0]) + int(Num[-1])
    print(N)

#Complexity : O(n)

#Solution 3 : Breaking an integer...

T = int(input())
for t in range(T):
    L = []
    n = int(input())
    while n != 0:
        digit = n % 10
        L.append(digit)
        n = n//10
    
    sum = L[0] + L[-1]
    print(sum)

#Complexity : O(T * n)

