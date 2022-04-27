import itertools

def solution(dist):
    answer = []
    pointCount = len(dist)
    pointList = []
    for i in range(pointCount):
        pointList.append(i)

    pointPermutation = list(itertools.permutations(pointList, pointCount))
    #print(pointList)
    print(pointPermutation)
    for element in pointPermutation:
        elementList = list(element)
        #print(elementList)

        temp = 'success'
        try:
            for i,iValue in enumerate(elementList):
                lengthList = []
                #for j,jValue in enumerate(elementList[i+1:pointCount]):
                for j in elementList[i+1:pointCount]:
                    #print(j)
                    #print(jValue)
                    lengthList.append(dist[iValue][j])

                #if elementList == [1, 2, 0, 4, 3]:
                    #print(lengthList)
                if sorted(lengthList) != lengthList or len(lengthList) != len(set(lengthList)):
                    raise NotImplementedError
        except:
            temp = 'error' # nothing

        if temp == 'success':
            answer.append(elementList)
            elementListReversed = list(reversed(elementList))
            answer.append(elementListReversed)
            sorted(answer,key=lambda x: x[1])
            break

    return answer

print(solution([[0,5,2,4,1],[5,0,3,9,6],[2,3,0,6,3],[4,9,6,0,3],[1,6,3,3,0]])) #[[1,2,0,4,3],[3,4,0,2,1]]
#print(solution([[0,2,3,1],[2,0,1,1],[3,1,0,2],[1,1,2,0]])) #[[0,3,1,2],[2,1,3,0]]

