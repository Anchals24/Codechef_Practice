""" 
Codechef Beginner :
Problem : Turbo Sort

"""

#Solution_1 : TLE 

Test = input()
T = int(Test)
L = []
for t in range(T):
    Num = input()
    L.append(Num)
    L.sort()
    leng = len(L)
print(L)
leng = len(L)
for l in range(leng):
    L[l] = int(L[l])
print(L)

#Solution_2 : Optimized Approach...

Test = input()
T = int(Test)
L = []
for t in range(T):
    Num = input()
    N = int(Num)
    L.append(N)
L.sort()
Leng = len(L)
for l in range(Leng):
    print(L[l])