import sys
input = sys.stdin.readline

N = int(input())
st = set()

for i in range(N):
    a = input().rstrip().split()
    if len(a) == 2:
        if a[0]== 'add':
            st.add(int(a[1]))
        elif a[0] == 'remove':
            if int(a[1]) in st:
                st.remove(int(a[1]))
        elif a[0] == 'check':
            if int(a[1]) in st:
                print(1)
            else:
                print(0)
        elif a[0] == 'toggle':
            if int(a[1]) in st:
                st.remove(int(a[1]))
            else:
                st.add(int(a[1]))
    else:
        if a[0] == 'all':
            st = set([i for i in range(1, 21)])
        elif a[0] == 'empty':
            st = set()