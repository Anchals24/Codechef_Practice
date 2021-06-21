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
    
#Complexity : O(T)
    
#Question : Golf
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
        
#Time Complexity : O(T)
