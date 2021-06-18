""" 
Codechef Beginner :
Problem : Add Two Numbers 

"""

#Solution: 

Num = input()
T = int(Num)
for t in range(T):
    x = input()
    first_s = x.split()
    A = int(first_s[0])
    B = int(first_s[1])
    C = A + B
    print(C)

#Complexity : O(n)
