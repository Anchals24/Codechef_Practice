""" 
Codechef Beginner :
Problem : Small factorials 

"""

#Solution:

Test = input()
T = int(Test)
for t in range(T):
    number = input()
    n = int(number)
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    print(fact)

#Complexity : O(T*n)