K, N = map(int, input().split())
lan = [int(input()) for _ in range(K)]

def binsch(lan, N, st, end):
    if st > end: return end
    mid = (st + end) // 2
    c = 0
    for i in lan: c += i // mid
    if c < N: return binsch(lan, N, st, mid-1)
    else: return binsch(lan, N, mid+1, end)

if K == 1:
    print(lan[0] // N)
else:   
    print(binsch(lan, N, 1, max(lan)))