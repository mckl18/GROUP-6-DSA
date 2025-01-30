def merge_sort(arr):
    steps = [arr[:]]  
    
    def _merge_sort(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]

            _merge_sort(left)  
            _merge_sort(right)  

            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1
                steps.append(arr[:])  

            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1
                steps.append(arr[:])  

            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1
                steps.append(arr[:]) 

    _merge_sort(arr)
    return arr, steps
