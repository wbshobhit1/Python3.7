def awseomeSort (N, arr):
    arrev = []
    arrodd = []
    n= len(arr)
    for i in range (0,n):
        if arr[i] % 2 != 0:
            arrodd.append(arr[i])
            continue
        else:
            arrev.append(arr[i])
            continue
    arrdiv = []
    arrnodiv = []
    for j in range (0,len(arrev)):
        if arrev[j] % 5 == 0:
            arrdiv.append(arrev[j])
            continue
        else:
            arrnodiv.append(arrev[j])

    arrdiv.sort(reverse=True)
    list1 = arrdiv + arrnodiv
    list2 = list1 + arrodd
    return list2





T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    out_ = awseomeSort(N, arr)
    print (' '.join(map(str, out_)))