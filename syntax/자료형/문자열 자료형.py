# 문자열 슬라이싱

a = "Life is too short, You need Python"
print(a[0:4]) # 0 <= a < 4


# 문자 개수 세기(count)
a = "hobby"
a.count('b')

# 위치 알려주기1(find)
a = "Python is the best choice"
a.find('b') # 14
a.find('k') # -1

# 위치 알려주기2(index)
a = "Life is too short"
a.index('t') # 8
a.index('k') # error
#try:
#    a.index('k') # error
#except ValueError as e:
#    print(e)

# 문자열 삽입(join)
",".join('abcd') #'a,b,c,d'
",".join(['a', 'b', 'c', 'd']) #'a,b,c,d'

# 소문자를 대문자로 바꾸기(upper)
a = "hi"
a.upper() # HI

# 대문자를 소문자로 바꾸기(lower)
a = "HI"
a.lower() # hi

# 왼쪽, 오른쪽, 양쪽 공백 지우기(lstrip)
a = " hi "
a.lstrip()
a.rstrip()
a.strip()

# 문자열 바꾸기(replace)
a = "Life is too short"
a.replace("Life", "Your leg") # 'Your leg is too short'

# 문자열 나누기(split)
a = "Life is too short"
a.split() # ['Life', 'is', 'too', 'short']
b = "a:b:c:d"
b.split(':') # ['a', 'b', 'c', 'd']
