"""
Problem: Migratory birds

diff:easy

"""
m=0
lst=[1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]

ch=[0]*(len(lst))

for i in lst:
    ch[i]+=1
for z in range (len(lst)):
    if ch[z]>m:
        m=z
print(m)
