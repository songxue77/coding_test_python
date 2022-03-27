def solution(array, commands):
    answer = []

    for i in commands:
        arraySliced = array[i[0] - 1 : i[1]]
        arraySliced.sort()

        if len(arraySliced) < i[2]:
            answer.append(arraySliced[-1])
        else:
            answer.append(arraySliced[i[2] - 1])

    return answer


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
