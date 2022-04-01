def solution(phone_book):
    phone_book.sort()
    answer = True
    for i in range(len(phone_book) - 1):
        for j in range(i + 1, len(phone_book)):
            if phone_book[j].find(phone_book[i]) == 0:
                answer = False
                break
        if not answer:
            break
    return answer


print(solution(["119", "97674223", "1195524421"]))    # false
print(solution(["123", "456", "789"]))    # true
print(solution(["12", "123", "1235", "567", "88"]))    # false