"""
Problem: Divisible Sum Pairs

diff:easy
complexity=o(n)

"""

k=3
track=[0]*(k)
pairs=0
arr = [1, 3, 2, 6, 1, 2]

for i in range(len(arr)):
    temp=arr[i]%k
    pairs+=track[((k-temp)%k)]

    track[temp]+=1

print(pairs)
