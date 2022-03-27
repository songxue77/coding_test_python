def solution(a, b):
    answer = 0

    for i, value in enumerate(a):
        answer = answer + a[i] * b[i]

    return answer

print(solution([1,2,3,4], [-3,-1,0,2]))