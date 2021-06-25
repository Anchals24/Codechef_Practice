Rounds = int(input())
Play1_S = []
Play2_S = []
Play1_C = []
Play2_C = []
Winners = []
lead_runs = []
winner = 'none'
lead = 0
for r in range(Rounds):
    score = input()
    Roundwisescore = score.split()
    Player1 = int(Roundwisescore[0])
    Player2 = int(Roundwisescore[1])
    Play1_S.append(Player1)
    Play2_S.append(Player2)
leng = len(Play1_S)
for l in range(leng):
    C_Sum1 = sum(Play1_S[:l+1])
    C_Sum2 = sum(Play2_S[:l+1])
    Play1_C.append(C_Sum1)
    Play2_C.append(C_Sum2)
    if Play1_C[l]-Play2_C[l] > Play2_C[l]-Play1_C[l]:
        winner = '1'
        lead = Play1_C[l]-Play2_C[l]
    else:
        winner = '2'
        lead = Play2_C[l]-Play1_C[l]
    Winners.append(winner)
    lead_runs.append(lead)
answer = max(lead_runs)
leader= lead_runs.index(answer)
print(Winners[leader],answer)
