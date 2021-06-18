""" 
Codechef Beginner:
Problem : Find Remainder

"""
Test = input()
T = int(Test)
for t in range(T):
    rem = input()
    spl_f = rem.split()
    A = int(spl_f[0])
    B = int(spl_f[1])
    C = A % B
    print(C)

#Complexity : O(n)