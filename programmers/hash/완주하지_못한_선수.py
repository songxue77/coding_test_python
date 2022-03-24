def solution(participant, completion):
    participant.sort()
    completion.sort()
    answer = ''

    for idx, val in enumerate(participant):
        if idx > len(completion) - 1:
            answer = participant[idx]
            break
        elif participant[idx] != completion[idx]:
            answer = participant[idx]
            break
        else:
            continue

    return answer

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

answer = solution(participant, completion)
print(answer)
