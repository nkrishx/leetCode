hashMap = {}
def threeN(n):
    if n in hashMap:
        return cache[n]
    if n == 1:
        return 0
    orig = n
    if n%2 == 0:
        n = n//2
    else:
        n = 3*n+1
    count = threen(n)+1
    hashMap[orig] = count
    return count

