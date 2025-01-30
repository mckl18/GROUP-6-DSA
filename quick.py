def quick_sort(arr):
    steps = [arr[:]]  
    
    def _quick_sort(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            _quick_sort(arr, low, pi - 1)  
            _quick_sort(arr, pi + 1, high) 
        return arr

    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                steps.append(arr[:]) 
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        steps.append(arr[:])  
        return i + 1

    _quick_sort(arr, 0, len(arr) - 1)
    return arr, steps
