from collections import deque


def combination(queue):
    result_queue = deque()
    for i in range(len(queue)-1):
        num1 = queue.popleft()
        num2 = queue.popleft()
        combination_num = num1 + num2
        result_queue.append(combination_num)
        queue.appendleft(num2)

    if len(result_queue) != 2:
        return combination(result_queue)
    else:
        result_num1, result_num2 = map(str, result_queue)
        return result_num1[-1] + result_num2[-1]

A = input()
B = input()

a_list = list(A)
a_list = [int(i) for i in a_list]
b_list = list(B)
b_list = [int(i) for i in b_list]

number_list = []
for i in range(len(a_list)):
    number_list.append(a_list[i])
    number_list.append(b_list[i])

queue = deque(number_list)
result = combination(queue)
print(result)
