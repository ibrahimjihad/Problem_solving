"""
Problem: breaking the records

diff:easy


"""
def breakingRecords(scores):
    # Write your code here
    new_min=scores[0]
    new_max=scores[0]
    arr=[0,0]
    for i in scores:
        if i>new_max:
            new_max=i
            arr[0]+=1
        if i<new_min:
            new_min=i
            arr[1]+=1
    print(arr)

if __name__ == '__main__':
  

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)
