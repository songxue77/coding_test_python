def solution(absolutes, signs):
    answer = 0

    for i, value in enumerate(absolutes):
        if signs[i] == True:
            answer = answer + absolutes[i]
        else:
            answer = answer - absolutes[i]

    return answer

print(solution([4,7,12], [True,False,True]))
