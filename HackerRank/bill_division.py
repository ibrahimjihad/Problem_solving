def bonAppetit(bill, k, b,n):
    cost=0
    for i in range(n):
        if i!=k:
            cost+=bill[i]
            
    if (cost//2)==b:
        print("Bon Appetit")
    else:
        print(b-(cost//2))


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b,n)
