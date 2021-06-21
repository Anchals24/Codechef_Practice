#Question_2 : BALLOON

T = int(input())
for t in range(T):
    N = int(input())
    In = input()
    L = In.split()
    VIBGYOR = ['1' , '2' , '3', '4', '5', '6' ,'7']
    Matching = ['YES' ,'YES', 'YES','YES','YES','YES','YES' ]
    Cnt = 0
    for i in L:
        Cnt += 1
        for j in range(len(VIBGYOR)):
            if i == VIBGYOR[j]:
                VIBGYOR[j] = 'YES'
        if VIBGYOR == Matching:
            break
    print(Cnt)

#Complexity : O(T * L)
# cook your dish here
