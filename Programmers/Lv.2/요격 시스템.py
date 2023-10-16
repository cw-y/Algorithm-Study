# main idea
# 1. 끝나는 지점을 기준으로 정렬한다.
# 2. 다음 시작점이 끝나는 점보다 크거나 같을 경우, 미사일 += 1, 새롭게 끝나는 점 갱신

def solution(targets):
    answer = 0
    targets.sort(key = lambda x: (x[1], x[0]))
    s = 0
    for target in targets:
        if target[0] >= s:
            answer += 1
            s = target[1]

    return answer

