def solution(new_id):
    answer = new_id

    # 소문자로 치환
    answer = answer.lower()
    #print(answer)

    # 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거
    stringList = ['-','_','.']
    new_id_after_purified = []
    for c in answer:
        if c.isalpha() or c.isdigit() or c in stringList:
            new_id_after_purified.append(c)

    answer = ''.join(new_id_after_purified)
    #print(answer)

    #마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
    while(True):
        if '..' in answer:
            answer = answer.replace('..', '.')
        else:
            break
    #print(answer)

    #마침표(.)가 처음이나 끝에 위치한다면 제거
    if len(answer) > 0:
        if answer[0] == '.':
            answer = answer[1:]
    if len(answer) > 0:
        if answer[-1] == '.':
            answer = answer[:-1]
    #print(answer)

    #new_id가 빈 문자열이라면, new_id에 "a"를 대입
    if len(answer) == 0:
        answer = 'a'
    #print(answer)

    #new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거
    if len(answer) >= 16:
        answer = answer[0:15]
    #만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거
    if answer[-1] == '.':
        answer = answer[:-1]
    #print(answer)
        
    #new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙임
    if len(answer) <= 2:
        while(True):
            if len(answer) >= 3:
                break
            else:
                answer = answer + answer[-1]

    return answer

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))