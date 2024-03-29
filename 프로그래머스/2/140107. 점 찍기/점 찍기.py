def solution(k, d):
    answer = 0
    for i in range(0, d+1, k):
        wer = (d**2 - i**2) ** 0.5 // k
        answer += wer + 1

    return int(answer)