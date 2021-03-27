def countsub(a, n, k):
    count = 0
    for i in range(0, n):
        if a[i] < k:
            count += 1
        mul = a[i]
        for j in range(i + 1, n):
            mul = mul * a[j]
            if mul <k:
                count += 1
            else:
                break
    return count 
matA=[]
matB=[]
matA_rows,matA_cols=map(int,input().split())
for idx in range(matA_rows):
    matA.append(list(map(int,input().split())))
maxK=int(input())
for i in matA:
    for j in i:
        if j not in matB:
            matB.append(j)
n=len(matB)
print(countsub(matB,n,maxK))