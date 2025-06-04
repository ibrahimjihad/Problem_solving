"""
Problem: Number Line Jumps

diff:easy


"""
def kangaroo(x1, v1, x2, v2):
    if x1 < x2 and v1 <= v2:
        return "NO"
    if x2 < x1 and v2 <= v1:
        return "NO"

    while x1 != x2:
        x1 += v1
        x2 += v2
        if (v1 > v2 and x1 > x2) or (v2 > v1 and x2 > x1):
            return "NO"
    return "YES"

if __name__ == '__main__':


    result = print(kangaroo(0,2,5,3))

