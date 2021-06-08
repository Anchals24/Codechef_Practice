# Question : Solubility 

T = int(input())
for t in range(T):
    Inp = input()
    L = Inp.split()
    X = int(L[0])
    A = int(L[1])
    B = int(L[2])
    if X <= 100:
        PT = (100 - X) * B
        Ans = (PT + A) * 10
    print(Ans)
    
    
#Question : Golf

#First Approach : Got TLE...
T = int(input())
for t in range(T):
    In = input()
    L = In.split()
    N = int(L[0])
    x = int(L[1])
    k = int(L[2])
    Li = []
    for n in range(0 , N+2):
        Li.append(n)
    #print(Li)
    LENG = len(Li)
    for i in range(LENG):
        Flag = False
#forward
        if x == L[0]:
            Flag = True
    
            break
        else:
            comp1 = k
            if comp1 == x:
                Flag = True
                break
            else:
                y = 0
                y += 1
                comp1 = (1+y) * comp1
        #backward
        if L[-1] == x or k == N+1:
            Flag = True
            break
        else:
            comp2 = k
            a = comp2
            if ((N+1) - a) == x:
                Flag = True
            else:
                z = 0
                z += 1
                a = (1+z) * comp2
    if Flag == True:
        print("Yes")
    else:
        print("No")



#Optimized Approach

T = int(input())
for t in range(T):
    Inp = input()
    L = Inp.split()
    N = int(L[0])
    x = int(L[1])
    k = int(L[2])
    d1 = x - 0
    d2 = (N+1) - x
    if d1 % k == 0:
        print("Yes")
    elif d2 % k == 0:
        print("Yes")
    else:
        print("No")
