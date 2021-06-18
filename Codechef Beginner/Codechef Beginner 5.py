""" 
Codechef Beginner: 
Problem : Sum of Digits

"""

#Solution 1:

lines = input()
T = int(lines)
for t in range(T):
    n = input()
    N = list(n)
    add = 0
    leng = len(N)
    for r in range(leng):
        add = add + int(N[r])
    print(add)


#It was using list.
#Complexity : O(1)

#Solution 2:

lines = input()
T = int(lines)
for t in range(T):
    N = input()
    add = 0
    leng = len(N)
    for r in range(leng):
        add = add + int(N[r])
    print(add)