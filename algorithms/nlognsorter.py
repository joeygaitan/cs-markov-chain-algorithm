arr = [1,4,6,1,4,6]

def sorting(arr):
    
    for (i, number) in enumerate(arr):
        if len(arr) -1 == i:
            return arr
        else:
            if arr[i+1] - number < 0:
                arr[i] = number
            elif arr[i+1] - number > 0:
                arr[i+1] = number             
    return arr

print(sorting(arr))