"""СОРТИРОВКА ВЫБОРОМ"""


def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return f"индекс меньшего элемента: {smallest_index}"

joj = [12, 41, 1]
print(find_smallest(joj))