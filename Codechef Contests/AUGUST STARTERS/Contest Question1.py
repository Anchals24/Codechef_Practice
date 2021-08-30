#Starters Ques1:

T = int(input())
for t in range(T):
    Input = input()
    Input = Input.split()
    SA , SB , SC =  int(Input[0]) ,  int(Input[1]) , int(Input[2])
    smaller = 100000000000000000000000000000000
    winner = None
    if SA < smaller:
        smaller = SA
        winner = "Draw"
    if SB < smaller:
        smaller = SB
        winner = "Bob"
    if SC < smaller:
        smaller = SC
        winner = "Alice"
    print(winner)