print ("Numeros Passados: [4, 3, 5, 1, 9, 2, 7, 6]")

def partition(arr, l, r):
    x = arr[r]
    i = l
    for j in range(l, r):
        if arr[j] <= x:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            print("----------------------")
            print(f"Trocou {arr[j]} por {arr[i]}")
    arr[i], arr[r] = arr[r], arr[i]
    return i

def kthSmallest(arr, l, r, k):
    if (k > 0 and k <= r - l + 1):
        index = partition(arr, l, r)
        if (index - l == k - 1):
            return arr[index]
        if (index - l > k - 1):
            return kthSmallest(arr, l, index - 1, k)
        return kthSmallest(arr, index + 1, r, k - index + l - 1)
    print("Índice fora do limite")

arr = [4, 3, 5, 1, 9, 2, 7, 6]
n = len(arr)
k = 3
print(kthSmallest(arr, 0, n - 1, k))
print(" é o K-ésimo menor elemento", end = "")
