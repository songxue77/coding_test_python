def solution(numbers):
    answer = 0

    for i in range(0, 10):
        if i in numbers:
            continue
        else:
            answer += i

    return answer

print(solution([1,2,3,4,6,7,8,0]))
print(solution([5,8,4,0,6,7,9]))
