from itertools import combinations_with_replacement

def solution(grid):
    answer = -1
    gridRowCount = len(grid)

    positionArray = []
    for rowIndex, gridString in enumerate(grid):
        #print(gridString)
        for cIndex, c in enumerate(gridString):
            if c == '?':
                positionArray.append([rowIndex, cIndex])

    print(positionArray)
    abcCombinations = list(combinations_with_replacement(['a', 'b', 'c'], gridRowCount))
    #print(abcCombinations)

    for element in abcCombinations:
        elementList = list(element)
        for p in positionArray:
            print(p)

        #for e in elementList:
        #    print(e)

    #print(grid)

    return answer

def dfs(x, y, graph):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

print(solution(["??b", "abc", "cc?"]))
#print(solution(["abcabcab","????????"]))
#print(solution(["aa?"]))
