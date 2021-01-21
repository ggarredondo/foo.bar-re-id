

def solution(i):
    number_list = [True] * (i+1)

    n = 2
    while n*n <= i:
        if number_list[n]:
            for m in range(n*n, i+1, n):
                number_list[m] = False
        n += 1

    for n in range(2, i+1):
        if number_list[n]:
            print(n)
