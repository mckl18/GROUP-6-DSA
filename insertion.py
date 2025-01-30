def insertion_sort(arr):
    steps = [arr[:]]  
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            steps.append(arr[:])  
        arr[j + 1] = key
        steps.append(arr[:])  
    return arr, steps
