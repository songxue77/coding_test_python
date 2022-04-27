import operator

def solution(N, stages):
    answer = []
    failRatioByStage = {}
    stages.sort()

    for i in range(N):
        failCount = 0
        totalCount = 0
        for stage in stages:
            if (stage > i + 1):
                totalCount = totalCount + 1
            elif (stage == i + 1):
                totalCount = totalCount + 1
                failCount = failCount + 1

        failRatioByStage[i+1] = failCount / totalCount

    afterSorted = sorted(failRatioByStage.items(), key=operator.itemgetter(1),reverse=True)
    for value in afterSorted:
        answer.append(value[0])

    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4,4,4,4,4]))
