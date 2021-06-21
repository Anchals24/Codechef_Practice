#Question_3 : The Wave

#Solution_1 : Got TLE...

IN = input()
L = IN.split()
Root = input()
N = int(L[0])
Q = int(L[1])
Roots = Root.split()

for q in range(Q):
    x = int(input())
    mul = 1
    for r in Roots:
        sub = x - int(r)
        mul = mul * sub
    if mul < 0:
        print( "NEGATIVE")
    elif mul > 0:
        print("POSITIVE") 
    else:
        print (0)     

#Time Complexity: O(q*r)

