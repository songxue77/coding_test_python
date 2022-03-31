def solution(record):
    answer = []
    nameByUid = {}

    for text in record:
        if "Enter" in text:
            tempText = text.split(' ')
            nameByUid[tempText[1]] = tempText[2]
        elif "Leave" in text:
            continue
        else:
            tempText = text.split(' ')
            nameByUid[tempText[1]] = tempText[2]

    for text in record:
        if "Enter" in text:
            tempText = text.split(' ')
            answer.append(nameByUid[tempText[1]]+"님이 들어왔습니다.")
        elif "Leave" in text:
            tempText = text.split(' ')
            answer.append(nameByUid[tempText[1]]+"님이 나갔습니다.")
        else:
            continue

    #print(nameByUid)
    return answer

print(solution([
    "Enter uid1234 Muzi",
    "Enter uid4567 Prodo",
    "Leave uid1234",
    "Enter uid1234 Prodo",
    "Change uid4567 Ryan"
]))