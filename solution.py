

def sieve_of_eratosthenes(n):
    txt = ""
    number_list = [True] * (n + 1)

    i = 2
    while i * i <= n:
        if number_list[i]:
            for j in range(i * i, n + 1, i):
                number_list[j] = False
        i += 1

    for i in range(2, n+1):
        if number_list[i]:
            txt += str(i)

    return txt


def solution(i):
    string = sieve_of_eratosthenes(i)
    print(string)



