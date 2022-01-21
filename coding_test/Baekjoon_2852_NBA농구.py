# 문제 : https://www.acmicpc.net/problem/2852
# 문제 번호 : 2852

if __name__ == "__main__":
    scoreSum = int(input())
    i = 0
    teamScore = [0, 0]  # 1팀, 2팀
    teamTime = [0, 0]  # 초 단위로 계산
    winFlag = [0, 0, 0]  # 이기는 팀, 시작 시간, 끝 시간

    while scoreSum > i:
        scoreTeam, scoreTime = map(str, input().split())
        scoreTimeM, scoreTimeS = map(int, scoreTime.split(':'))  # 시간 계산
        scoreTimeCal = scoreTimeM * 60 + scoreTimeS  # 시간 계산
        teamScore[int(scoreTeam)-1] += 1  # 팀 득점 계산

        if teamScore[0] > teamScore[1]:  # 1팀이 이기는 중
            if winFlag[0] == 0:  # 이전에 비기는 상태였다면
                winFlag = [1, scoreTimeCal, 0]  # 1팀이 scoreTimeCal 시간부터 이기는 중
        elif teamScore[0] < teamScore[1]:  # 2팀이 이기는 중
            if winFlag[0] == 0:  # 이전에 비기는 상태였다면
                winFlag = [2, scoreTimeCal, 0]  # 2팀이 scoreTimeCal 시간부터 이기는 중
        else:  # 비기는 중
            teamTime[winFlag[0] - 1] += scoreTimeCal - winFlag[1]  # 이전에 이기던 팀 시간 증가
            winFlag[2] = scoreTimeCal  # 이기던 마지막 시간 체크
            winFlag[0] = 0  # 비기는 중

        i += 1

    if winFlag[2] == 0:  # 끝 시간이 체크되지 않았다면
        teamTime[winFlag[0]-1] += 2880-winFlag[1]  # 우승팀 시간 추가 (48분 == 2880초)

    print("%02d:%02d" % (int(teamTime[0] / 60), int(teamTime[0] % 60)))
    print("%02d:%02d" % (int(teamTime[1] / 60), int(teamTime[1] % 60)))
