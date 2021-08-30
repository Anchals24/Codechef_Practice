#Question 3

T = int(input())
for t in range(T):
    Input1 = input()
    Input1 = Input1.split()
    N, K = int(Input1[0]) , int(Input1[1])
    Input2 = input()
    Givenarr = Input2.split()
    Negative = []
    maxadd = 0
    cnt = 0
    for ele in Givenarr:
        if int(ele) < 0:
            Negative.append(int(ele))
            cnt += 1
        else:
            maxadd = maxadd + int(ele)
    if cnt > 0 and K>0 and cnt <= K:
        Negative.sort()
        for n in range(K):
            mul = Negative[n] * (-1)
            maxadd = maxadd + mul
    print(maxadd)