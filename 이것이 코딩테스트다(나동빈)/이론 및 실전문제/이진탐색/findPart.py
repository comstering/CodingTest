N = int(input())
N_list = set(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

for i in M_list:
    print('yes' if i in N_list else 'no', end=' ')
# 이진 탐색 사용
"""
def binary_search_recursive(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search_recursive(array, target, start, mid - 1)
    else:
        return binary_search_recursive(array, target, mid + 1, end)

N = int(input())
N_list = sorted(list(map(int, input().split())))
M = int(input())
M_list = sorted(list(map(int, input().split())))


for i in M_list:
    print('yes' if binary_search_recursive(N_list, i, 0, N - 1) else 'no', end=' ')
"""