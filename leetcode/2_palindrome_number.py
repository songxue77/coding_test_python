def isPalindrome(x: int) -> bool:
    answer = False
    xString = str(x)
    xStringReversed = xString[::-1]

    if xString == xStringReversed:
        answer = True

    return answer


print(isPalindrome(121))
print(isPalindrome(-121))
print(isPalindrome(10))
print(isPalindrome(-101))