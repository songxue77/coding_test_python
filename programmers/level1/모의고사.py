def solution(answers):
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    res = [0,0,0]
    for i in range(len(answers)):
        if a[i%5] == answers[i]:
            res[0] +=1
        if b[i%8] == answers[i]:
            res[1] += 1
        if c[i%10] == answers[i]:
            res[2] += 1
    return [idx+1 for idx, score in enumerate(res) if score == max(res)]

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))
