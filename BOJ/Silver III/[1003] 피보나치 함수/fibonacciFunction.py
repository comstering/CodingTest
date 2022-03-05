fibonacci_list = [0] * 100
fibonacci_count_list = [[0, 0] for i in range(100)]

def fibonacci(num):
    if num == 0:
        fibonacci_count_list[0] = [1, 0]
        return 0
    if num == 1:
        fibonacci_count_list[1] = [0, 1]
        return 1

    if fibonacci_list[num] != 0:
        return fibonacci_list[num]

    fibonacci_list[num] = fibonacci(num - 1) + fibonacci(num - 2)
    fibonacci_count_list[num] = [x + y for x, y in zip(fibonacci_count_list[num - 1], fibonacci_count_list[num -2])]
    return fibonacci_list[num]


t = int(input())

for _ in range(t):
    n = int(input())
    fibonacci(n)
    print(fibonacci_count_list[n][0], fibonacci_count_list[n][1])
