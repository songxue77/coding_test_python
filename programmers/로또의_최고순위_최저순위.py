def solution(lottos, win_nums):
    compareResult = set(lottos) & set(win_nums)
    lowScoreCount = len(compareResult)

    zeroCount = 0
    for num in lottos:
        if num == 0:
            zeroCount = zeroCount + 1

    highScoreCount = lowScoreCount + zeroCount

    if highScoreCount > 1:
        highRank = 7 - highScoreCount
    else:
        highRank = 6

    if lowScoreCount > 1:
        lowRank = 7 - lowScoreCount
    else:
        lowRank = 6

    return [highRank, lowRank]

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0],	[38, 19, 20, 40, 15, 25]))
print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))