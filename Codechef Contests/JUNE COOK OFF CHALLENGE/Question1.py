#Question_1 : VISA

T = int(input())
for t in range(T):
    In = input()
    L = In.split()
    x1 = int(L[0])
    x2 = int(L[1])
    y1 = int(L[2])
    y2 = int(L[3])
    z1 = int(L[4])
    z2 = int(L[5])
    if x2 >= x1 and y2 >= y1 and z2 <= z1:
        print ("YES")
    else:
        print( "No" )

#Time Complexity : O(T)
