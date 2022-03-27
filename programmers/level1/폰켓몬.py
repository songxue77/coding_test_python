def solution(nums):
    count = int(len(nums) / 2)

    countByType = {}
    for i in nums:
        if i in countByType:
            countByType[i] = countByType[i] + 1
        else:
            countByType[i] = 1

    if (count > len(countByType)):
        answer = len(countByType)
    else:
        answer = count

    return answer

print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))
