""" 
Codechef Beginner :
Problem :  Reverse The Number
"""
#Solution :

T = int(input())
for t in range(T):
    str1 = " "
    N = int(input())
    while N != 0:  
        digit = N % 10  #Breaking an integer into digits
        str1 += str(digit)
        N = N // 10
    str1 = int(str1)
    print(str1)


#complexity : O(T * N)