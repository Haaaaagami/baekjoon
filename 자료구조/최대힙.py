# https://www.acmicpc.net/problem/11279
#
# 22년 11월 12일 시작
import sys


def swap(tree, index1, index2):
    temp = tree[index1]
    tree[index1] = tree[index2]
    tree[index2] = temp


def heapify(tree, index):
    l_child_index = index * 2
    r_child_index = index * 2 + 1
    largest = index
    tree_size = len(tree)

    if 0 < l_child_index < tree_size and tree[largest] < tree[l_child_index]:
        largest = l_child_index

    if 0 < r_child_index < tree_size and tree[largest] < tree[r_child_index]:
        largest = r_child_index

    if largest != index:
        swap(tree, largest, index)
        heapify(tree, largest)


def reverse_heapify(tree, index):
    parent_index = index // 2
    if 0 < parent_index < len(tree) and tree[index] > tree[parent_index]:
        swap(tree, index, parent_index)
        reverse_heapify(tree, parent_index)


class PriorityQueue:
    def __init__(self):
        self.heap = [None]

    def insert(self, data):
        if self.heap == [None]:
            self.heap.append(data)
        else:
            self.heap.append(data)
            reverse_heapify(self.heap, len(self.heap)-1)

    def max_pop(self):
        if self.heap[-1] is not None:
            swap(self.heap, 1, len(self.heap)-1)
            return_value = self.heap.pop(-1)
            heapify(self.heap, 1)
            return return_value
        else:
            return 0


n = int(sys.stdin.readline())
pq = PriorityQueue()
for i in range(n):
    num = int(sys.stdin.readline())
    if num:
        pq.insert(num)
    else:
        print(pq.max_pop())
