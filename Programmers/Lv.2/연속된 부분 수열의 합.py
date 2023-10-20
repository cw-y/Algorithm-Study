def solution(sequence, k):
    answer = []
    # 끝 좌표와 첫 좌표 설정 left&Right
    l = 0;
    r = -1
    s = 0

    while True:
        if s < k:
            r += 1
            if r >= len(sequence):
                break
            s += sequence[r]
        else:
            s -= sequence[l]
            if l >= len(sequence):
                break
            l += 1
        if s == k:
            answer.append([l, r])

    answer.sort(key=lambda x: (x[1] - x[0], x[0]))
    return answer[0]