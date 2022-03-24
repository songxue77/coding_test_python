def solution(clothes):
    answer = 1

    if len(clothes) == 0:
        return 0

    dictionary = {}
    for value in clothes:
        if value[1] in dictionary:
            dictionary[value[1]] += 1
        else:
            dictionary[value[1]] = 1

    for key, value in dictionary.items():
        answer *= (value + 1)

    return answer - 1

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]

print(solution(clothes))