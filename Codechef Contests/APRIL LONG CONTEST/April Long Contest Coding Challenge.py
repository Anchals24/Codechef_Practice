
#Question_1 : SOCKS1


S = input()
L = S.split()
A = int(L[0])
B = int(L[1])
C = int(L[2])
if (1 <= A <= 10) and (1 <= B <= 10) and (1 <= C <= 10):
    if (A == B):
        print('YES')
    elif (A == C):
        print('YES')
    elif (B == C):
        print('YES')
    else:
        print('NO')


#Question 2 : BOLT


T = int(input())
for t in range(T):
    I = input()
    T = I.split()
    k1 = float(T[0])
    k2 = float(T[1])
    k3 = float(T[2])
    v = float(T[3])
    F_S = (k1 * k2 * k3 * v)
    TT = 100 / F_S
    if round(TT , 2) < 9.58:
        print('yes')
    else:
        print('no')


#Question 3: STRONG LANGUAGE

T = int(input())
for t in range(T):
    I = input()
    L = I.split()
    N = int(L[0])
    K = int(L[1])
    S = input()
    c = 0
    max_c = 0
    for s in S:
        if s == '*':
            c += 1
            max_c = max(c , max_c)
            if max_c >= K:
                print('YES')
                break
        else:
            c = 0
    if max_c < K:
        print('NO')
