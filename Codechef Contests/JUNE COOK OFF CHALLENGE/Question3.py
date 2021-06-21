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

#Solution_2 : Optimized Approach..

from bisect import bisect_left

t1 = input()
n = int(t1.split()[0])
q = int(t1.split()[1])
t2 = input()
a = []
for n in t2.split():
    a.append(int(n))
a.sort()
l = len(a)
for i in range(q):
    n = int(input())
    idx = bisect_left(a, n)
    if idx < l and a[idx] == n:
        print(0)
    elif (l-idx == 0 ):
        if l%2 == 0:
            print('POSITIVE')
        else:
            print('NEGATIVE')
    elif (l-idx)%2 == 0:
        print('POSITIVE')
    else:
        print('NEGATIVE')
        
# cook your dish here


