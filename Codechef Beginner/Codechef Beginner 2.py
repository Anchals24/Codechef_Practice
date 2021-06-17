""" 
Codechef Beginner :

Problem Name : Enormous Input Test  

"""
#Solution:

x = input()
first_s = x.split()
n = int (first_s[0])
k = int (first_s[1])
count = 0
for i in range(n):
    T = input()
    if int(T) % k == 0:
        count += 1
print(count)

