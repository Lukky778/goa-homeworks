#1
def sort_by_length(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if len(arr[j]) < len(arr[min_index]):
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]  # ადგილების გაცვლა
    return arr

#2
def sequence_sum(begin_number, end_number, step):
    if begin_number > end_number:
        return 0
    return sum(range(begin_number, end_number + 1, step))

#3
def series_sum(n):
    total = 0
    denominator = 1
    
    for _ in range(n):
        total += 1 / denominator
        denominator += 3  
    
    return f"{total:.2f}"

#4
def round_to_next5(n):
    return ((n + 4) // 5) * 5

#5
    return sorted(ages)[-2:]