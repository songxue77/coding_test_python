def solution(phone_book):
    #answer = True
    #phone_book.sort()

    #print(phone_book)

    #for i in range(len(phone_book)):
    #    for key, value in enumerate(phone_book):
    #        if key == i:
    #            continue
            #print(value)
            #print(len(value))
    #        if len(value) < len(phone_book[i]):
    #            continue

            #print(value[0:len(phone_book[0])])

    #        if phone_book[i] in value:
    #            answer = False
    #            break

    #return answer

    phoneBook = sorted(phone_book)

    print(phoneBook)
    print(phoneBook[1:])

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        print(p1)
        print(p2)
        if p2.startswith(p1):
            return False
    return True

#phone_book = ["119", "97674223", "1195524421"]
#phone_book = ["123","456","789"]
#phone_book = ["12","123","1235","567","88"]
phone_book = ["118", "119", "1191"]

result = solution(phone_book)

print(result)