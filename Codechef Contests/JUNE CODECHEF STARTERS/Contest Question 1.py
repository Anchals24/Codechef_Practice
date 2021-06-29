"""
Question : Cyclic Quadrilateral

"""


T = int(input())
for t in range(T):
    Inp = input()
    L = Inp.split()
    A = int(L[0])
    B = int(L[1])
    C = int(L[2])
    D = int(L[3])
    if A + C == 180 and B + D == 180:
        print("YES")
    else:
        print("NO")

#Complexity : O(n)