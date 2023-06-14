
print ("----------------------------------------")
print ("A matriz Original é: [4, 3, 5, 1, 9, 2, 7, 6]")
print ("----------------------------------------")

def partition(arr, l, h):
	i = ( l - 1 )
	x = arr[h]

	for j in range(l, h):
		if arr[j] <= x:

			i = i + 1
			arr[i], arr[j] = arr[j], arr[i]

	arr[i + 1], arr[h] = arr[h], arr[i + 1]
	return (i + 1)

def quickSortIterative(arr, l, h):
    
    size = h - l + 1
    stack = [0] * (size)

    
    top = -1

    
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h
    
    while top >= 0:
        # Pop h and l
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1
        
        p = partition(arr, l, h)

        # Print the pivot index
        print ("----------------------------------------")
        print(f"Pivo: {p}")
  
        print(f"Pilha: {stack}")
        print(f"Partição esquerda: {arr[l:p]}")
        print(f"Partição direta: {arr[p+1:h+1]}")
        
        if p-1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1

        if p + 1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h

arr = [4, 3, 5, 1, 9, 2, 7, 6]
n = len(arr)
quickSortIterative(arr, 0, n-1)
print ("----------------------------------------")
print("Matriz Ordenada é: ")
for i in range(n):
    print("%d" % arr[i])
print ("----------------------------------------")
