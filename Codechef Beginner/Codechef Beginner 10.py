""" 
Codechef Beginner :
Problem : LUCKFOUR
"""

#Solution:

T = int(input())
for t in range(T):
    count = 0
    N = int(input())
    while N != 0:
        digit = N % 10
        if digit == 4:
            count += 1
        N = N // 10
    print(count)
        
#Complexity : O(T * N)