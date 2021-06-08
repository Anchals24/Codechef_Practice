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