import time
import random
import matplotlib.pyplot as plt

# 1. Алгоритм Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# 2. Алгоритм Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# 3. Настройки тестов
sizes = [1000, 5000, 10000, 50000] 
bubble_times = []
merge_times = []

print(f"{'Размер':<10} | {'Bubble Sort (сек)':<20} | {'Merge Sort (сек)':<20}")
print("-" * 55)

for s in sizes:
    data = [random.randint(0, 10000) for _ in range(s)]
    
    # Замеряем пузырек
    start = time.perf_counter()
    bubble_sort(data.copy())
    t_bubble = time.perf_counter() - start
    bubble_times.append(t_bubble)
    
    # Замеряем слияние
    start = time.perf_counter()
    merge_sort(data.copy())
    t_merge = time.perf_counter() - start
    merge_times.append(t_merge)
    
    print(f"{s:<10} | {t_bubble:<20.5f} | {t_merge:<20.5f}")

# 4. Рисуем график
plt.figure(figsize=(10, 6))
plt.plot(sizes, bubble_times, label='Bubble Sort (Медленный)', marker='o')
plt.plot(sizes, merge_times, label='Merge Sort (Быстрый)', marker='s')
plt.title('График эффективности сортировок')
plt.xlabel('Количество элементов')
plt.ylabel('Время (секунды)')
plt.legend()
plt.grid(True)
plt.show()
