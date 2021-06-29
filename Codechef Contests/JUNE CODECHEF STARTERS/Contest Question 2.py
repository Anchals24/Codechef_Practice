"""

Question 2: Chess Match

"""

T = int(input())
for t in range(T):
    Inp = input()
    L = Inp.split()
    N = int(L[0])
    A = int(L[1])
    B = int(L[2])
    Part1 = 2 * (180 + N)
    Part2 = A + B
    Ans = Part1 - Part2
    print(Ans)

#Complexity : O(n)
