def stars(n):
    if n == 3:
        return ["***", "* *", "***"]
    else:
        div = n // 3
        matrix = stars(div)
        result = []
        for i in range(n):
            star = matrix[i % div]
            if i // div == 1:
                result.append(star + " " * (n // 3) + star)
            else:
                result.append(star * 3)
        return result


num = int(input())
for i in stars(num):
    print(i)