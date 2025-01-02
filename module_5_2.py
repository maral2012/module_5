nums = [5, 6, 2, 1, 3, 4]

def bubble_sort(ls):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(ls) - 1):
            if ls[i] > ls[i + 1]:
                ls[i], ls[i + 1] = ls[i + 1], ls[i]
                swapped = True
print(bubble_sort(nums))
print(nums)

