

class LambdaString:
    def __init__(self, ndigits):
        self.string = ""
        self.initial = 2
        self.set_digits(ndigits)

    def __sieve_of_eratosthenes(self, n):
        sieve = [True] * (n+1)

        i = 2
        while i*i <= n:
            if sieve[i]:
                for j in range(i*i, n+1, i):
                    sieve[j] = False
            i += 1

        for i in range(self.initial, n+1):
            if sieve[i]:
                self.string += str(i)
        self.initial = n+1

    # Sieve of Eratosthenes is used from 2 through n. If the resulting string
    # is not equal or above the number of digits, Sieve of Eratosthenes is done
    # again from 2 to n+50%. Repeat until the condition is met.
    def set_digits(self, ndigits):
        n = ndigits
        self.__sieve_of_eratosthenes(n)
        while len(self.string) < ndigits:
            n += n/2
            self.__sieve_of_eratosthenes(n)

    def get_string(self):
        return self.string


# Precondition: i must be between 0 and 10000
def solution(i):
    return LambdaString(i+5).get_string()[i:i+5]
