'''
10
123 1
2737 1
757148 1
78466 2
32888 2
777770 5
436659 2
431159 7
112233 3
456789 10

#1 321
#2 7732
#3 857147
#4 87664
#5 88832
#6 777770
#7 966354
#8 954311
#9 332211
#10 987645
'''
T = int(input())

for tc in range(T):
    card, N = map(str, input().split())
    N = int(N)
    card = list(map(int, card))