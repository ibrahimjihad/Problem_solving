"""
Problem: Subarray Division

diff:easy


"""
def birthday(s, d, m):
    count=0
    for i in range(len(s)-(m-1)):
        print(i)
        sum=0
        for x in range(i,i+m):
            sum+=s[x]
        if sum==d:
            count+=1
        sum=0
    print(count)
            
if __name__ == '__main__':

    n = 1

    s = [4]
    d = 4

    m = 1

    result = birthday(s, d, m)
