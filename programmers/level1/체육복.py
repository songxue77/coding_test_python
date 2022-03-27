#먼저 N+2 크기의 배열 u을 만들고 모두 1로 초기화합니다.
#reserve를 순회하여 존재하는 원소를 u의 인덱스로 하여 +1을 해줍니다.
#lost를 순회하여 존재하는 원소를 u의 인덱스로 하여 -1을 해줍니다.
#u를 1 <= i < N+1 범위만큼 순회합니다.
#만약 u[i-1] == 0 && u[i] == 2 인 경우, 체육복을 나눠줍니다.
#1의 조건이 아니고 u[i] == 2 && u[i+1] == 0 인 경우 체육복을 나눠줍니다.
#값이 0인 원소, 즉 체육복이 없는 학생의 수를 구하고 n에 빼줍니다.

def solution(n, lost, reserve):
    u = [1] * (n + 2)

    for i in reserve:
        u[i] += 1

    for i in lost:
        u[i] -= 1

    for i in range(1, n+1):
        if u[i-1] < 1 and u[i] > 1:
            u[i-1:i+1] = [1, 1]
        elif u[i] > 1 and u[i+1] < 1:
            u[i:i+2] = [1, 1]

    answer = n - len([e for e in u[1:-1] if e < 1])

    return answer