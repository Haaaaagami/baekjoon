# https://www.acmicpc.net/problem/11279
# 백준 자료구조 실버 2문제
# 11월 16일 시작

def swap(tree, index1, index2):
    temp = tree[index1]
    tree[index1] = tree[index2]
    tree[index2] = temp



class Heap:
    def __init__(self):
        self.heap = [None]

    def insert(self, data):
        self.heap.append(data)
        self.heapify(self.heap, len(self.heap)-1)

    def heapify(self, tree, index):
        left_child_index = index * 2
        right_child_index = index * 2 + 1
        largest = index
        tree_size = len(self.heap)

        if 0 < left_child_index < tree_size and tree[largest] < tree[left_child_index]:
            largest = left_child_index
        if 0 < right_child_index < tree_size and tree[largest] < tree[right_child_index]:
            largest = right_child_index

        if largest != index:
            swap(self.heap, largest, index)
            self.heapify(self.heap, largest)

    def reverse_heapify(self, tree, index):
        parent_index = index // 2
        if 0 < parent_index and tree[index] > tree[parent_index]:
            swap(tree, index, parent_index)
            self.reverse_heapify(tree, parent_index)

    def max_pop(self):
        if self.heap[-1] is None:
            return 0

        swap(self.heap, len(self.heap)-1, 1)
        return_value = self.heap.pop(-1)
        self.heapify(self.heap, 1)
        return return_value


h = Heap()
n = int(input())
for i in range(n):
    num = int(input())
    if not num:
        print(h.max_pop())
    else:
        h.heap.append(num)
        h.reverse_heapify(h.heap, len(h.heap)-1)

### 답은 맞지만 시간초과!

