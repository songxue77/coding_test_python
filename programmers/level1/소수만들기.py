import itertools

def solution(nums):
    numbers = []
    answer = 0
    nums = list(itertools.combinations(nums, 3))

    for i in range(len(nums)):
        numbers.append(sum(nums[i]))

    for i in numbers:
        count = 2
        for j in range(2, i):
            if i % j == 0:
                continue
            else:
                count += 1

        if count == i:
            answer += 1

    return answer

print(solution([1,2,3,4]))
print(solution([1,2,7,6,4]))
