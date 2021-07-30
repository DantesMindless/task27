# task1
class Kolobok:
    def __init__(self, data):
        self.data = data
        self.right = None

    def __gt__(self, other):
        return self.data > other.data


class Stack:
    def __init__(self):
        self.begin = None
        self.__lenght = 0

    def push_data(self, data):
        info = Kolobok(data)
        info.right = self.begin
        self.begin = info
        self.__lenght += 1

    def pop_data(self):
        if self.begin:
            x = self.begin
            self.begin = x.right
            self.__lenght -= 1
            return x.data
        raise IndexError

    def extend(self, *args):
        for info in args:
            self.push_data(info)

    def __len__(self):
        return self.__lenght


class SortedList(Stack):
    def push_data(self, data):
        kolobok = Kolobok(data)
        prev = None
        current = self.begin
        if self.begin is None:
            self.begin = kolobok
            return
        if self.begin > kolobok:
            kolobok.right = self.begin
            self.begin = kolobok
            return
        while current:
            if current < kolobok:
                prev = current
                current = current.right
            else:
                prev.right = kolobok
                kolobok.right = current
                return
        if current >= kolobok or current is None:
            kolobok.right = current


# task2
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    left = [0] * (n1)
    right = [0] * (n2)
    for i in range(0, n1):
        left[i] = arr[l + i]

    for j in range(0, n2):
        right[j] = arr[m + 1 + j]

    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = left[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = right[j]
        j += 1
        k += 1

def mergeSort(arr, l, r):
    if l < r:
        m = (l + (r - 1)) // 2

        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)
#task3

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)