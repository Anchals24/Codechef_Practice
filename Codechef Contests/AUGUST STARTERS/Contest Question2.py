#Aproach1 >> Brute-Force solution >> TLE

T = int(input())
for t in range(T):
    Input = input()
    Input = Input.split()
    N , K , S = int(Input[0]) , int(Input[1]) , int(Input[2])
    Initialoddnumbers = []
    cnt = 0
    number = 1
    while cnt != N:
        if number % 2 != 0:
            Initialoddnumbers.append(number)
            number += 1
            cnt += 1
        else:
            number += 1
    K = K-1
    sumofarray = sum(Initialoddnumbers)
    #print(sumofarray)
    for odd in Initialoddnumbers:
        #print("odd is" , odd)
        if sumofarray + K* (odd) == S:
            print(odd)

#Approach2 >> Optimized Code 

T = int(input())
for t in range(T):
    Input = input()
    Input = Input.split()
    N , K , S = int(Input[0]) , int(Input[1]) , int(Input[2])
    sumofoddnum = N * N #Formula to calculate the sum of N odd numbers.
    K = K-1
    cnt = 0
    num = 1
    while cnt != N:
        if num % 2 != 0:
            cnt += 1
        if K *(num) + sumofoddnum == S:
            print(num)
            break
        num += 1