# 문제 : https://www.acmicpc.net/problem/2606
# 문제 번호 : 2606

if __name__ == "__main__":
    computers = int(input())
    connected = int(input())
    i = 0
    status = []
    for computer in range(computers):
        status.append([])  # 컴퓨터 이차원 배열 만들기

    while connected > i:
        a, b = map(int, input().split())
        if a != 1:  # 목적지가 1번 컴퓨터이 아니면 양쪽 배열에 추가
            status[b-1].append(a)
        status[a-1].append(b)
        i += 1

    # print(status)
    for line in status[0]:  # 1번 컴퓨터에 연결된 컴퓨터 확인
        # print(int(str(line)))
        # print(status)
        for j in status[int(str(line))-1]:  # 1번 컴퓨터에 연결된 컴퓨터가 어디에 연결되어 있는지 확인
            if j not in status[0] and j != 1:
                status[0].append(j)

    print(len(set(status[0])))  # 중복 제거한 1번 컴퓨터에 연결된 컴퓨터의 수
