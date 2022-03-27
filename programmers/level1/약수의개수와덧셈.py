def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        if getDivisor(i) % 2 == 0:
            answer = answer + i
        else:
            answer = answer - i

    return answer

def getDivisor(n):
    divisorsList = []

    for i in range(1, n + 1):
        if (n % i == 0) :
            divisorsList.append(i)

    return len(divisorsList)

print(solution(13, 17))
print(solution(24, 27))