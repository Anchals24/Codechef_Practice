#Question 1: ATM
""" Solution 1 : Runtime Error """

x , y   = [int(x) for x in input().split()]
if int(x) % 5 == 0:
    x = float(x) + 0.50
    y = float(y) - float(x)
print (y)

""" Solution 2 : Correct Approach """
x = input()
amount = x.split()
with_am = int(amount[0])
current_am = float(amount[1])
if (with_am % 5 == 0) and (with_am < current_am):
    y = with_am + 0.50
    z = current_am - y
    if z >= 0:
        print(z)
    else:
        print(current_am)   
else:
    print(current_am)


#Time Complexity : O(1) 



