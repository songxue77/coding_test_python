s1 = set([1,2,3])

s2 = set("Hello")

# 집합 자료형의 특징

# 중복을 허용하지 않는다.
# 순서가 없다(Unordered).

l1 = list(s1)

# 교집합, 합집합, 차집합 구하기
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 교집합
print(s1 & s2) # {4, 5, 6}
print(s1.intersection(s2)) # {4, 5, 6}

# 합집합
print(s1 | s2) # {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(s1.union(s2))

# 차집합
print(s1 - s2) # {1, 2, 3}
print(s2 - s1) # {8, 9, 7}

print(s1.difference(s2)) # {1, 2, 3}
print(s2.difference(s1)) # {8, 9, 7}

# 값 1개 추가하기(add)
s1 = set([1, 2, 3])
s1.add(4)

# 특정 값 제거하기(remove)
s1 = set([1, 2, 3])
s1.remove(2)
