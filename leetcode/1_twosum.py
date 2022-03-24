from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    answer = []
    dic = {}

    for i, value in enumerate(nums):
        dic[value] = i

    for i, value in enumerate(nums):
        findValue = target - value
        if findValue in dic.keys():
            if dic[findValue] != i:
                answer = [i, dic[findValue]]

    return answer

twoSum([2,7,11,15], 9)
twoSum([3,2,4], 6)
twoSum([3,3], 6)